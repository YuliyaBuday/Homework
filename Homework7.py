import sqlite3 as sq

with sq.connect('PhoneBook.db') as con:
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Names(
        ID INTEGER,
        First Name TEXT,
        Surname TEXT,
        Phone Number VARCHAR
        )

        """
                )
    con.commit()
    users = [(1,"Simon","Howeis", "01223 349752"), (2,"Karen","Phillips", "01954 295773"),
            (3,"Darren","Smith", "01583 749012"),(4,"Anne","Jones", "01323 567322"),
            (5,"Mark","Smith", "01223 855534")]
    cur.executemany("INSERT INTO Names VALUES(?, ?, ?, ?);", users)
    con.commit()