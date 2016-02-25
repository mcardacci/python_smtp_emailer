import smtplib

content="example email stuff"
mail=smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login('youremail@gmail.com', 'yourpassword')
mail.sendmail("youremail@gmail.com","to-email@anything.com", content)
mail.close()