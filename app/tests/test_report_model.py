import unittest
from app import Report

class ReportModelMethods(unittest.TestCase):
	def setUp(self):
		self.report=Report([],[],[],{})
		self.system_report_mock={'hosts': {u'1012604211': {u'operatingSystem': {u'type': u'Windows XP Professional', u'installDate': u'2008-07-22 07:51:00.000'}}, u'1012439145': {u'operatingSystem': {u'type': u'Windows 7 Professional', u'installDate': u'2008-06-26 14:23:00.000'}}}}
		self.hosts_report_mock={u'hosts': [{u'description': u'MLH888-POS1', u'id': 1012439145}, {u'description': u'SEL005-S', u'id': 1012604211}]}
	
	def tearDown(self):
		self.report=None
		self.system_report_mock=None
		self.hosts_report_mock=None

	def test_model_has_attr_host_ids(self):
		self.assertEqual(self.report.host_ids, [], "DOESN'T HAVE ARRAY AS DATA STRUCTURE")

	def test_model_has_attr_operating_systems(self):
		self.assertEqual(self.report.operating_systems, [], "DOESN'T HAVE ARRAY AS DATA STRUCTURE")

	def test_model_has_attr_machine_names(self):
		self.assertEqual(self.report.machine_names, [], "DOESN'T HAVE ARRAY AS DATA STRUCTURE")

	def test_model_has_attr_machines_report(self):
		self.assertEqual(self.report.machines_report, {}, "DOESN'T HAVE DICT AS DATA STRUCTURE")

	def test_grab_OSes_method(self):
		rep=self.report
		grab_OSes=rep.grab_OSes(self.system_report_mock)
		first_id_in_tuple=grab_OSes[0][0]
		first_os_in_tuple=grab_OSes[1][0]
		second_os_in_tuple=grab_OSes[1][1]

		self.assertEqual(type(grab_OSes), tuple, "'grab_OSes' SHOULD RETURN A TUPLE")
		self.assertEqual(len(grab_OSes), 2, "'grab_OSes' DOESN'T RETURN WITH A LENGTH OF 2")
		self.assertEqual(self.system_report_mock['hosts'][first_id_in_tuple]['operatingSystem'], first_os_in_tuple, "ID AND OS DON'T CORRESPOND IN THE TUPLE RETURNED FROM 'grab_os' METHOD")
		self.assertEqual(second_os_in_tuple.keys(), ['type','installDate'], "DOESN'T RETURN AN ARRAY WITH 'type' AND 'installDate' KEYS")

	def test_grab_machine_names_method(self):
		rep=self.report
		grab_machine_names=rep.grab_machine_names(self.hosts_report_mock)

		self.assertEqual(type(grab_machine_names), list, "'grab_machine_names' METHOD DOESN'T HAVE CORRECT DATA STRUCTURE")
		self.assertEqual(len(grab_machine_names), 2, "'grab_machine_names' METHOD DOESN'T HAVE CORRECT LENGTH (2)")
		self.assertEqual(grab_machine_names[0]['description'], u'MLH888-POS1', "'grab_machine_names' METHOD DOESN'T HAVE CORRECT DESCRIPTION VALUE")
		self.assertEqual(grab_machine_names[0]['id'], 1012439145, "'grab_machine_names' METHOD DOESN'T HAVE CORRECT ID VALUE")

	def test_get_new_report(self):
		rep=self.report
		get_new_report= rep.get_new_report(self.hosts_report_mock, self.system_report_mock)
		self.assertEqual(type(get_new_report), dict, "'get_new_report' DOES NOT RETURN A DICTIONARY")
		self.assertEqual(len(get_new_report), 2, "'get_new_report' DOES NOT RETURN THE CORRECT LENGTH OF THE REPORT")
		self.assertEqual(get_new_report['SEL005-S']['type'], 'Windows XP Professional', "'get_new_report' HAS A LOGIC ISSUE PAIRING THE OS TO THE MACHINE NAME")

	




if __name__=='__main__':
	unittest.main()	


















