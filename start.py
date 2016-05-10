#!/usr/bin/env python

# Python
import logging
import sys
import pickle

# LogMeIn API
from app import *


logging.basicConfig(level=logging.DEBUG,
	format='%(levelname)-8s %(name)s:%(message)s')

os_report=OS_Report_Controller()
os_report.run()
