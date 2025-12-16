#I DONT UNDERSTAND!!!
#this is something i dont understand so feel free to skip to the next tutorial


import sqlite3

class Person:
    def __init__(self, idnumber=None, first=None, last=None, age=None):
        self.idnumber = idnumber
        self.first = first
        self.last = last
        self.age = age

        # correct connection inside the class
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()

    def load_person(self, id_number):
        self.cursor.execute(
            "SELECT * FROM persons WHERE id = ?", 
            (id_number,)
        )
        row = self.cursor.fetchone()

        if row:
            self.idnumber = row[0]
            self.first = row[1]
            self.last = row[2]
            self.age = row[3]
        else:
            print("No user with that ID.")


# ------------------- OUTSIDE THE CLASS -------------------

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

cursor.executemany("""
INSERT INTO persons (first_name, last_name, age)
VALUES (?, ?, ?)
""", [
    ('Paul', 'Smith', 24),
    ('Mark', 'Johnson', 42),
    ('Anna', 'Smith', 34)
])

# Example SELECT
cursor.execute("SELECT * FROM persons WHERE last_name = 'Smith'")
rows = cursor.fetchall()
print(rows)

connection.commit()
connection.close()

# Example of loading a person object
p = Person()
p.load_person(1)
print(p.first, p.last, p.age)
