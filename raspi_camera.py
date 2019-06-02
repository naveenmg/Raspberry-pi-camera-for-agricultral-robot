Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import smtplib,ssl
from picamera import PiCamera  
from time import sleep  
from email.mime.multipart import MIMEMultipart  
from email.mime.base import MIMEBase  
from email.mime.text import MIMEText  
from email.utils import formatdate  
from email import encoders  
camera=PiCamera()
camera.start_preview()
image=1
sleep(3)
camera.capture('/home/pi/animation/image%03d.jpg'%image)
camera.stop_preview()
def send_an_email():  
    toaddr = 'naveenmathewgeorge@gmail.com'      
    me = 'raspiprojekt94@gmail.com'          
    subject = "Forschungsprojekt"              
    path='/home/pi/animation/image001.jpg'
    msg = MIMEMultipart()  
    msg['Subject'] = subject  
    msg['From'] = me  
    msg['To'] = toaddr  
    msg.preamble = "test "  
    part = MIMEBase('application', "octet-stream")  
    part.set_payload(open(path, "rb").read())  
    encoders.encode_base64(part)  
    part.add_header('Content-Disposition', 'attachment; filename=image') 
    msg.attach(part)   
    s = smtplib.SMTP('smtp.gmail.com', 587)  
    s.ehlo()  
    s.starttls()  
    s.ehlo()  
    s.login(user = 'raspiprojekt94@gmail.com', password = 'forraspberry')  
    s.sendmail(me, toaddr, msg.as_string())  
    s.quit()
send_an_email()
