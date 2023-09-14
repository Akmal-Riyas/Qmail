![Qmail]([https://document-export.canva.com/VriQM/DAFtJZVriQM/6/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20230902%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230902T025303Z&X-Amz-Expires=63287&X-Amz-Signature=bc0fc9df17ebc416eefb9d9a7af03ebc65fff9eed1030d5e9f4c0fa00227a1d5&X-Amz-SignedHeaders=host&response-expires=Sat%2C%2002%20Sep%202023%2020%3A27%3A50%20GMT](https://document-export.canva.com/VriQM/DAFtJZVriQM/6/thumbnail/0001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQYCGKMUHWDTJW6UD%2F20230913%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230913T025303Z&X-Amz-Expires=88487&X-Amz-Signature=70a54acf4c9f8c548570ea46df6fe2f0ad9d378394fffa6e9319ed7512fb367a&X-Amz-SignedHeaders=host&response-expires=Thu%2C%2014%20Sep%202023%2003%3A27%3A50%20GMT))

###

## In this documentation 👇
- #### [Pypi](https://pypi.org/project/Qmail/)
- #### [Features](#features)
- #### [Usage](#usage)
  - ##### [Install Qmail](#installation)
  - ##### [SMTP](#smtp)
  - ##### [Qmail MSG Class](#qmail-msg-class)
  - ##### [Qmail HTML MSG Class](#qmail-html-msg-class)
  - ##### [Qmail OTP](#qmail-otp-services)
 
- #### [Authors](#authors)
- #### [Modules Used](#modules-used)

###

## Features

Qmail makes sending emails Quick and easy:

#### 📨 Email Smtp:
  - Supports all email providers supported with Python. (Defaulted at  smtp.gmail.com)
  - Email Spam Bot 
  - HTML, PLAIN, Attachments
  

#### 🔑 OTP Services:
  - OTP Msg class used with Email Smtp
  - OTP Generator (Alpha Numerical & Numerical)
  - 3 HTML Themes
 



###

## USAGE

### Installation

1. Python 3.8 or newer environment recommended


2.  Install Qmail

    *Open up terminal and type*

    ```
    pip install Qmail
    ```
    *For mac*

    ```
    pip3 install Qmail
    ```



### SMTP

##### Create Qmail Smtp class.
#
1. import the Qmail library
    ```python
    import Qmail
    ```

2.  Create Qmail Class

    ```python
    sender = Qmail.SMTP(\
        EMAIL='yourmail@yourdomain.com',
    
        PASSWORD= 'Your App Password', 
        
        smtp= "smtp.domain.com", # Ex: smtp.gmail.com, Default : smtp.gmail.com
    
        reciever_emails= ["Mail To send1", "Mail To Send2", 'etc.'],  # Emails that will be receiving mail.
    
        port='port to send email in', # Optional
    
        cc='cc email address', # Give this value if cc is needed in the email
    
        bcc= 'bcc email address', # Give this value if bcc is needed in the email
    )  
    
    ```
    
    #### SMTP Class Parameters In Detail👇
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### EMAIL
    #####
    Your Email Goes Here
    Strings Are Only Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### PASSWORD
    #####
    The app password of the email you gave in EMAIL parameter.
    Strings __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### smtp
    #####
    The SMTP server of your email's domain
    Ex: smtp.gmail.com for  __gmail.com__ domain
   Strings __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### reciever_emails
    #####
    Emails of the people your sending to goes here
    Ex: ['email1@gmail.com', 'email2@outlook.com', 'email3@yahoo.com']
    Lists accepted __ONLY__
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### port *|Optional|*
    #####
    The Port Number goes here (for SSL connections)
    Default: 465
    3 Digit Integers __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### cc *|Add this value if you want an email to be sent as CC|*
    #####
    CC Email goes here
    Strings __ONLY__ accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### bcc *|Add this value if you want an email to be sent as BCC|*
    #####
    BCC Email goes here
    Strings __ONLY__ accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ###
    #### More Creation Examples
    ```python
    import Qmail
    
    sender2 = Qmail.SMTP(\
        EMAIL='Your Mail Goes Here', 
        PASSWORD= "Your EMAIL'S app password goes here.", 
        reciever_emails=['receicermail@yourdomain.com'], 
        smtp= 'Your Emails Smtp Server
    
    ) # Create a Qmail smtp server with your email. 

    ```
###

##### Send Emails
#####
1. Invoke the send_mail function on Qmail SMTP class
    ```python
    import Qmail
    
    sender = Qmail.SMTP('parameters 👆')
    
    # To send
    sender.send_mail(message= 'Any Qmail MSG Class. (OTP, MSG, HTML_MSG)' )
    ```

2. Qmail Smtp class spammer
    ```python
    import Qmail
    
    sender = Qmail.SMTP('parameters 👆')
    
    # To Spam
    sender.spam_mail(message= 'Any Qmail MSG Class. (OTP, MSG, HTML_MSG)', num = 10 )
    # num= ammount of mails to send (Integer ONLY)
    ```
    

###
### Qmail Msg Class

##### Create Qmail MSG Class
####
1. import the Qmail library
    ```python
    import Qmail
    ```

2.  Create Qmail MSG Class

    ```python
    
    message = Qmail.MSG(\
        subject= 'Subject Of Email',
        txt= 'txt in the email',
        attachments=['file1', 'file2'] # Add Attachment Filepaths here 
    )
    
    ```
    
    #### Qmail MSG class Parameters In Detail👇
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### subject
    #####
    subject of the email goes here
    Strings Are Only Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### txt
    #####
    What you want to include in your email goes here
    Strings __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### attachments
    #####
    Put filenames here if you want to add them into the email.
   Strings __ONLY__ Accepted for 1 file, Lists __ONLY__ Accepted for mutiple
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### Once you create this you can add it to the send_mail and spam_mail functions.


###

### Qmail Html Msg Class
##### Create Qmail HTML MSG Class
####

1. import the Qmail library
    ```python
    import Qmail
    ```

2.  Create Qmail HTML_MSG Class

    ```python
    
    message = Qmail.HTML_MSG(\
        subject= 'Subject Of Email',
        html= '<h1>Enter Html Here</h1>',
        attachments=['file1', 'file2'] # Add Attachment Filepaths here 
    )
    
    ```
    
    #### Qmail HTML MSG class Parameters In Detail👇
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### subject
    #####
    the subject of the email goes here
    Strings Are Only Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### html
    #####
    Html goes here
    Strings __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### attachments
    #####
    Put filenames here if you want to add them to the email.
   Strings __ONLY__ Accepted for 1 file, Lists __ONLY__ Accepted for mutiple
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### Once you create this you can add it to the send_mail and spam_mail functions.

###
### Qmail Otp Services
##### Generate OTP
####

1. import the Qmail.OTP library
    ```python
    from Qmail import OTP
    ```

2.  generate OTP function

    ```python
    
    otp = OTP.generateOTP(lenght=4, type='numeric')
    # generateOTP returns OTP as string
    
    #### Types ####
    ## numeric
    # ex: 198745
    
    ## alphanumeric
    # ex: YRjliMZLx4 
    ```
    
    #### generateOTP() Parameters In Detail👇
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### lenght
    #####
    Lenght of OTP goes here
    Integers Are __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### type
    #####
    OTP type:  numeric or alphanumeric
    Strings __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
##### Create OTP MSG Class
####

1. import the Qmail.OTP library
    ```python
    from Qmail import OTP
    ```

2.  Create Qmail OTP_EMAIL Class

    ```python
    
    from Qmail import OTP
    
    one_time_password = OTP.generateOTP(lenght=10, type='alphanumeric')
    NAME = 'Qmail'
    themes_available = ['simple', 'default', 'modern']

    message = OTP.OTP_EMAIL(subject='OTP MAIl', otp=one_time_password, brand_name=NAME, theme='default')
    
    ```
    
    #### Qmail HTML MSG class Parameters In Detail👇
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### subject
    #####
    the subject of the email goes here
    Strings Are __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### otp
    #####
    OTP goes here
    Strings __ONLY__ Accepted
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### brand_name
    #####
    your companies name or project name goes here.
    Strings __ONLY__ Accepted 
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### theme
    #####
    choose one of the 3 themes
    default, simple, modern
    Strings __ONLY__ Accepted 
    ###### ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    
    ##### Once you create this you can add it to the send_mail and spam_mail functions.

###
## Authors

##### Akmal Riyas

## Modules Used
##### - email
##### - smtplib
##### - ssl
##### - random
##### - math
##### - Qmail

####
## Thanks For Using My Module
