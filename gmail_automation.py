import smtplib
import ssl
from email.message import EmailMessage
#post image support
from email.utils import make_msgid
import mimetypes

# Define email sender
email_sender = '@gmail.com' # email name 
email_password = 'xxxxxxxx' #sender email password -- do not make public to repo
msg = EmailMessage()

# set the plain text body
msg.set_content('')

# now create a Content-ID for the image
image_cid = make_msgid(domain='xyz.com')
# if `domain` argument isn't provided, it will 
# use your computer's name

# set an alternative html body
msg.add_alternative("""\
<html>
    <body>
        <p>
To Whom it May Concern,<br>
<br>
Authors Jarrod Shusterman & Sofía Lapuente here—we hope this message finds you well! :) We’re reaching out because our mission is to get kids reading,
and we're doing a virtual tour and wanted to know if your school or your district would be interested in a virtual motivational author visit! <br>
<br>
(If you're the wrong person to talk to, if you would be so kind to forward this to the English Department or librarian that would be greatly appreciated)<br>
<br>
As New York Times bestselling authors and UCLA professors of creative writing, connecting with teens through YA literature is our passion! My novel DRY,
made many award lists, which I co-wrote with Author Neal Shusterman (Unwind & Scythe series).<br>
<br>
We have no speaking fee--we just ask for a minimum order of 35 books of our upcoming Simon & Schuster title, RETRO, for your students or library.
(digital samples of book available for serious inquiries) Although it’s a fun YA  thriller, RETRO handles important issues like cyberbullying <br>
and responsible technology usage, which is why we want to make sure we can get it in the hands of as many teens as possible!<br>
<br>
Thank you so much for your time! If you’d like more info about what we do, we can send you a detailed powerpoint presentation.<br>
Feel free to email us at whenever— we’re here for you! Please respond to Jarrodshusterman19@gmail.com<br>
<br>
(Oh and we promise this is a legitimate email, and if there is any doubt feel free to DM us on our social media)<br>
<br>
Warmest regards :)<br>
<br>
Sofi & Jarrod<br>
Tiktok/IG @sofiandjarrod<br>
        </p>
        <img src="cid:{image_cid}", width = "450", height = "750">
    </body>
</html>
""".format(image_cid=image_cid[1:-1]), subtype='html')



# now open the image and attach it to the email
with open('poster.jpeg', 'rb') as img:

    # know the Content-Type of the image
    maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

    # attach it
    msg.get_payload()[1].add_related(img.read(), 
                                         maintype=maintype, 
                                         subtype=subtype, 
                                         cid=image_cid)

recipient_list = open("names.txt").read().splitlines()

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








