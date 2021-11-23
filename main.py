import smtplib

my_email = "anirudhvasudevan11@gmail.com"
password = "SXXXXXXXXXXXXX"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="av4861@srmist.edu.in",msg="hey")
connection.close()