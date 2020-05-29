# FIrst download postgre: https://www.postgresql.org/download/

# pip install  psycopg2

import psycopg2

# STEPS
# Connect to a database
# Create a cursor object'with SQL query
# Commit changes
# Close database connection

def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
#    cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item, quantity, price))  # can be done this way, but susceptible to SQL injections     
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()       
    conn.close()        #We do not need commit while viewing
    return rows 


def delete(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))  # When you have one parameter include comma at the end!
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
#insert ("Apple", 10, 15)
#insert ("Orange", 5, 5)
#delete("Orange")
update(22, 22, 'Apple')

print(view())
