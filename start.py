#!/usr/bin/env python

# Python
import logging
import sys

# LogMeIn API
from lmiapi_interface import LogMeInAPI

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)-8s %(name)s:%(message)s')

# Option 1: Pass credentials as a dictionary.
# auth = {'companyId': 1009656696, 'psk': '01_z5hzknjtn5j7xo4bk52m31zhjreighedsznks7niiva0y7uhlqwg8yk2a4pfypoedwbio8ahlkdlw92gu2eyir8iizh9jccwssgqlb1wkgpqyrgylj5y4b31l2dlv'}
# api = LogMeInAPI(auth)

# Option 2: Pass the content of the credentials file provided by LogMeIn.
auth = file('auth.txt').read()
api = LogMeInAPI(auth)

# Option 3: Pass in the credentials file name directly.
# api = LogMeInAPI('auth.txt')

# Check that credentials work to authenticate.
# print api.authentication()

# Get host ID/description for all hosts.
print api.hosts()

# Get list of hardware report fields.
# print api.hardware_fields()

# Get list of system report fields.
# print api.system_fields()

# Get or create a hardware report (default to all fields, all hosts).
# print api.hardware_report()

# Get or create a system report (default to all fields, all hosts).
# print api.system_report()
