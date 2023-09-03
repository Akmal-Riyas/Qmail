import ssl
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import math
import random

# default acc

default_acc_pass = 'test'
default_acc_email = 'yourdomain@yourdomain.com'


class SMTP:
    def __init__(self, EMAIL = default_acc_email, PASSWORD = default_acc_pass, port = 465, reciever_emails = [], smtp = 'smtp.gmail.com', cc = None, bcc = None):
        self.creator = 'Akmal Riyas'

        self.email = EMAIL
        self.password = PASSWORD
        self.to_send = reciever_emails

        self.domain = smtp
        

        self.context = ssl.create_default_context()
        self.port = port

        self.cc = cc
        self.bcc = bcc

    ### SEND TYPES ###
    
    def send_mail(self, message):
        message = self.add_msg_headers(message)
        

        if self.to_send != []:
            for email in self.to_send:
                self.send(reciever_mail=email, data= message.text)
    

    ### SEND ###
    
    def send(self, reciever_mail, data, type = 't'):
        
        try:

            with smtplib.SMTP_SSL(self.domain, self.port, context=self.context) as server:
                server.login(self.email, self.password)
                
                server.sendmail(self.email, reciever_mail, data.as_string())
            
            print(f'Mail Sent to {reciever_mail} \n')
        
        except Exception as e:
            print(e)


    ### SPAM ###
    def spam_mail(self, message,  num = 5):
        message = self.add_msg_headers(message)
        for num in range(0, num):
            print(num +1)
            for mail in self.to_send:
                self.send(reciever_mail= mail, data=message.text)
            
            
            time.sleep(1)

    
    def add_msg_headers(self,msg):
        msg.text['From'] = self.email
        msg.text['To'] = self.to_send[0]

        if self.cc != None:
            msg.text['CC'] = self.cc
            self.to_send.append(self.cc)
        
        elif self.bcc != None:
            self.to_send.append(self.bcc)

        
        return msg




class MSG:
    def __init__(self, subject = 'msg', txt= 'hi', attachments = []):
        self.text = MIMEMultipart("alternative")
        self.text["Subject"] = subject
        self.text.attach(MIMEText(txt, "plain"))

        if attachments != [] or attachments != '':
            files = FILES(attachments)
            
            for file in files.parts:
                self.text.attach(file)



    def print_message(self):
        print(self.text.as_string())

class FILES:
    def __init__(self, files):
        self.parts = []

        if type(files) == str:
           self.parts.append(self.create_part(files))
    
        elif type(files) == list:

            for file in files:
                self.parts.append(self.create_part(file))
                

    def create_part(self,file):
        with open(file, "rb") as attachment:              
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {file}",
            )
        
        return part

class HTML_MSG:
    def __init__(self, subject = 'html msg', txt = '', html= '<h1> HI </h1>', attachments = []):
        self.text = MIMEMultipart("alternative")
        self.text["Subject"] = subject

        if txt != '':
            self.text.attach(MIMEText(txt, "plain"))
            self.text.attach(MIMEText(html, "html"))
            
        
        else:
            self.text.attach(MIMEText(html, 'html'))
        
        if attachments != [] or attachments != '':
            files = FILES(attachments)
            
            for file in files.parts:
                self.text.attach(file)
        
        
        
        

    def print_message(self):
        print(self.text.as_string())

