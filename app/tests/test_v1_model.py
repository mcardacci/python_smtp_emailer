import unittest
import inspect
from time import sleep
from app import LogMeInAPI

class V1ModelMethods(unittest.TestCase):
	def setUp(self):
		self.auth=file('.auth.txt').read()
		self.api=LogMeInAPI(self.auth)
		self.header_keys=self.api.session.headers.keys()

	def tearDown(self):
		self.api=None
		self.auth=None
		self.header_keys=None

	def test_object_is_a_class(self):
		self.assertTrue(self.api, "OBJECT SHOULD NOT TRUE BUT IT'S NOT")
		self.assertEqual(inspect.isclass(LogMeInAPI), True, "OBJECT SHOULD HAVE TYPE 'class' instead has type "+str(type(self.api)))

	def test_object_attributes(self):
		api=self.api
		self.assertEqual(type(api.creds), dict, "LMI ATTR 'creds' SHOULD BE A 'dict' but equals"+str(type(api.creds)))
		self.assertNotEqual(type(api.creds), str, "LMI ATTR 'creds' SHOULD BE A 'dict' but equals"+str(type(api.creds)))

	def test_object_session_initialisation(self):
		keys=['Connection', 'Authorization', 'Accept-Encoding', 'Accept', 'User-Agent']
		api=self.api

		for k in keys:
			if k in self.header_keys:
				self.assertTrue(k)
			else:
				self.fail("SESSION HEADER KEYS DON'T MATCH. SHOULD BE THIS "+str(keys)+"INSTEAD IT'S THIS "+str(self.header_keys))

	# def test_hosts_method(self):
	# 	sleep(60)
	# 	hosts=lambda: self.api.hosts()
	# 	hosts_values=hosts()["hosts"][0].values()

	# 	self.assertEqual(type(hosts()), dict, "'hosts()' SHOULD HAVE RETURNED A DICTIONARY BUT INSTEAD RETURNED "+str(hosts()))
	# 	self.assertEqual(type(hosts()["hosts"]), list, "THE VALUE OF HOSTS SHOULD BE A LIST INSTEAD IT'S A "+str(hosts()["hosts"]))
	# 	self.assertEqual(hosts()["hosts"][0].keys(), ['description', 'id'], "THE KEYS OF THE FIRST DICT SHOULD BE 'description' and 'id', GOT "+str(hosts()["hosts"][0].keys()))
	# 	self.assertEqual(type(hosts_values[0]), unicode, "THE VALUE OF KEY u'description' SHOULD BE unicode, GOT: "+str(type(hosts_values[0])))
	# 	self.assertEqual(type(hosts_values[1]), int, "THE VALUE OF KEY u'description' SHOULD BE 'int', GOT: "+str(type(hosts_values[1])))

	# def test_system_report_method(self):
	# 	sleep(60)
	# 	sys_rep=self.api.system_report()
	# 	sample_host_id,sample_os=sys_rep["hosts"].popitem()

	# 	self.assertEqual(type(sys_rep), dict, "'system_report' METHOD SHOULD BE TYPE DICT, GOT"+str(type(sys_rep)))
	# 	self.assertGreater(int(sample_host_id), 1, "THE HOST ID IS NOT GREATER THAN 1, GOT: "+str(int(sample_host_id)))
	# 	self.assertEqual(sample_os["operatingSystem"].keys(), ['type', 'installDate'], "DOESN'T HAVE KEYS u'type' and u'installDate' IN DICT, GOT: "+str(sample_os["operatingSystem"].keys()))
	# 	self.assertIn("Windows" or None, sample_os["operatingSystem"].values()[0], "DOESN'T HAVE VALUE 'Windows' or None AS VALUE, GOT: "+str(sample_os["operatingSystem"].values()[0]))
		

if __name__=='__main__':
	unittest.main()

