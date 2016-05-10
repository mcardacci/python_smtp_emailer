import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Mailer(object):

	def __init__(self,subject,to_address,from_address,password):
		self.subject=subject
		self.to_address=to_address
		self.from_address=from_address
		self.password=password

	def format_content(self):
		pass

	def send(self,content):
		msg=MIMEMultipart()
		msg['From']=self.from_address
		msg['To']=self.to_address
		msg['Subject']=self.subject

		msg.attach(MIMEText(content,'plain'))

		mail=smtplib.SMTP("smtp.gmail.com",587)
		mail.ehlo() # this isn't in the example
		mail.starttls()
		mail.login(self.from_address,self.password)
		text=msg.as_string()
		mail.sendmail(self.from_address,self.to_address,text)
		mail.close()

#--------------------------TESTING----------------------------------------------------

# ttmailer=Mailer("Operating System Updates","marcoc@ticketech.com","ticketechtest@gmail.com",'locationswithpendingfiles')

# dic={u'hosts': [{u'description': u'MAURICIOC-TKTWIN7', u'id': 1009946249}, {u'description': u'MAURICIO-WIN7-HOME', u'id': 1010104408}, {u'description': u'MAM031-S', u'id': 1011902330}, {u'description': u'SPN200-S', u'id': 1012139205}]}

# ttmailer.send(dic)