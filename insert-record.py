import sqlite3
# link to the course: https://www.youtube.com/watch?v=byHcYRpMgI4

# Connect to the DB
conn = sqlite3.connect('customer.db')

# Create a cursor
cur = conn.cursor()

cur.execute()

conn.commit()

# Close the connection
conn.close()
