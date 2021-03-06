![CUNYFIRST Enrollment Bot](http://www2.cuny.edu/wp-content/uploads/sites/4/page-assets/about/administration/offices/budget-and-finance/CUNYfirst.jpeg?raw=true "CUNYFIRST Enrollment Bot")
# CUNYFirst Enrollment Bot
This a CUNYFirst Enrollment bot that notifies you through text and email when there are changes in your enrollment shopping cart. Use this bot and you won't have to sit at your computer and be stressed about not knowing when a class opens up. The bot works by automatically logging you in and heading to your shopping cart. Once at the shopping cart the bot will refresh every 60 seconds by default althogh (you can change that variable in the code). The text/email will show the class section followed by the original status and the latest status of the class.
![CUNYFIRST TEXT UPDATE](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/TextUpdate.PNG?raw=true "CUNYFIRST TEXT UPDATE")
---------------------------------------------------------------------------------------------------------------------------
![CUNYFIRST EMAIL UPDATE](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/emailupdate.png?raw=true "CUNYFIRST EMAIL UPDATE")
---------------------------------------------------------------------------------------------------------------------------
![CUNYFIRST Course Closed to Open](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/Course_closed_to_open.png?raw=true "CUNYFIRST Course Closed to Open")

# Requirements
1. Make sure you have python 3.5.1 installed on your computer. Go into your 'Advanced System Settings' and add the python.exe to your Path if you have not already done so. Also add the folder location of phantomjs.exe(which I included with the bot) to your PATH variable. The bot will not work without the location in the PATH variable for your system. Restart your computer after you make changes to your PATH variable.

2. Go to 'https://twilio.com' and sign up for a free account. Once you are verified and have gotten a twilio number, take the **twilio number, auth token, and accountsid**, and put them in the code with quotes next to the variables that have the same name. This will allow you to receives text updates when your classes open up.
![Twilio Info](https://www.twilio.com/blog/wp-content/uploads/2016/08/oy1Q-OazNr90Wl8URRpS0KweZBf8I285WuRzabOWpLUvNGY18ftMbdmlRLckbQHS1RibmdszmnkGLrnO2pc1vDJyor1l74M-Eu_Dl45eDUUBXySUQfOzMwPWj04HSvSVyPr7B2X0.png?raw=true "Twilio Info")

3. Go to 'https://myaccount.google.com/security' and scroll all the way to he bottom. Then go to where it says 'Allow less secure apps: ON' and check OFF. You should get an email about the change. Go ahead and update the code to have your gmail email/user and password to send emails to your yourself
![Google Account](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/myaccountgoogle.png?raw=true "Google Account Security")

4. Go to CUNYFIRST, Click Enroll. Then choose your Term. Once you are are on the Shopping Cart Page, Right + Click on the 'add' button and Click on 'Copy Link Location'.  Then paste the link next to self.addshoppingcartlink in the code. It should look like the link below:

    self.addshoppingcartlink = 'https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=12345678&ENRL_REQUEST_ID=&INSTITUTION=BKL01&STRM=1172'
    
![CUNYFIRST Add Link](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/addlinkcart.png?raw=true "CUNYFIRST Add Link")
    
# How to Run
-Make sure you add phatomjs.exe to your System PATH variable or else the bot will not work. Open a console/terminal window in the same folder as the bot. Type **python cunyenrollment.py**. After a brief moment a Firefox window will open and the bot the will do the rest.

![Bot in Action](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/Screen%20Shot%202016-11-23%20at%2011.36.16%20AM.png?raw=true "CUNYFirst Enrollment Bot")
----------------------------------------------------------------------------------------------------------------------------
![Bot in Action3](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/textupdate2.PNG?raw=true "CUNYFirst Enrollment Bot")
----------------------------------------------------------------------------------------------------------------------------
![Bot in Action2](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/openclosedopen.png?raw=true "CUNYFirst Enrollment Bot")
----------------------------------------------------------------------------------------------------------------------------
