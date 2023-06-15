import mysql.connector
import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

connection = mysql.connector.connect(user='root',
                                     password='1234567hjkw',
                                     host='localhost',
                                     database='miragedb')

cursor = connection.cursor()

for i in range(1,10000):  # 1 million times
    random_first_name = get_random_string(5)
    random_last_name = get_random_string(8)
    email = f'{random_first_name}.{random_last_name}@example.com'
    cursor.execute(f"INSERT INTO Students (StudentID, FirstName, LastName, Email) VALUES ({i}, '{random_first_name}', '{random_last_name}', '{email}')")

connection.commit()  # Don't forget to commit changes

cursor.close()
connection.close()
