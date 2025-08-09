import mysql.connector

def create_database():
    try: 
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root", 
            password = "Legend009$",
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        # Close cursor and connection
        try:
            if mycursor:
                mycursor.close()
            if mydb and mydb.is_connected():
                mydb.close()
        except:
            pass

if _name_ == "_main_":
    create_database()
