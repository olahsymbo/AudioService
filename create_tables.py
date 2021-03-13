import psycopg2
from db_config import *
import warnings
warnings.filterwarnings("ignore")

# get the postgres db connection parameters from environment variable
name = os.environ.get('name')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')

# connect an instance of postgres DB
con = psycopg2.connect(database=name, user=user, password=password, host=host, port=port)
print("Database opened successfully")

cursor = con.cursor()

## creating tables
cursor.execute("CREATE TABLE song "
               "(id SERIAL PRIMARY KEY NOT NULL, "
               "name VARCHAR(100) NOT NULL, "
               "duration INT NOT NULL, "
               "uploaded_at TIMESTAMP NOT NULL)")

cursor.execute("CREATE TABLE podcast "
               "(id SERIAL PRIMARY KEY NOT NULL, "
               "name VARCHAR(100) NOT NULL, "
               "duration INT NOT NULL, "
               "host VARCHAR(100) NOT NULL, "
               "participants VARCHAR(100), "
               "uploaded_at TIMESTAMP NOT NULL)")

cursor.execute("CREATE TABLE audiobook "
               "(id SERIAL PRIMARY KEY NOT NULL, "
               "title VARCHAR(100) NOT NULL, "
               "author VARCHAR(100) NOT NULL, "
               "narrator VARCHAR(100) NOT NULL, "
               "duration INT NOT NULL, "
               "uploaded_at TIMESTAMP NOT NULL)")

print("Table created successfully")
con.commit()
con.close()
