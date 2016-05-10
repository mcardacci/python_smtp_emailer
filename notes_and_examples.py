# Pickle is for storing a serialized version of the OS dictionary

# rep=Report([],[],[],{})

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(levelname)-8s %(name)s:%(message)s')

# auth = file('auth.txt').read()
# api = LogMeInAPI(auth)


#------------API algorithm to grab proper report-----------
# Example will look like: {u'OPI040-POS2': {u'type': u'Windows 7 Professional', u'installDate': u'2012-02-22 16:38:00.000'}}
# host_ids=[]
# operating_systems=[]

# Grabs host ids, OSes, and install dates from lmi api interface
# for ident, data in api.system_report()["hosts"].items():
# 	host_ids.append(ident)
# 	operating_systems.append(data["operatingSystem"])

# machines_report={}

# for machine_name in api.hosts()["hosts"]:
# 	string_id=str(machine_name["id"])
# 	if string_id in host_ids:
# 		machines_report[machine_name["description"]]=operating_systems[host_ids.index(string_id)]

# 'machines_report' is the report we will use for comparison
# print machines_report


#------------------TESTING--------------------

#Compare old report to new report

# pickle.dump(machines_report, open('reports\master_report.txt', 'wb'))

# text_db_dict=pickle.load(open('reports\master_report.txt', 'rb'))


#----------------Writing to a file-------------

# Writes to a file in reports dir	
# f=open('reports\master_report.txt', 'w')
# f.write(str(machines_report))
# f.close()
