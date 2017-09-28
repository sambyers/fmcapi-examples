# fmcapi-examples
Example Scripts using the [fmcapi](https://github.com/daxm/fmcapi)

## rmv_objects
rmv_objects removes objects from the FMC with the fmcapi library. You can specify the type of object you want to remove and a regular expression to match on object names you want to delete. This script will not delete objects that are in use.

- Install [python](python.org)
- Install [git](https://git-scm.com/downloads)
- git clone https://github.com/sambyers/fmcapi-examples
- pip install -r requirements.txt
- python rmv_objects.py server username password object_type regex

### Usage

python rmv_objects.py -h
usage: rmv_objects.py [-h] server username password object_type regex

Get arguments for rmv_objects script.

positional arguments:  
  _server_       IP or DNS of the FMC Server  
  _username_     Username for FMC.  
  _password_     Password for FMC.  
  _object_type_  Object type to remove. protocolport, ipnetwork, networkgroup are supported
               today.  
  _regex_        The regular expression to match objects to remove. Use double
               quotes around the pattern.  
