import sqlite3 as sq

with sq.connect('PhoneBook.db') as con:
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Names(
        ID INTEGER primary key AUTOINCREMENT,
        "First Name" TEXT,
        Surname TEXT,
        "Phone Number" TEXT
        )

        """
                )
    con.commit()
    users = [("Simon","Howeis", "01223 349752"), ("Karen","Phillips", "01954 295773"),
            ("Darren","Smith", "01583 749012"),("Anne","Jones", "01323 567322"),
            ("Mark","Smith", "01223 855534")]
    cur.executemany(""" INSERT INTO Names ("First Name",Surname, "Phone Number") VALUES(?, ?, ?);""", users)
    con.commit()