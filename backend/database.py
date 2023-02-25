import mysql.connector as mysql


# Creating connection object
mydb = mysql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database= "ninjavan_db",
    port=8889
)

my_cursor = mydb.cursor()

sql = "INSERT INTO user (name, address) VALUES (%s, %s)"
mock_data = [
    ('Peter', '111 Yew Tee Street'),
    ('Jia Wei', '112 Boon Keng Street'),
    ('Dai Wei', '113 Cooperation Street'),
    ('Wei Jun', '114 Pasir Tee Street')

]


my_cursor.executemany(sql, mock_data)

print(my_cursor.rowcount, "was inserted")

## defining the Query
query = "SELECT * FROM user"

## getting records from the table
my_cursor.execute(query)

## fetching all records from the 'cursor' object
records = my_cursor.fetchall()

## Showing the data
for record in records:
    print(record)