from v1 import LogMeInAPI
import logging
import pickle
from os import system as sys_command

class Report(object):
	
	def __init__(self,host_ids,operating_systems,machine_names,machines_report):
		self.host_ids=host_ids
		self.operating_systems=operating_systems
		self.machine_names=machine_names
		self.machines_report=machines_report

	# api call to system_report in lmi interface
	def grab_OSes(self,api_call):
		for ident, data in api_call["hosts"].items():
			self.host_ids.append(ident)
			self.operating_systems.append(data["operatingSystem"])
		return self.host_ids, self.operating_systems

	# api call to hosts in lmi interface 
	def grab_machine_names(self,api_call):
		self.machine_names=api_call["hosts"]
		return self.machine_names
		
	# Formulates report from 'grab_OSes' and 'grab_machine_names'
	def get_new_report(self,machines_api_call,OSes_api_call):
		host_ids,operating_systems=self.grab_OSes(OSes_api_call)
		hosts=self.grab_machine_names(machines_api_call)

		for machine_name in hosts:
			string_id=str(machine_name["id"])
			if string_id in host_ids:
				self.machines_report[machine_name["description"]]=operating_systems[host_ids.index(string_id)]
		return self.machines_report

	# Cleans up pickled data, takes out carriage returns.
	def clean_data(self,dic):
		clean_dict={}
		for machine_name in dic:
			type_and_installdate={key.strip() : val.strip() if val!=None else val for key,val in dic[machine_name].items()}
			clean_dict[machine_name.strip()]=type_and_installdate
		return clean_dict
		
	def store_report(self,report):
		if len(report) > 0:
			# serializes and stores report
			pickle.dump(report, open('reports/master_report.txt', 'wb'))
			return report
		else:
			return "No machines have been added, no Operating Systems have been changed."

	# Compares master report to newly generated cron job report
	# Be careful with the file path here, linux-style works on MINGW64 but won't in CMD, it will also vary depending on where you call it.
	def compare_reports(self,machines_api_call,OSes_api_call):
		master_report=self.clean_data(pickle.load(open("reports/master_report.txt", 'rb')))
		new_report=self.get_new_report(machines_api_call, OSes_api_call)
		machines_to_be_mailed={}

		for machine_name,os in new_report.items():
			if machine_name not in master_report:
				machines_to_be_mailed[machine_name]=os
			elif master_report[machine_name] != os:
				machines_to_be_mailed[machine_name]=os
		return machines_to_be_mailed
