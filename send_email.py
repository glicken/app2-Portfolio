import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "glicken@gmail.com"
password = "wxvzcllfjfgccxyf"

receiver = "glicken@gmail.com"

context = ssl.create_default_context()

message = '''\
subject: Thank you for your request
hello there'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)