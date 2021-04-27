# joining two or more tables

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!"
)

# create my database
mycursor = mydb.cursor()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!",
    database="customerdatabase"
)

"""
mycursor = mydb.cursor()

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
mycursor = mydb.cursor()
mycursor.execute(
    "CREATE TABLE products (name VARCHAR(255), address VARCHAR(255))")

mycursor = mydb.cursor()
sql = "SELECT \
    users.name AS user, \
    products.name AS favorite \
    FROM users \
    INNER JOIN products ON users.name = products.address"

mycursor.execute(sql)

myresult = mycursor.fetchall()
for x in myresult:
    print(x)
