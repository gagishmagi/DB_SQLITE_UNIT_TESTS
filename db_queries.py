import sqlite3

database = 'PersonsDB.sqlite'

conn = sqlite3.connect(database)
cursor = conn.cursor()


def get_all_persons():
    result = cursor.execute("SELECT * FROM Persons")
    return result.fetchall()


def get_person_by_id(id):
    result = cursor.execute("SELECT * FROM Persons WHERE id=?", (id,))
    return result.fetchone()

def get_person_by_name(name):
    result = cursor.execute("SELECT * FROM Persons WHERE name=?", (name,))
    return result.fetchone()

def create_person(last_name, first_name, address, city):
    cursor.execute("INSERT INTO Persons (LastName, FirstName, Address, City) VALUES (?, ?, ?, ?)", (last_name, first_name, address, city))
    conn.commit()


def update_person(id, last_name, first_name, address, city):
    cursor.execute("UPDATE Persons SET LastName=?, FirstName=?, Address=?, City=? WHERE id=?", (last_name, first_name, address, city, id))
    conn.commit()

def delete_person(id):
    cursor.execute("DELETE FROM Persons WHERE id=?", (id,))
    conn.commit()

# for row in data:
#     if row == data[0]:
#         print(row[2])

# print(data[0][2])