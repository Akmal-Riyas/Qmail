import Qmail


txt_msg = """
In the digital realm, where the currents of communication flow ceaselessly, I extend my virtual hand in greeting. With the gentle click of keys and the hum of electrons, 
I embark on this electronic journey to share thoughts, ideas, and moments with you. As the bits and bytes traverse the vast expanse of the internet, 
they carry with them the essence of our connection, transcending distances and bridging our worlds.
Welcome to this exchange, where words become bridges, and together, we navigate the boundless seas of cyberspace."""

html_msg = """
<!DOCTYPE html>
<html>
<body>

<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>

</body>
</html>

"""

otp = Qmail.OTP.generateOTP(lenght=4)

EMAIL = 'aranimation2020@gmail.com'
PASSWORD = 'vsxcshkptsgawqdq'

sender = Qmail.SMTP(emails = ['akmalriyas@gmail.com'], smtp= 'smtp.gmail.com', bcc=EMAIL)

#message = eml.HTML_MSG( subject='HTML TEST', html=html_msg, attachments=['hi.txt','hi2.txt'])

#message = eml.HTML_MSG( subject='HTML TEST', html=html_msg)

#message = easymail.MSG(subject='TEXT MSG', txt=txt_msg, attachments=['hi.txt','hi2.txt'])

message = Qmail.OTP.OTP_EMAIL(subject='OTP MAIL DEFUALT', otp=otp, theme='modern', brand_name='Tecrontec')

#message.print_message()

sender.send_mail( message=message)

#sender.spam_mail(message=message, num= 5)



