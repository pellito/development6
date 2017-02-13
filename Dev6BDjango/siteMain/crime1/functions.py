from extraMethods import Database, userData, cooldown
import time

def addmoney(amount):
    userData.userData.money += amount
    db = Database.getDatabase()
    cur3 = db.cursor()
    cur3.execute("UPDATE suspect SET money = " + str(
        userData.userData.money) + " WHERE username = '" + userData.userData.username + "'")

    db.commit()

def updateCooldown():
    db = Database.getDatabase()

    tempTijd = time.strftime("%H:%M:%S")
    tempDatum = time.strftime("%d/%m/%y")

    cur = db.cursor()
    cur.execute(
        "UPDATE suspect_cd SET cooldown = 90 WHERE username = '" + userData.userData.username + "' AND cId = 1")
    curx = db.cursor()
    curx.execute(
        "UPDATE suspect_cd SET datum = '" + tempDatum + "' WHERE username = '" + userData.userData.username + "' AND cId = 1")
    cury = db.cursor()
    cury.execute(
        "UPDATE suspect_cd SET tijd = '" + tempTijd + "' WHERE username = '" + userData.userData.username + "' AND cId = 1")
    db.commit()

def addExperience():
    userData.userData.crime1exp += 10

    db = Database.getDatabase()
    cur= db.cursor()

    cur.execute("UPDATE suspect_crimes SET experience = " + str(
        userData.userData.crime1exp) + " WHERE username = '" + userData.userData.username + "' AND cId = 1")
    db.commit()

def setCooldown():
    db = Database.getDatabase()
    cur = db.cursor()
    cur.execute(
        "SELECT s.cooldown, s.datum, s.tijd FROM suspect_cd s WHERE s.username = '" + userData.userData.username + "' AND s.cId = 1")
    for row in cur.fetchall():
        if row != None:
            userData.userData.tempCd = row[0]
            userData.userData.tempDatum = row[1]
            userData.userData.tempTijd = row[2]
    cooldown.checkforCooldown(90, userData.userData.username, 1, userData.userData.tempTijd, userData.userData.tempDatum)

    cur = db.cursor()
    cur.execute(
        "SELECT s.cooldown, s.datum, s.tijd FROM suspect_cd s WHERE s.username = '" + userData.userData.username + "' AND s.cId = 1")
    for row in cur.fetchall():
        if row != None:
            userData.userData.tempCd = row[0]
            userData.userData.tempDatum = row[1]
            userData.userData.tempTijd = row[2]



