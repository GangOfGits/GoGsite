from passlib.hash import pbkdf2_sha256 as sha256
import pyodbc
from databaser import connect
#Connects to the login database using databaser.py
connection = connect()
#Creates a cursor from the connection, which can be used to execute queries
cursor = connection.cursor()

def verify_user_exists(username):
    username = username.lower() #Usernames are not case sensitive
    #SQL Query to be executed by the cursor
    query = "SELECT 1 FROM Users WHERE username = ?"
    cursor.execute(query, (username))
    return True if cursor.fetchone() is not None else False


#Generates a hash to be stored in the database, based on the password and a generated salt
def generate_hash(password):
    hash = sha256.hash(password)


#Checks a password against a parsed hash to verify that the password is correct.
#This hash should come from the login database and the users table
def verify_password(username, password):
    username = username.lower() #Usernames are not case sensitive
    #SQL Query to be executed by the cursor
    query = "SELECT hash FROM Users WHERE username = ?"
    cursor.execute(query, (username))
    fetch = cursor.fetchone()
    if fetch is not None:
        hash = fetch[0]
        return sha256.verify(password, hash)
    else:
        return False
