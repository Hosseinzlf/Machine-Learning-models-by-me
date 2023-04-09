#Update sql file with a specific condition

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect(db_path)
    
# Define the values to be inserted and the condition to update the column
date_ = str('xxxxxxxx')
value = str('yyyyyyyy')

# Define the SQL query with the conditional WHERE clause
sql_query = "UPDATE sun_detection SET sun_filter_Th30_Val5 = ? WHERE datetime = ?"

# Create a cursor object to execute SQL queries
cursor = conn.cursor()    

# Execute the SQL query with the values using the cursor object
cursor.execute(sql_query, (value, date_))

# Commit the changes to the database
conn.commit()

# Close the cursor and database connection
cursor.close()
conn.close()
