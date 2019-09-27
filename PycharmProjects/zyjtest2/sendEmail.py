import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class sendEmail():
    # ----------1.跟发件相关的参数------
    smtpserver = "smtp.163.com" # 发件服务器
    port = 0 # 端口
    sender = "zhaoyajingyhms@163.com" # 账号
    psw = "13502288210" # 密码
    # receiver =["463186855@qq.com","1505682177@qq.com","liugang17@126.com"] # 接收人
    receiver = ["liugang17@126.com", "zhaoyajingyhms@163.com"]
    # ----------2.编辑邮件的内容------
    # 读文件
    file_path = "C:\\Users\\TTT\\PycharmProjects\\zyjtest2\\report\\result.html"
    with open(file_path, "rb") as fp:
        mail_body = fp.read()
    msg = MIMEMultipart()
    msg["from"] = sender # 发件人
    msg["to"] =";".join(receiver) # 收件人
    msg["subject"] = "这是我的主题" # 主题
    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="test_report.html"'
    msg.attach(att)
    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver) # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw) # 登录
    smtp.sendmail(sender, receiver, msg.as_string()) # 发送
    smtp.quit()