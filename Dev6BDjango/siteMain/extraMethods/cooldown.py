import time
from extraMethods import Database

def checkforCooldown(cooldown,username,crime,hour1,date1):
    hour2 = time.strftime("%H:%M:%S")
    date2 = time.strftime("%d/%m/%y")
    db = Database.getDatabase()
    if date1 != date2:
        cur = db.cursor()
        cur.execute(
            "UPDATE suspect_cd SET cooldown = 0 WHERE username = '" + username + "' AND cId = " + str(crime))

        return 0
    else:
        x1 = hour1.split(':')
        h1 = int(x1[0])
        m1 = int(x1[1])
        s1 = int(x1[2])
        seconds1 = h1 * 3600 + m1 * 60 + s1

        x2 = hour2.split(':')
        h2 = int(x2[0])
        m2 = int(x2[1])
        s2 = int(x2[2])
        seconds2 = h2 * 3600 + m2 * 60 + s2

        if (seconds2 - seconds1) < cooldown:
            newCooldown = cooldown - (seconds2 - seconds1)
            cur = db.cursor()
            cur.execute(
                "UPDATE suspect_cd SET cooldown = "+ str(newCooldown) +" WHERE username = '" + username + "' AND cId = " + str(crime))
        else:
            cur = db.cursor()
            cur.execute(
                "UPDATE suspect_cd SET cooldown = 0 WHERE username = '" + username + "' AND cId = " + str(crime))
    db.commit()
