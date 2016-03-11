import smtplib

def send(report):
	content=report
	mail=smtplib.SMTP("smtp.gmail.com", 587)
	mail.ehlo()
	mail.starttls()
	mail.login('ticketechtest@gmail.com', 'locationswithpendingfiles')
	mail.sendmail("ticketechtest@gmail.com","ticketechtest@gmail.com", content)
	mail.close()

