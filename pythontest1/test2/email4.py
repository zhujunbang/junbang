# coding=utf-8
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))


# 输入Email地址和口令:
from_addr = "562014704@qq.com"
password = "rqgibakwsvdsbchg"
# 输入SMTP服务器地址:
smtp_server = "smtp.qq.com"
# 输入收件人地址:
to_addr = "junbang@summba.com"

# 邮件对象:
msg = MIMEMultipart('alternative')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))
# 正常发送msg对象...

server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
