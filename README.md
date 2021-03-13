## Audio Service
This service provides functionality (endpoints) to create, read, upload, and delete audio file
from the database.


## Getting Started 

The following steps will guide you through setting up the project

First, clone the repo 

`git clone https://wikoced@bitbucket.org/hypi-universe/hypi_services_ocr.git`

#### Install and configure virtual environment

Goto project directory:

`cd hypi_services_ocr`

Inside the directory install virtual environment:

`pip3 install virtualenv` 

Setup a virtualenv name for the project e.g:

`virtualenv ocrenv`

Activate the virtual environment (important to activate this)

`source ocrenv/bin/activate`

To ensure this app functions properly, install the dependencies in the `requirements.txt` Simply run:

`pip install -r requirements.txt`

#### Create a Postgres DB
First install postgresql 12.2 (incase it's not installed already).

One way of doing this is to download the postgresql app from https://postgresapp.com/downloads.html or use homebrew by running:

`brew install postgresql`

After installing postgresql, start all postgresql services from terminal by either running (postgres must be running at all times):

`pg_ctl -D /usr/local/var/postgres start or brew services start postgresql`

Second, create a new postgres database named task using:

`CREATEDB nerdb;`

Afterward, launch the task db shell by running:

`psql nerdb`

create username and password for the database using:

`CREATE USER hypidev with encrypted password 'hypidev';`

grant all privileges of the db to USER hypidev using:

`GRANT ALL PRIVILEGES ON DATABASE task TO hypidev;`

grant the USER the role to create new db using:

`ALTER USER hypidev CREATEDB;`

Create the data fields in nerdb