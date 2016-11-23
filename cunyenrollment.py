import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import TwilioRestClient
import smtplib
import time


class CunyFirstEnrollmentShoppingCartNotifier(object):
    def __init__(self):
        '''change these variables to fit your needs'''
        '''Go to twilio.com and create a free account'''
        self.accountsid = '??????????????'                       # accountsid for twilio account, required to receive texts
        self.authtoken = '????????????'                          # authtoken for twilio account, required to receive texts
        self.mycellphone = '????????'                            # your cell phone number
        self.twiliocell = '???????'                              # twilio cellnumber that will be used to send texts to your actual phone
        self.username = '????????'                               # CUNYFIRST USERNAME
        self.password = '????????'                               # CUNYFIRST PASSWORD
        '''In order to receive an email you must go myaccount.google.com/security and scroll all the way to he bottom.
           Then go to where it says 'Allow less secure apps: ON' and check OFF. You should get an email about the change '''
        self.gmailuser= '???????????'                            # GMAIL USER
        self.gmailpass= '??????????'                             # GMAIL PASSWORD
        self.recipient = '????????????'                          # Recipient email address (most likely your email)
        self.interval = 60                                       # refresh interval in seconds

        '''Add shopping cart link is very important to this script. Go to CUNYFIRST, Click Enroll. Then choose your Term.
           Once you are are on the Shopping Cart Page, Right + Click on 'add' and Click on 'Copy Link Location'.
           Then copy and paste in here with single quotes. It should look like the link below'''
        self.addshoppingcartlink = 'https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=12345678&ENRL_REQUEST_ID=&INSTITUTION=BKL01&STRM=1172'

        print("Starting Firefox and heading to CUNYFIRST")
        self.driver = webdriver.Firefox()
        self.driver.get('https://home.cunyfirst.cuny.edu')
        login = WebDriverWait(self.driver, timeout=30).until(
            EC.presence_of_element_located((By.NAME, "login")))
        login.send_keys(self.username)
        passs = self.driver.find_element_by_name("password")
        passs.send_keys(self.password, Keys.ENTER)
        studentcenter = WebDriverWait(self.driver, timeout=30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Student Center")))
        studentcenter.click()
        self.driver.get(self.addshoppingcartlink)
        shoppingcartlen = len(self.driver.find_elements_by_xpath("//table[@id='SSR_REGFORM_VW$scroll$0']/tbody/tr")) - 2
        self.shoppingcart = {}
        for i in range(0, shoppingcartlen):
            classname = self.driver.find_element_by_name('P_CLASS_NAME$' + str(i)).text  # does not work for joined sections (lecture, and lab)
            status = self.driver.find_element_by_xpath(
                "//div[@id='win0divDERIVED_REGFRM1_SSR_STATUS_LONG$" + str(i) + "']/div/img").get_attribute('alt')
            self.shoppingcart[classname] = status

    '''While the script is running do not close or mess with the firefox window that the script opens'''
    def run(self):
        while True:
            print("refresh in {0} seconds".format(self.interval))
            time.sleep(self.interval)
            self.driver.get(self.addshoppingcartlink)
            latestshoppingcart = {}
            latestshoppingcartclasses = len(
                self.driver.find_elements_by_xpath("//table[@id='SSR_REGFORM_VW$scroll$0']/tbody/tr")) - 2
            for i in range(0, latestshoppingcartclasses):
                classname = self.driver.find_element_by_name('P_CLASS_NAME$' + str(i)).text
                status = self.driver.find_element_by_xpath(
                    "//div[@id='win0divDERIVED_REGFRM1_SSR_STATUS_LONG$" + str(i) + "']/div/img").get_attribute('alt')
                latestshoppingcart[classname] = status
            modified = self.dict_compare(self.shoppingcart, latestshoppingcart)
            if bool(modified):
                print(modified)
                self.send_email(user=self.gmailuser, pwd=self.gmailpass, recipient=self.recipient,
                                subject='CUNYFIRST ENROLLMENT SHOPPING CART', body=str(modified))
                self.textmyself(str(modified))
                modified.clear()
                self.shoppingcart.clear()
                self.shoppingcart = latestshoppingcart.copy()
                latestshoppingcart.clear()
                continue
            elif len(self.shoppingcart) > len(latestshoppingcart) or len(self.shoppingcart) < len(latestshoppingcart):
                print('you added or removed classes')
                self.shoppingcart.clear()
                self.shoppingcart = latestshoppingcart.copy()
                print(self.shoppingcart)
                latestshoppingcart.clear()
                continue
            else:
                continue

    def dict_compare(self, d1, d2):
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())
        intersect_keys = d1_keys.intersection(d2_keys)
        modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
        return modified

    def textmyself(self, message):
            twilioCli= TwilioRestClient(self.accountsid, self.authtoken)
            twilioCli.messages.create(body=message, from_=self.twiliocell, to=self.mycellphone)

    def send_email(self, user, pwd, recipient, subject, body):
        gmail_user = user
        gmail_pwd = pwd
        FROM = user
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = subject
        TEXT = body
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            print('successfully sent the mail')
        except:
            print("failed to send mail")


if __name__ == "__main__":
    a = CunyFirstEnrollmentShoppingCartNotifier()
    a.run()

