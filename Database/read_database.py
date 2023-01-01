import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('Database/UserSavedData.db')

# cursor object
cursor_obj = connection_obj.cursor()

# to select all column we will use
statement = '''SELECT * FROM saved_house_data'''

cursor_obj.execute(statement)

print("All the data")
output = cursor_obj.fetchall()
for row in output:
    print(row)

connection_obj.commit()

# Close the connection
connection_obj.close()
