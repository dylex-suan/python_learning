import mysql.connector

# establish the connection for the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Spelling4bees!?!!",
    database="customerdatabase"
)

# create the database
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS trustee_database (name VARCHAR(255), time_served VARCHAR(255), city_rep VARCHAR(255))")


sql = "INSERT INTO trustee_database (name, time_served, city_rep) VALUES (%s, %s, %s)"
val = [
    ('Brenda Agnew', '3', 'Burlington'),
    ('Peter DeRosa', '3', 'Oakville'),
    ('Helena Karabela', '10', 'Oakville'),
    ('Helena Karabela', '10', 'Oakville'),
    ('Vincent Iantomasi', '3', 'Burlington'),
    ('Tim O\'\'Brien', '3', 'Burlington'),
    ('Janet O\'\'Hearn-Czarnota', '3', 'Halton Hills'),
    ('Martin Duarte', '3', 'Milton'),
    ('Patrick Murphy', '3', 'Milton'),
    ('Nancy Guzzo', '3', 'Oakville')
]

mycursor.executemany(sql, val)

if (mycursor.rowcount == 1):
    print("1 record was inserted.")
else:
    print(mycursor.rowcount, "records were inserted.")

"""
mycursor = mydb.cursor()
sql = "SELECT * FROM trustee_database WHERE time_served = %s"
adr = ('3', )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor = mydb.cursor()
sql = "SELECT * FROM trustee_database WHERE city_rep = %s"
adr = ("Burlington", )
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

"""
print('\n')
sql = "SELECT * FROM trustee_database ORDER BY time_served DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

print('\n')
mycursor.execute("SELECT * FROM trustee_database")
myresult = mycursor
for x in myresult:
    print(x)

print('\n')
sql = "SELECT name, COUNT(name) FROM trustee_database GROUP BY time_served HAVING COUNT(name) > 1"
mycursor.execute(sql)
myresult = mycursor
for x in myresult:
    print(x)

mycursor = mydb.cursor()
sql = "DELETE FROM trustee_database"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

# we gonna connect to the database and execute a table from which we can write data to
# if we want to delete an existing table by using DROP TABLE, that is also possible
# to prevent errors (e.g., if the table doesn't exist)
sql = "DROP TABLE trustee_database"
mycursor.execute(sql)
