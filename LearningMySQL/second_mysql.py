import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!"
)

# create my database
"""
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE customerdatabase")
"""
# connect to the database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!",
    database="customerdatabase"
)


mycursor = mydb.cursor()
"""
mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()  # we must execute this to make the changes, otherwise no changes are made
print(mycursor.rowcount, "record inserted.")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central St 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")
"""
# getting the id of the row by asking the cursor object
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor
for x in myresult:
    print(x)

## fetchall() fetches or returns all rows from the last executed statement
mycursor = mydb.cursor()
mycursor.execute("SELECT name, address from CUSTOMERS")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# if only interested in one row, we use fetchone() method, which 
# in this case, will return the first row of the result

"""
print('\n')
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)
"""

print('\n')
# you may also do filters to fitler the selection by using the "WHERE" statement
mycursor = mydb.cursor()
sql = "SELECT * FROM customers WHERE address ='One way 98'"
mycursor.execute(sql)
myresult = mycursor.fetchall() # fetch all rows which have the address 'Park Lane 38'
for x in myresult:
    print(x)

# wildcard characters are records that starts, includes or ends with a given letter or phraase
sql = "SELECT * FROM customers WHERE address LIKE '%Y%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('\n')

# IMPORTANT:
# should query values be provided by the user, you must escape the values
# intended to prevent SQL injections, used to destroy or misuse your database
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",) # must have the comma at the end
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)


# we can sort the result in either ascending or descending order
# by default it's always ascending, so in descending order, we use DESC
sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# deleting record using DELETE FROM
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Green Grass 1", )
mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

# when we update, you MUST include the WHERE, otherwise all the records will be updated
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123", )
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

"""
print('\n')
mycursor = mydb.cursor()
sql = "SELECT name, address FROM customers"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor = mydb.cursor()
# if we want to delete an existing table by using DROP TABLE, that is also possible
# to prevent errors (e.g., if the table doesn't exist)
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
"""

# limiting the number of records returned from the query
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 9")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('\n')
# we can also return records but from another position in the table (OFFSET)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 9 OFFSET 2")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
