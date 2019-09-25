# Flask Rest APIs CRUD - CREATE, READ, UPDATE, DELETE.

A Basic Flask Application to crud operations.

## Prerequisites:

You will need the following programs properly installed on your computer.

* [Python](https://www.python.org/) 3.6+
* [Postgres](https://www.postgresql.org/)

To install the virtual environment on your system use:

```bash
sudo apt-get install python3-venv -y

## Installation:

```bash
git clone https://github.com/ongraphpythondev/flask-rest.git

cd flask-rest

python3 -m venv venv

source venv/bin/activate

# install required packages for the project to run
pip install -r requirements.txt
```
Configure database setting
* Open instance/config.py and add your database setting.

* SQLALCHEMY_DATABASE_URI = 'postgresql://postgres_user:postgres_password@localhost/postgres_api'


## Running:

To run the development server after installation:

```bash

# run server
$ export FLASK_CONFIG=development
$ export FLASK_APP=run.py
$ flask db migrate
$ flask db upgrade
$ flask run
```

# Test APIs
#### Create User- 

    Method: POST

    URL: 127.0.0.1:5000/user

    Body:{
           "username":"test",
           "email":"test@gmail.com"
	 }

#### Get All Users- 

    Method: GET

    URL: 127.0.0.1:5000/user


#### Get Single Users- 

    Method: GET

    URL: 127.0.0.1:5000/user/id


#### Update User- 

    Method: PUT

    URL: 127.0.0.1:5000/user/id

    Body:{
           "username":"test1",
           "email":"test1@gmail.com"
	 }


#### Delete User- 

    Method: DELETE

    URL: 127.0.0.1:5000/user/id


