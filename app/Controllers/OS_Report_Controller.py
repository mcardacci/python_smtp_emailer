import sys, os
import time

# Appends abs path to this project folder to Python's system path at runtime
sys.path.append(os.path.abspath(os.path.join('..','logmein_api_interface','app')))

from Models import *
from Views import *

class OS_Report_Controller(object):

	def __init__(self,lmi_auth=None,lmi_obj=None,report_obj=None,mailer_obj=None,format_obj=None):
		self.lmi_auth=file('.auth.txt').read() if lmi_auth is None else lmi_auth
		self.lmi_obj=LogMeInAPI(self.lmi_auth) if lmi_obj is None else lmi_obj
		self.report_obj=Report([],[],[],{}) if report_obj is None else report_obj		
		self.time_stamped_string="Master_Report_"+time.strftime("%Y%m%d_%H%M%S")+".txt"
		if mailer_obj is None:
			self.mailer_obj=Mailer(
				"Operating System Updates",
				"Email To Address",
				"Email From Address",
				"Password to 'To Address' account"
				) 
		else:
			self.mailer_obj=mailer_obj

	# Cleans up pickled data, takes out carriage returns.
	def clean_data(self):
		clean_dict={}
		dir_list=os.listdir("reports")
		dirty_dict=pickle.load(open("reports/"+dir_list[-1], 'rb'))

		for machine_name in dirty_dict:
			# else conditional is necessary bc you can't strip a 'None' type
			type_and_installdate={key.strip() : val.strip() if val!=None else val for key,val in dirty_dict[machine_name].items()}
			clean_dict[machine_name.strip()]=type_and_installdate
		return clean_dict

	# Compares master report to newly generated cron job report
	def compare_reports(self):
		rep=self.report_obj
		lmi=self.lmi_obj
		master_report=self.clean_data()
		new_report=rep.get_new_report(lmi.hosts(), lmi.system_report())
		machines_to_be_mailed={}

		for machine_name,os in new_report.items():
			if machine_name not in master_report:
				machines_to_be_mailed[machine_name]=os
			elif master_report[machine_name] != os:
				machines_to_be_mailed[machine_name]=os
		return machines_to_be_mailed,new_report

	# Pickle dump is commented out bc we need test data
	def store_report(self,machines_to_be_mailed,new_report):
		if len(machines_to_be_mailed) > 0:
			# serializes and stores report
			pickle.dump(new_report, open("reports/"+self.time_stamped_string, 'wb'))
			return machines_to_be_mailed

	def run(self):
		# Grab 2 dictionaries
		machines_to_be_mailed,new_report=self.compare_reports()
		# init Mailer
		mailer=self.mailer_obj
		# Serialize new report if machines_to_be_mailed is populated
		self.store_report(machines_to_be_mailed,new_report)
		# init Format (change new_report to machines_to_be_mailed below for intended use)
		formatter=Format(new_report)
		# Make dict pretty for email
		os_report=formatter.os_report()
		# Mailer object sends os report
		return mailer.send(os_report)
