Freezer User's Guide
==========================

Introduction
------------
The Freezer API is an API used to retrieve data from the freezer system manager. TO use it,
the database server must be active. You can set a database by running an Xampp server and loading
the database on it. An sample of the database has been extracted and can be found `root_folder/database/freezer.sql`
If Xampp is used as server and is installed at `opt/lampp`. The script `run_server.sh` can be run as root to activate the server.

When the database is set and is active. The REST API server can be run.
To run this server the bash script file `flask_run.sh` must be run with the database name as parameter.
In our case it will be `freezer`.

Installation
------------
To use the API no installation of specific tools are required.
It can be used with `curl` request, for instance.

Commands
--------
A couple of commands can be used. These commands are explained in the `requests` section.
For most of them a user's token is needed.
This token can be obtain by the user on the login page. If you do not have an account you can create one on the 
register page.

