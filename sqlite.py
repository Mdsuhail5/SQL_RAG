import sqlite3

# connect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record, create table
cursor = connection.cursor()

# create the table
table_info = """
CREATE TABLE STUDENT (NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25), MARKS INT)
"""

# Execute the CREATE TABLE statement
cursor.execute(table_info)

# Insert some more records
cursor.execute(
    ''' Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute(
    ''' Insert Into STUDENT values('John','Data Science','A',100)''')
cursor.execute(''' Insert Into STUDENT values('Mukesh','Devops','A',86)''')
cursor.execute(
    ''' Insert Into STUDENT values('Jacob','Data Science','A',90)''')
cursor.execute(''' Insert Into STUDENT values('Dipesh','Devops','A',50)''')

# Display all the records
print('The inserted records are')
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
