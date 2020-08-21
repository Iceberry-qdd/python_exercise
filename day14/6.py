from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    sender = 'qddwork@outlook.com'
    recrivers = ['2783243257@qq.com']
    message = MIMEText('用Python发送邮件的示例代码.', 'plain', 'utf-8')
    message['From'] = Header('Iceberry', 'utf-8')
    #message['To'] = Header('qdd', 'utf-8')
    message['subject'] = Header('示例代码实验邮件', 'utf-8')
    smtper = SMTP('smtp.office365.com')
    smtper.connect('smtp.office365.com', 587)
    smtper.ehlo()
    smtper.starttls()
    smtper.login(sender, 'bbs836525')
    smtper.sendmail(sender, recrivers, message.as_string())
    print('邮件发送完成！')


if __name__ == "__main__":
    main()
