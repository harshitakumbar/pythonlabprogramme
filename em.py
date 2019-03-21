#sending a mail using python
import smtplib
s=smtplib.SMTP("smtp.gmail.com","587")
s.starttls()
sender="harshitarkumbar22@gmail.com"
receiver="hemaishanya123@gmail.com"
msg="hello how r u?"
s.login(sender,"supritrk")
s.sendmail(sender,receiver,msg)
print("msg sent sucessfully")
s.quit()