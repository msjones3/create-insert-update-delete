import sqlite3

try:
    db = sqlite3.connect('student.db')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    studentID integer PRIMARY KEY AUTOINCREMENT,
    firstNAME text NOT NULL,
    lastName text NOT NULL,
    grade integer,
    dob text
);""")

    # commmit changes
    db.commit()
    print("table created")

except Exception as error:
    db.rollback()
    print("something went wrong: " + str(error))

finally:
    db.close()

