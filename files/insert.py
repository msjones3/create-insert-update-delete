import sqlite3

# connect to db
try:
    db = sqlite3.connect('student.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO students (firstNAME, lastNAME, grade, dob) VALUES ('Cheryl', 'Jones', 'A', '07-02-1980')")

    # save database
    db.commit()
    print('new row added')

except Exception as error_msg:
    db.rollback()
    print("An error occurred: ", error_msg)

finally:
    db.close()