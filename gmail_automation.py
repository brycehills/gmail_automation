import smtplib
import ssl
from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes

# Define email sender
email_sender = 'yourname123@gmail.com' # email name 
email_password = '16digitcode' #sender email password -- do not make public to repo
msg = EmailMessage() # emailmsg object

# set the plain text body
msg.set_content('')

# now create a Content-ID for the image
image_cid = make_msgid(domain='xyz.com')

# set an alternative html body
msg.add_alternative("""\
<html>
    <body>
        <p>
        </p>
        <img src="cid:{image_cid}", width = "450", height = "750">
    </body>
</html>
""".format(image_cid=image_cid[1:-1]), subtype='html')

# now open the image and attach it to the email
with open('poster.jpeg', 'rb') as img:

    # know the Content-Type of the image
    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    # attach
    msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)

# build list seperated by newline from file
recipient_list = open("names.txt").read().splitlines()

#loop over emails grabbed from names.txt
for i in range(len(recipient_list)):
    # Set the subject and body of the email
    subject = 'Author Visit'
    msg['From'] = email_sender
    msg['To'] = recipient_list[i]
    msg['Subject'] = subject

    # Add SSL --  Log in and send the email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, recipient_list[i], msg.as_string())

    #avoid multiple headers error
    del msg['To']
    del msg['From']
    del msg['Subject']








