import unittest
import inspect
import pickle
import time
from app import OS_Report_Controller


class OSReportControllerMethods(unittest.TestCase):
	def setUp(self):
		self.os_rep_cont=OS_Report_Controller()


	def tearDown(self):
		self.os_report=None

	def test_lmi_auth_attribute(self):
		os_rep_cont=self.os_rep_cont
		self.assertIn("CID" and "PSK", os_rep_cont.lmi_auth, "DOESN'T HAVE 'CID' OR 'PSK' IN 'lmi_auth' ATTR, GOT "+str(os_rep_cont.lmi_auth))
		self.assertEqual(type(os_rep_cont.lmi_auth), str, "'lmi_auth' ATTR SHOULD BE A STRING, GOT "+str(type(os_rep_cont.lmi_auth)))

	def test_lmi_obj_attr_for_OS_report_controller(self):
		os_rep_cont=self.os_rep_cont
		self.assertTrue(inspect.isclass(type(os_rep_cont.lmi_obj)), "'lmi_obj' SHOULD BE AN INSTANCE OF A CLASS, GOT "+str(inspect.isclass(type(os_rep_cont.lmi_obj))))
		self.assertFalse(inspect.isclass(os_rep_cont.lmi_obj), "'lmi_obj' SHOULD NOT BE A CLASS, IT'S AN INSTANCE OF A CLASS SAVED TO A VARIABLE, GOT "+str(inspect.isclass(os_rep_cont.lmi_obj)))

	def test_report_obj_attr_for_OS_report_controller(self):
		os_rep_cont=self.os_rep_cont
		self.assertTrue(inspect.isclass(type(os_rep_cont.report_obj)), "'report_obj' SHOULD BE AN INSTANCE OF A CLASS, GOT "+str(inspect.isclass(type(os_rep_cont.report_obj))))
		self.assertFalse(inspect.isclass(os_rep_cont.report_obj), "'report_obj' SHOULD NOT BE A CLASS, IT'S AN INSTANCE OF A CLASS SAVED TO A VARIABLE, GOT "+str(inspect.isclass(os_rep_cont.report_obj)))

	def test_mailer_obj_attr_for_OS_report_controller(self):
		os_rep_cont=self.os_rep_cont
		self.assertTrue(inspect.isclass(type(os_rep_cont.mailer_obj)), "'mailer_obj' SHOULD BE AN INSTANCE OF A CLASS, GOT "+str(inspect.isclass(type(os_rep_cont.mailer_obj))))
		self.assertFalse(inspect.isclass(os_rep_cont.mailer_obj), "'mailer_obj' SHOULD NOT BE A CLASS, IT'S AN INSTANCE OF A CLASS SAVED TO A VARIABLE, GOT "+str(inspect.isclass(os_rep_cont.mailer_obj)))

	def test_clean_data_method(self):
		os_rep_cont=self.os_rep_cont
		clean_data=os_rep_cont.clean_data()
		os_tuple=clean_data.iteritems().next()

		self.assertNotIn("\r" and "\n", os_tuple[0], "'clean_data' SHOULD RETURN NO CARRIAGE RETURNS OR NEW LINES, GOT "+str(os_tuple[0]))
	
	# def test_compare_reports_method(self):
	# 	time.sleep(60)
	# 	os_rep_cont=self.os_rep_cont
	# 	machines_to_be_mailed,new_report=os_rep_cont.compare_reports()

	# 	self.assertEqual(len(os_rep_cont.compare_reports()), 2, "COMPARE REPORTS METHOD DOES NOT RETURN 2 OBJECTS, GOT"+str(len(os_rep_cont.compare_reports())))
	# 	self.assertEqual(type(machines_to_be_mailed), dict, "'compare_reports()' DID NOT RETURN A DICTIONARY FOR IT'S FIRST TUPLE INDEX, GOT "+str(type(machines_to_be_mailed)))
	# 	self.assertEqual(type(new_report), dict, "'compare_reports()' DID NOT RETURN A DICTIONARY FOR IT'S SECOND TUPLE INDEX, GOT "+str(type(machines_to_be_mailed)))

	# def test_store_report_method(self):
	# 	time.sleep(60)
	# 	os_rep_cont=self.os_rep_cont
	# 	machines_to_be_mailed,new_report=os_rep_cont.compare_reports()
	# 	store_report=os_rep_cont.store_report(machines_to_be_mailed, new_report)

	# 	self.assertEqual(store_report, machines_to_be_mailed, "'store_report' DID NOT RETURN MACHINES TO BE MAILED, NEEDED FOR THE 'mailer_obj', GOT "+str(machines_to_be_mailed))
	# 	self.assertEqual(type(store_report), dict, "'store_report()' DID NOT RETURN A DICTIONARY, GOT "+str(type(store_report)))


if __name__=='__main__':
	unittest.main()