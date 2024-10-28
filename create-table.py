import sqlite3
# link to the course: https://www.youtube.com/watch?v=byHcYRpMgI4

# Connect to the DB
conn = sqlite3.connect('customer.db')

# Create a cursor
cur = conn.cursor()

# Create a table
cur.execute("""CREATE TABLE customers (
        first_name TEXT,
        last_name TEXT,
        email TEXT
    )""")
# commit our command
conn.commit()

# Close the connection
conn.close()
