import sqlite3

# connect to database
try:
    db = sqlite3.connect('student.db')
    cursor=db.cursor()
    cursor.execute("UPDATE students SET grade = 'B-'")

    # save changes
    db.commit()
    print('update complete')

except Exception as error_msg:
    print("An error occurred: ", error_msg)

finally:
    db.close()