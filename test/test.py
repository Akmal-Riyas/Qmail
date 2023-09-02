import Qmail

test1 = Qmail.SMTP(\
    EMAIL='yourmail@yourdomain.com', # Default: emailsender437@gmail.com

    PASSWORD= 'Your App Password', # Default: emailsender437 pass
    
    smtp= "smtp.domain.com", # Ex: smtp.gmail.com, Default : smtp.gmail.com

    reciever_emails= ["Mail To send1", "Mail To Send2", 'exc.'],  # Emails that will be recieving mails.

    port='port to send email in', # Optional

    cc='cc email address', # Give this value if cc needed in email

    bcc= 'bcc email address', # Give this value if bcc needed in email
    )  

sender = Qmail.SMTP(reciever_emails= ['email1@gmail.com']) # Create a default Qmail smtp server 

sender2 = Qmail.SMTP(\
    EMAIL='Your Mail Goes Here', 
    PASSWORD= "Your EMAIL'S app password goes here.", 
    reciever_emails=['receicermail@yourdomain.com'], 
    smtp= 'Your Emails Smtp Server'

) # Create a Qmail smtp server with your email. 


# Qmail MSG class is for PLAIN Emails

message = Qmail.MSG(\
    subject= 'Subject Of Email',
    txt= 'txt in the email',
   #attachments=['file1', 'file2'] # Add Attachment Filepaths here 

    )

message = Qmail.HTML_MSG(\
    subject= 'Subject Of Email',
    html= '<h1>Enter Html Here</h1>',
    #attachments=['file1', 'file2'] # Add Attachment Filepaths here 

    )


from Qmail import OTP

one_time_password = OTP.generateOTP(lenght=10, type='alphanumeric')
NAME = 'Qmail'

themes_available = ['simple', 'default', 'modern']


message = OTP.OTP_EMAIL(subject='OTP MAIl', otp=one_time_password, brand_name=NAME, theme='default')