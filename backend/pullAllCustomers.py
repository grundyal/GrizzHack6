import mariadb
import sys

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'password',
    'database': 'grizzhack'
}

def getAllCustomers():
    conn = mariadb.connect(**config)
    # create a connection cursor
    cur = conn.cursor()
    query = f"SELECT * FROM info"
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit() 
    conn.close() 

    return rows
