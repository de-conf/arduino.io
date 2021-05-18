import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr,formataddr
import os
import time
from app.models import User

from_address = '201607070511@stumail.xsyu.edu.cn'
from_passwd = 'HMQfFtcn2mFD56d'
smtp_server = 'stumail.xsyu.edu.cn' # port 465

receive_mail =  User.query.all().pop().email   # 烟雾警报收件人
#test_mail = 'chenjiagen88@gmail.com'

def format_address(from_info):
    name, address = parseaddr(from_info)
    return formataddr((Header(name, 'utf-8').encode(), address))


def send_html(send_to_address):
    html_msg = MIMEMultipart()
    html_msg['From'] = format_address('机房室监控<%s>'%from_address)
    html_msg['To'] = format_address('Dear User<%s>'%send_to_address)
    html_msg['subject'] = Header('监控报警<%s>'%time.asctime(time.localtime(time.time())), 'utf-8').encode()

    html_msg.attach(MIMEText('<html><body><h1>!!!!!当前烟雾数值异常，可能发生火灾，请立即查看!!!!!</h1>' +
                            '</body></html>',
                             'html', 'utf-8'))
    send_server = smtplib.SMTP_SSL(smtp_server, 465)
    send_server.set_debuglevel(1)
    send_server.login(from_address, from_passwd)
    send_server.sendmail(from_address, [send_to_address], html_msg.as_string())
    send_server.quit()

def alm_bot():
    send_html(receive_mail)
