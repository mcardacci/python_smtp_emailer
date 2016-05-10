import unittest
from app import Format

class FormatViewMethods(unittest.TestCase):

	def setUp(self):
		self.formatter=Format({u'ABC084-S': {u'type': u'Windows 7 Professional', u'installDate': u'2011-08-31 11:07:00.000'}, u'GMC088-POS1': {u'type': u'Windows 7 Professional', u'installDate': u'2011-08-31 11:07:00.000'}})
	
	def tearDown(self):
		self.formatter=None

	def test_object_has_content_named_attribute(self):
		self.assertEqual(hasattr(self.formatter, 'content'), True, 'CONTENT FIELD EXISTS')

	def test_object_content_is_a_dictionary(self):
		self.assertEqual(type(self.formatter.content), dict, 'CONTENT IS NOT A DICTIONARY')

	def test_os_report_function_responds_correctly_when_content_is_empty(self):
		self.formatter.content={}
		self.assertEqual(self.formatter.os_report(), "No machines have been added, No Operating Systems have been changed.", "DIDN'T RESPOND WITH WARNING STRING.")

	def test_os_report_function_responds_correctly_when_content_is_populated(self):
		os_report=self.formatter.os_report()
		self.assertEqual(type(os_report), unicode, "DIDN'T RESPOND WITH CORRECT TYPE (str)")
		self.assertIsNot(os_report, "No machines have been added, No Operating Systems have been changed.", "DIDN'T RESPOND WITH CORRECT STRING.")



if __name__=='__main__':
	unittest.main()