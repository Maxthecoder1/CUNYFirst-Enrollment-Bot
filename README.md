# CUNYFirst-Enrollment-Bot
This a CUNYFirst bot that notifies you through text and email when there are changes in your enrollment shopping cart. Use this bot and you won't have to sit at your computer and be stressed about not knowing when a class opens up. The bot works by automatically logging you in and heading to your shopping cart. Once at the shopping cart the bot will refresh every 60 seconds by default although you can change that variable in the script.

# Requirements
1. Make sure you have python 3.5.1 installed on your computer. Go into your 'Advanced System Settings' and add the python.exe to your Path if you have not already done so. Also add the location of firefox.exe and the location of the geckodriver.exe(which I included with the script) to your Path variable.

2. Go to 'https://twilio.com' and sign up for a free account. Once you are verified and have gotten a twilio number, take the twilio number, auth token, and accountsid, and put them in the script with quotest next to the variables that have the same name. This will allow you to receives text updates when your classes open up.

3. Go to 'https://myaccount.google.com/security' and scroll all the way to he bottom. Then go to where it says 'Allow less secure apps: ON' and check OFF. You should get an email about the change. Go ahead and update the script to have your gmail email/user and password to send emails to your yourself

4. Go to CUNYFIRST, Click Enroll. Then choose your Term. Once you are are on the Shopping Cart Page, Right + Click on the 'add' button and Click on 'Copy Link Location'.  Then paste the link next to self.addshoppingcartlink in the script. It should look like the link below:

    self.addshoppingcartlink = 'https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=12345678&ENRL_REQUEST_ID=&INSTITUTION=BKL01&STRM=1172'
    
# How to Run
-open a console window in the same folder as the script. Type 'python cunyenrollment.py'. After a biref moment a Firefox window will open and the bot the will do the rest. **DO not alter the window or else the bot will stop working. Also for now the bot does not work with combined section classes where there is a lab and lecture. ENJOY.**

![Bot in Action](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/Screen%20Shot%202016-11-23%20at%2011.36.16%20AM.png?raw=true "CUNYFirst Enrollment Bot")
