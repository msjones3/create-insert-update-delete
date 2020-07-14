import sqlite3

# connect to database
try:
    db = sqlite3.connect('student.db')
    cursor= db.cursor()
    # here is my SQL statement - I can use w3schools
    # SQL + Python + delete to find this

    cursor.execute("DELETE FROM students WHERE lastNAME = 'Jones'")

    # save changes
    db.commit()
    print("record(s) deleted. ")

except Exception as error_msg:
    print("An error Occurred: ", error_msg)

finally:
    db.close()

