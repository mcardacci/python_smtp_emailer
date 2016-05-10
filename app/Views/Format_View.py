import sys

# This path insert is for testing the Formatter class, later this will be taken care of by 
sys.path.insert(0, 'C:\Users\marcoc\Desktop\projects\python\logmein_api_interface')

# from Models import *
# from Models import Report

class Format(object):

	def __init__(self,content):
		self.content=content

	def os_report(self):
		content=self.content
		if len(content) > 0: 	
			formatted_email="""

					   Newly Installed or Updated OS's by Machine Name\n
			   Machine             |                      OS                   |              Install Date
			"""

			for machine_name,os in content.items():
				os_and_date=os.values()
				formatted_email+= "\n                  "+machine_name+"           "+str(os_and_date[0])+"       "+str(os_and_date[1])
			return formatted_email
		else:
			return "No machines have been added, No Operating Systems have been changed."




#-------------------TESTING----------------------------
# rep=Report([],[],[],{})

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(levelname)-8s %(name)s:%(message)s')

# auth = file('auth.txt').read()
# api = LogMeInAPI(auth)

#-----------os_report TESTING---------------------------
# Real args for Format instantiation: rep.compare_reports(api.hosts(),api.system_report()
# f=Format(rep.compare_reports(api.hosts(),api.system_report()))
# print f.os_report()