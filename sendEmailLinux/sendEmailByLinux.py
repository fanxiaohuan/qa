#!/usr/bin/python
# -*- coding: utf-8 -*-
import smtplib
# import datetime
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from getResult import runReport


def sendmail(mail_title, receiver, sender, username, password):
    # 读取html文件内容
    # HTML文件默认和当前文件在同一路径下，若不在同一路径下，需要指定要发送的HTML文件的路径
    f = open(r"/data/jenkins/workspace/epjs-jmeter/epjsReport.html", 'rb')
    mail_body = f.read()
    f.close()
    # 构造附件，传送当前目录下的 详细测试报告 文件
    attachment = MIMEApplication(
        open(r'/data/jenkins/workspace/epjs-jmeter/epjsReport_detail.html',
             'rb').read())
    #重命名文件
    attachment.add_header('Content-Disposition',
                          'attachment',
                          filename='epjsReport_detail.html')
    # 邮件内容, 格式, 编码
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')
    message.attach(attachment)
    message.attach(MIMEText(mail_body, 'html', 'utf-8'))
    try:
        # 所使用的用来发送邮件的SMTP服务器
        smtp = smtplib.SMTP_SSL("smtp.qiye.aliyun.com", 465)
        smtp.connect('smtp.qiye.aliyun.com')
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("发送邮件失败！！！")
    return ()


if __name__ == '__main__':
    # 发件人和收件人
    sender = 'fanxiaohuan@yinongt.com'
    receiver = 'epjs-api@yinongt.com'
    # 发送邮箱的用户名和密码
    username = 'fanxiaohuan@yinongt.com'
    password = 'fanxhYNT1'
    # 获取接口用例执行是否存在失败用例
    result = str
    getRunResult = runReport(result)
    # 邮件主题
    mail_title = 'e浦橘社-接口测试报告: ' + getRunResult
    sendmail(mail_title, receiver, sender, username, password)
