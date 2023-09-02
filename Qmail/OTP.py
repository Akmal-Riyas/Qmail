import ssl
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
import random
import math

class NoOtpGivenError(Exception):
    """Exception raised when no otp is given.

    Attributes:
        otp -- the value that was not given
        message -- explanation of the error
    """

    def __init__(self, otp, message="No otp was given when creating an OTP_EMAIL class."):
        self.otp = otp
        self.message = message
        super().__init__(self.message)

class OTP_EMAIL:
    def __init__(self,subject = 'Otp Email', brand_name = 'title', otp = None, theme = 'default'):
        self.creator = 'Akmal Riyas'
        
        if otp == None:
            raise NoOtpGivenError(otp)
        
        self.text = MIMEMultipart("alternative")
        self.text["Subject"] = subject

        if theme == 'default':
            self.text.attach(MIMEText(self.default_theme(otp=otp, brand=brand_name), "html"))
        
        if theme == 'simple':
            self.text.attach(MIMEText(self.simple_theme(otp=otp, brand=brand_name), "html"))
        
        if theme == 'modern':
            self.text.attach(MIMEText(self.modern(otp=otp, brand=brand_name), "html"))
    

    def default_theme(self, otp, brand):
        theme = f"""
        <div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
            <div style="margin:50px auto;width:70%;padding:20px 0">
                <div style="border-bottom:1px solid #eee">
                    <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">{brand}</a>
                </div>
                    <p style="font-size:1.1em">Hi,</p>
                    <p>Thank you for choosing {brand}. Use the following OTP to complete your procedures. OTP is valid for 2 minutes</p>
                    <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{otp}</h2>
                    <p style="font-size:0.9em;">Regards,<br />{brand}</p>
                    <hr style="border:none;border-top:1px solid #eee" />
                <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
                    <p>{brand}</p>
                    <p>created by easymail</p>
                    
                </div>
            </div>
        </div>"""

        return theme
    
    def simple_theme(self, otp, brand):
        theme = """<!doctype html>
        <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">

        <head>
        <title>
        </title>
        <!--[if !mso]><!-->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!--<![endif]-->
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style type="text/css">
            #outlook a (
            padding: 0;
            )

            body (
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
            )

            table,
            td (
            border-collapse: collapse;
            mso-table-lspace: 0pt;
            mso-table-rspace: 0pt;
            )

            img (
            border: 0;
            height: auto;
            line-height: 100%;
            outline: none;
            text-decoration: none;
            -ms-interpolation-mode: bicubic;
            )

            p (
            display: block;
            margin: 13px 0;
            )
        </style>
        <!--[if mso]>
                <noscript>
                <xml>
                <o:OfficeDocumentSettings>
                <o:AllowPNG/>
                <o:PixelsPerInch>96</o:PixelsPerInch>
                </o:OfficeDocumentSettings>
                </xml>
                </noscript>
                <![endif]-->
        <!--[if lte mso 11]>
                <style type="text/css">
                .mj-outlook-group-fix ( width:100% !important; )
                </style>
                <![endif]-->
        <!--[if !mso]><!-->
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,500,700" rel="stylesheet" type="text/css">
        <style type="text/css">
            @import url(https://fonts.googleapis.com/css?family=Open+Sans:300,400,500,700);
        </style>
        <!--<![endif]-->
        <style type="text/css">
            @media only screen and (min-width:480px) ()
            .mj-column-per-100 ()
                width: 100% !important;
                max-width: 100%;
            )
            )
        </style>
        <style media="screen and (min-width:480px)">
            .moz-text-html .mj-column-per-100 (
            width: 100% !important;
            max-width: 100%;
            )
        </style>
        <style type="text/css">
        </style>
        </head>

        <body style="word-spacing:normal;background-color:#fafbfc;">
        <div style="background-color:#fafbfc;">
            <!--[if mso | IE]><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
            <div style="margin:0px auto;max-width:600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;">
                <tbody>
                <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:20px;padding-top:20px;text-align:center;">
                    <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:middle;width:600px;" ><![endif]-->
                    <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">
                        <tbody>
                            <tr>
                            <td align="center" style="font-size:0px;padding:25px;word-break:break-word;">
                                <div style="font-family:open Sans Helvetica, Arial, sans-serif;font-size:30px;font-style:normal;line-height:1;text-align:center;color:#000000;">{Brand}</div>
                            </td>
                            </tr>
                        </tbody>
                        </table>
                    </div>
                    <!--[if mso | IE]></td></tr></table><![endif]-->
                    </td>
                </tr>
                </tbody>
            </table>
            </div>
            <!--[if mso | IE]></td></tr></table><table align="center" border="0" cellpadding="0" cellspacing="0" class="" style="width:600px;" width="600" bgcolor="#ffffff" ><tr><td style="line-height:0px;font-size:0px;mso-line-height-rule:exactly;"><![endif]-->
            <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px;">
            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="background:#ffffff;background-color:#ffffff;width:100%;">
                <tbody>
                <tr>
                    <td style="direction:ltr;font-size:0px;padding:20px 0;padding-bottom:20px;padding-top:20px;text-align:center;">
                    <!--[if mso | IE]><table role="presentation" border="0" cellpadding="0" cellspacing="0"><tr><td class="" style="vertical-align:middle;width:600px;" ><![endif]-->
                    <div class="mj-column-per-100 mj-outlook-group-fix" style="font-size:0px;text-align:left;direction:ltr;display:inline-block;vertical-align:middle;width:100%;">
                        <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="vertical-align:middle;" width="100%">
                        <tbody>
                            <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-right:25px;padding-left:25px;word-break:break-word;">
                                <div style="font-family:open Sans Helvetica, Arial, sans-serif;font-size:16px;line-height:1;text-align:center;color:#000000;"><span>Hello,</span></div>
                            </td>
                            </tr>
                            <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-right:25px;padding-left:25px;word-break:break-word;">
                                <div style="font-family:open Sans Helvetica, Arial, sans-serif;font-size:16px;line-height:1;text-align:center;color:#000000;">Heres your one time password:</div>
                            </td>
                            </tr>
                            <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;">
                                <div style="font-family:open Sans Helvetica, Arial, sans-serif;font-size:24px;font-weight:bold;line-height:1;text-align:center;color:#000000;">{OTP}</div>
                            </td>
                            </tr>
                            <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-right:16px;padding-left:25px;word-break:break-word;">
                                <div style="font-family:open Sans Helvetica, Arial, sans-serif;font-size:16px;line-height:1;text-align:center;color:#000000;">If you didn't request this, you can ignore this email or let us know.</div>
                            </td>
                            </tr>
                            <tr>
                            <td align="center" style="font-size:0px;padding:10px 25px;padding-right:25px;padding-left:25px;word-break:break-word;">
                                <div style="font-family:open Sans Helvetica, Arial, sans-serif;font-size:16px;line-height:1;text-align:center;color:#000000;">Thanks! <br />{Brand} team</div>
                            </td>
                            </tr>
                        </tbody>
                        </table>
                    </div>
                    <!--[if mso | IE]></td></tr></table><![endif]-->
                    </td>
                </tr>
                </tbody>
            </table>
            </div>
            <!--[if mso | IE]></td></tr></table><![endif]-->
        </div>
        </body>

        </html>
        """.format(Brand= brand, OTP = otp)

        return theme
    
    def modern(self, otp, brand):
        theme = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>OTP</title>
  <!--[if mso]><style type="text/css">body, table, td, a ( font-family: Arial, Helvetica, sans-serif !important; )</style><![endif]-->
