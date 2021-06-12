[![AudioService](https://github.com/olahsymbo/AudioService/actions/workflows/audio-service-pipeline.yml/badge.svg)](https://github.com/olahsymbo/AudioService/actions/workflows/audio-service-pipeline.yml)

## Audio Service
This service provides functionality (endpoints) to create, read, upload, and delete audio file
from the database.


## Getting Started 

The following steps will guide you through setting up the project

First, clone the repo 

`git clone https://github.com/olahsymbo/AudioService.git`

#### Install and configure virtual environment

Goto project directory and setup virtual environment:

```
cd AudioService
pip3 install virtualenv
virtualenv audioserv
source audioserv/bin/activate
```

To ensure this app functions properly, install the dependencies in the `requirements.txt` Simply run:

`pip install -r requirements.txt`

#### Create a Postgres DB
First install postgresql 12.2 (incase it's not installed already).

Second, create a new postgres database named task using:

`CREATEDB audiodb;` 

inside the db shell, create username and password for the database using:

`CREATE USER audiodev with encrypted password 'audiodev';` 


### Run the AudioService 

Launch the flask web server using:

`python app.py`

The base url is:

`http://127.0.0.1:5000/`

A sample request to create a song file:
```
curl --location --request POST 'http://127.0.0.1:5000/create' \
--form 'audioFileType="song"' \
--form 'audioFileMetadata="{\"name\": \"fernando\", \"duration\": \"106\",
\"uploaded_at\": \"20210220\"}"'
```

### API Response

The standard expected response is `.json` with:
```
{
    "data": {
        "duration": 106,
        "id": 18,
        "name": "fernando",
        "uploaded_at": "Sat, 20 Feb 2021 00:00:00 GMT"
    },
    "status": "success"
}
```


Standard error response will be:

```
{
    "code": 500,
    "data": [],
    "message": "internal server error",
    "status": "error"
}
```