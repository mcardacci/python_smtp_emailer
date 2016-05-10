# Logmein API Interface
---
This is a python interface for version 1 of the Logmein API
* This application requires at least Python 2.7.11

## How to pass credentials
---
#### Option 1: Pass credentials as a dictionary.
```python
auth = {'companyId': <int>(company_id), 'psk': <string>(passkey)}
api = LogMeInAPI(auth)
```

#### Option 2: Pass the content of the credentials file provided by LogMeIn.
```python
auth = file('auth.txt').read()
api = LogMeInAPI(auth)
```

#### Option 3: Pass in the credentials file name directly.
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

## How to Run Tests
---
Navigate to the root directory and leverage python's 'discover' feature while in the command line.
```
$ python -m unittest discover -v
``` 
It should run the tests automatically.