</head>

<body style="font-family: Helvetica, Arial, sans-serif; margin: 0px; padding: 0px; background-color: #ffffff;">
  <table role="presentation"
    style="width: 100%; border-collapse: collapse; border: 0px; border-spacing: 0px; font-family: Arial, Helvetica, sans-serif; background-color: rgb(239, 239, 239);">
    <tbody>
      <tr>
        <td align="center" style="padding: 1rem 2rem; vertical-align: top; width: 100%;">
          <table role="presentation" style="max-width: 600px; border-collapse: collapse; border: 0px; border-spacing: 0px; text-align: left;">
            <tbody>
              <tr>
                <td style="padding: 40px 0px 0px;">
                  <div style="text-align: left;">
                    <div style="padding-bottom: 20px;">
                        <h1>
                            {Brand}
                        </h1>
                    </div>
                  </div>
                  <div style="padding: 20px; background-color: rgb(255, 255, 255);">
                    <div style="color: rgb(0, 0, 0); text-align: left;">
                      <h1 style="margin: 1rem 0">Verification code</h1>
                      <p style="padding-bottom: 16px">Please use the OTP below</p>
                      <p style="padding-bottom: 16px"><strong style="font-size: 130%">{OTP}</strong></p>
                      <p style="padding-bottom: 16px">If you didn’t request this, you can ignore this email.</p>
                      <p style="padding-bottom: 16px">Thanks,<br>The {Brand} team</p>
                    </div>
                  </div>
                  <div style="padding-top: 20px; color: rgb(153, 153, 153); text-align: center;">
                    <p style="padding-bottom: 16px">Made by {Brand} using easymail</p>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</body>

</html>

""".format(Brand = brand, OTP= otp)

        return theme



def generateOTP(lenght=4, type = 'numeric') :
        if lenght < 4:
            print('Atleast 4 characters is recommended for an OTP')

        if type == 'numeric':
            digits = "0123456789"
            OTP = ""

            for i in range(lenght) :
                OTP += digits[math.floor(random.random() * 10)]
    
            return OTP
        
        elif type == 'alphanumeric':
            string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            OTP = ""
            length = len(string)
            for i in range(lenght) :
                OTP += string[math.floor(random.random() * length)]
        
            return OTP