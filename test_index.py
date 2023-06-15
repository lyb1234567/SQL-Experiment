import mysql.connector
import random
import string
import time
def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
connection = mysql.connector.connect(user='root',
                                     password='1234567hjkw',
                                     host='localhost',
                                     database='miragedb')
cursor = connection.cursor()
try:
    cursor.execute("ALTER TABLE students DROP INDEX idx_students_lastname")
except:
    pass 
start = time.time()
cursor.execute("SELECT * FROM Students WHERE LastName = 'rhwjfnca'")
results = cursor.fetchall()
end = time.time()
print(f"Time without index: {(end - start)*1000} ms")
cursor.execute('CREATE INDEX idx_students_lastname ON Students (LastName)')
# Measure time to execute query with index
start = time.time()
cursor.execute("SELECT * FROM Students WHERE LastName = 'rhwjfnca'")
results = cursor.fetchall()
end = time.time()
print(f"Time with index: {(end - start)*1000} ms")

cursor.close()
connection.close()