from extraMethods import Database


class userData():
    tempCd = 0
    tempDatum = ''
    tempTijd = ''

    username = ''
    password = ''
    rank = 0
    money = 0
    reputatie = 0
    crime1exp = 0
    crime2exp = 0
    crime3exp = 0
    crime4exp = 0
    crime5exp = 0
    crime6exp = 0
    fakeCooldown = 10

    def prepareData(self):
        db = Database.getDatabase()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM suspect WHERE username = '" + userData.username + "'")
        for rows in cursor.fetchall():
            userData.rank = rows[2]
            userData.money = rows[3]
            userData.reputatie = rows[4]

        cursor2 = db.cursor()
        cursor2.execute("SELECT * FROM suspect_crimes where username = '" + userData.username + "'")
        for rows in cursor2.fetchall():
            if rows[1] == 1:
                userData.crime1exp = rows[2]
            if rows[1] == 2:
                userData.crime2exp = rows[2]
            if rows[1] == 3:
                userData.crime3exp = rows[2]
            if rows[1] == 4:
                userData.crime4exp = rows[2]
            if rows[1] == 5:
                userData.crime5exp = rows[2]
            if rows[1] == 6:
                userData.crime6exp = rows[2]

    def testMethod():
        # hier kijkt hij wat je cooldown is.
        if userData.fakeCooldown > 0:
            return 1
        else:
            return 0
        # hij return 0 als er geen cooldown is.
