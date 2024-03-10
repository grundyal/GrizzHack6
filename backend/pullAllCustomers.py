import mariadb
import sys

def getAllCustomers():
    # Create a connection to the database
    conn = mariadb.connect(
        user="db_user",
        password="db_user_passwd",
        host="192.0.2.1",
        port=3306,
        database="info"
    )
    # Create a cursor object
    cursor = cnx.cursor()

    # Execute a SQL query
    cursor.execute("SELECT * FROM info")

    # Fetch all the rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    cnx.close()
