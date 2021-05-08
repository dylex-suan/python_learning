# create a connection to the database
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!"
)

print(mydb)

# create a database named mydatabase
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase") # this creates the database

# used to access the database when making the connection
"""
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
"""

# connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!",
    database="mydatabase"
)

# to create a table in MySQL, use CREATE TABLE
"""
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
"""

# if table exists, we can check by listing all tables in the database
mycursor = mydb.cursor()
"""
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
"""

# this will create a column with a unique key for each record; the table exists though

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


# we execute this instead since the table exists already
"""
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
"""

# to fill a table in MySQL, use "INSERT INTO"

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit() # we must execute this to make the changes, otherwise no changes are made
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