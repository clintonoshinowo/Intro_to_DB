#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode

# Your database connection credentials
# NOTE: Replace with your actual username and password
DB_HOST = 'localhost'
DB_USER = 'clintonoshinowo'
DB_PASSWORD = '@Lamp1235'

def create_database():
    """Connects to MySQL and creates the alx_book_store database."""
    try:
        # Establish a connection to the MySQL server without specifying a database
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = connection.cursor()

        db_name = "alxbookstore"

        # SQL query to create the database if it doesn't exist
        # This prevents the script from failing if the database is already there
        create_db_query = "CREATE DATABASE IF NOT EXISTS {}".format(db_name)
        
        cursor.execute(create_db_query)
        print("Database '{}' created successfully!".format(db_name))

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Please check your username and password.")
        else:
            print("Error: {}".format(err))
    
    finally:
        # Close the cursor and connection if they were opened
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
