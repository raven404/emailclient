import smtplib
conn=smtplib.SMTP('smtp.gmail.com',587)
type(conn)
conn.ehlo()

emailId = input('Enter your email : ')
password = input('Enter enter your password : ')
receiver=input('Enter receivers email : ')
conn.starttls()
conn.login(emailId,password)

sub = input('Enter subject of mail : ')
body = input('Enter body of your mail : ')

conn.sendmail(emailId,receiver,sub,body)
conn.logout()




