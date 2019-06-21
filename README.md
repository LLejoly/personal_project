# Freezer manager

The code related to this project follows this directory architecture:
```
personal_project
├── database
├── documentation
├── external_website
├── website
├── rest_api
├── flask_run.sh
├── run_server.sh
└── README
```
- `database`: directory that contains a sample of the database created with the schema linked to it.
- `documentation`: directory contains files related to the API documentation and the website built for that effect.
- `external_website`: directory contains files used to built the `external_website`.
- `REST_api`: directory contains files used to build the REST API server and communicate with the database.
- `flask_run.sh` and `run_server.sh` are scripts used to run severs(note that the settings used in these scripts are dependent of the system installation. If you want to use these scripts please refer to the following section.

# Pre-installation required (Xampp server)

To use the API you need to install XAMPP [click here](https://www.apachefriends.org/fr/index.html)
The version used is PHP Version 7.0.27

- You need to install xampp server in the `/opt` directory. Normally is the default place which proposed by xampp.
- When the server is installed you can run it. When it is running you can open your favorite browser and  type `localhost/dashboard`
Normally you should have a xampp webpage.  On the header click on `phpMyAdmin` button to go to phpMyAdmin panel.
- On the phpMyAdmin you can import a new database. Import the sql defined in the database `folder`.

Add a reference to the website folder.
- go to `opt/lampp/htdocs` and create a symbolic link that refers to the `website` folder. To do a symbolic link 
```
ln -s /path/of/the/website/directory/ freezer_manager
```
- When it is done you should have access to the website `http://localhost/freezer_manager/` note that xampp server must be running.

# Pre-installation required (python)

Python version used is python 3.6

To use the REST API a number of modules are needed:
- flask link [here](http://flask.pocoo.org/)
- MySQLdb link [here](http://mysqlclient.readthedocs.io/)
- flask_limiter link [here](https://flask-limiter.readthedocs.io/en/stable/)

To run the REST API the xampp need to be active. You can run it by simply use the `run_server.sh` as root.
When the  Xampp server is running you can run `flask_run.sh` script with database name `freezer` as parameter.

Then all servers need to use the API are set.

# TODO list
- [ ] Create a better site example
- [ ] Rework the SQL commands with SQLalchemy
- [ ] Add new functionalities
