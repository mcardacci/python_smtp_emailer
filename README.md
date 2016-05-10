# Mailer Report Tool
---
The application leverages the Logmein API and Python's Mailer library.

## Purpose and Dependencies
---
* The purpose of this project was to learn Python and build a tool that allows my company to track their hardware across the vast net of their machines nationwide.
* They use this data to ensure accounting and security information is up to date.
* This application requires:
  ** Python 2.7.11
  ** Logmein credentials
## How to Run Tests
---
Navigate to the root directory and leverage python's 'discover' feature while in the command line.
```
$ python -m unittest discover -v
``` 
It should run the tests automatically.

## How to pass credentials
---
#### Option 1: Pass credentials as a dictionary.
```python
auth = {'companyId': <int>(company_id), 'psk': <string>(passkey)}
api = LogMeInAPI(auth)
```

#### Option 2: Create a text file called 'auth.txt' and pass in the credentials file name directly. The text file should read:
```
CID:  "ID without quotes"
PSK:  "Passkey without quotes"
```
Then in start.py:
```python
api = LogMeInAPI('auth.txt')
```
## How to check credentials
---
Check that credentials work to authenticate.
```python
print api.authentication()
```

## Example API Interface calls
---
#### Get host ID/description for all hosts:
```python
print api.hosts()
```

#### Get list of hardware report fields:
```python
print api.hardware_fields()
```

#### Get list of system report fields:
```python
print api.system_fields()
```

#### Get or create a hardware report (default to all fields, all hosts):
```python
print api.hardware_report()
```

#### Get or create a system report (default to all fields, all hosts):
```python
print api.system_report()
```


