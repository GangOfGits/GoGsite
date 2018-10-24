# notjoshno
A 'lil website for Gang of Gits

## Notes for developers

> GoGsite is a continued development of my personal webapp. The server it is hosted on relies on certain filenames. Please do not rename any file named 'notjoshno'. Even if you think you've changed it everywhere, you haven't. Thanks <3

Joshua

### Modules
* *** wsgi.py is used to host the webapp on notjoshno.co.uk. Please do not change or rename this file. ***
* approutes.py is for handling any url routing e.g. /app/namegenerator
* errorhandlers.py is for handling any error codes e.g. 404
* databaser.py is the module used for anything involving the SQL Server ** excluding queries ** e.g. connecting to a database
* web_pages.py is for handling any web page rendering, formatting, etc.