PubsWarehouse_UI
================

To get this application running using the flask local dev server, there are three steps:

1. Create a virtualenv using python 2.7.9 and install the requirements in 'requirements.txt'. This can be done as follows while in the project directory:
  1. Run `virtualenv --python=python2.7 env`
  2. Activate your virtualenv (depends on whether linux or windows)
  3. Run `pip install -r requirements.txt`
 
2. Create a  `local_settings.py` file under PubsWarehouse_UI folder, and add this file to .gitignore.  The contents of the files should looks like so:

 ```python
 SECRET_KEY = 'the_secret_key'
 DEBUG = True #you want debug to be true for development, but not production

 # URL for getting publication information
 PUB_URL = "[server of choice]/pubs-services/"
 # URL for getting lookup information- authors, contributing offices, etc
 LOOKUP_URL = "[server of choice]/pubs-services/lookup/"
 # URL for endpoint to get supersede info
 SUPERSEDES_URL = "[server of choice]/service/citation/json/extras?"
 # URL for Browse
 BROWSE_URL = "[server of choice]/browse/"
 # URL for Search
 BASE_SEARCH_URL = "[server of choice]/pubs-services/publication"
 # URL to instert into JSON-LD output- use the local address for local development
 JSON_LD_ID_BASE_URL = 'http://127.0.0.1:5050/'
 # replacement of relative links in the browse interface
 BROWSE_REPLACE = "browse"
 # Code for Google analytics- insert appropriate code for dev or prod
 GOOGLE_ANALYTICS_CODE = 'GA-CODE-STRING'
 # Code for webmaster tools- needed on prod only
 GOOGLE_WEBMASTER_TOOLS_CODE = 'googlerandomstring'
 # set variable for if robots are welcome to index the site or not 
 ROBOTS_WELCOME = False
 # If logging is turned on or not
 LOGGING_ON = False
 # A string to put into the announcements block on the homepage- can contain html
 ANNOUNCEMENT_BLOCK = ""
 # The endpoint to get an authorization token based on AD credentials
 AUTH_ENDPOINT_URL = '[server of choice]/pubs-services/auth/'
 # The endpoint to get a preview of a pub that is only in mypubs
 PREVIEW_ENDPOINT_URL = '[server of choice]/pubs-services/mppublications/'
 # set the default path for the login page- for local development, it is '/login/'
 LOGIN_PAGE_PATH = '/login/'
 # verify ssl certificate for outside service calls
 VERIFY_CERT = True or False

 ```

3. After you have created your `local_settings.py`, you can start the app by running `runserver.py`, which will give you an output like so:

 ```python
 * Running on http://127.0.0.1:5050/
 * Restarting with reloader
 ```

---

If you want to generate a real secret key, you can do so trivially from the Python console by using `os.urandom()` like so:

```python
>>> import os
>>> os.urandom(24)
'\xa1\x89D\x9e+\xb4Pl\xbfr\xa5\xc3\xc1\x05\x9c\x90\x91\x10\xa8\xfa\x10\xe7r\x9e'

```
You can paste the generated string right into your SECRET_KEY global constant