# Mass Email Sender - Gmail

* Allows a user to automate the sending of many emails to a customizable list of recipients. 
* Initially created for a friend who needed to send thousands of individual emails manually.

## Description

* gmail_automate.py - script which loops through a user defined list of email addresses and sends an email, which can be edited as needed by the user. 
* names.txt - user defined list of email addresses to be email recipients.
* poster.jpeg - resizeable image that can be included at foot of email

### Required Steps: 
* make changes to the username and password as desbribed under depedencies
* edit the html to change the body of the message 
```html
 msg.add_alternative("""\
<html>
    <body>
        <p>
        example email body message here
        </p>
        <img src="cid:{image_cid}", width = "450", height = "750">
    </body>
```
* if wanted, add/edit/delete the poster.jpeg to add a custom photo to the email
* edit the names.txt file to specify who to send the email to

## Getting Started

### Dependencies

* must have python 3 installed on machine
* additionally, user must have a google account with 2 factor authtification turned on to generate an access code by the following steps:
* 1
    * Under account find security settings
    * Enable 2 step auth (will prompt to log in)
    * enter phone number and enter code via text mesaage
    * after completed, you should be prompted that 2fa is enabled.
* 2
    * go to myaccount.google.com/apppasswords
    * on drop-down menu select "other" -> type 'python' & hit generate
    * copy and paste this code into the gmail_automate.py script as the variable "email_password"
    * save your google account email address as the variable "email_sender"


### Installing/Executing

* directly download the folder or clone the repo
* after editing is done, navigate to the directory where the files are located
* run python gmail_automation.py


## Help
* note: if you want an image at the foot of the email, change the poster.jpeg to required photo
* otherwise -> comment out the following line: 
```html
 <img src="cid:{image_cid}", width = "450", height = "750">
```
* note: Gmail will limit 500 emails per day per account 
* if you have previusly installed python 2, you may need to use the python3 command. 
