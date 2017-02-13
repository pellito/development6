from django.test import TestCase
from extraMethods import userData, Database
from crime1.functions import addmoney, addExperience


# Create your tests here.
class Crime1TestCase(TestCase):
    username = "testsubject"
    password = "Ditisgeheim"
    def setUp(self):
        userData.userData.money = 0
        userData.userData.username = Crime1TestCase.username
        userData.userData.password = Crime1TestCase.password
        db = Database.getDatabase()
        cur = db.cursor()
        cur.execute("DELETE FROM suspect_cd WHERE username = '" + Crime1TestCase.username + "'")
        cur.execute("DELETE FROM suspect_crimes WHERE username = '" + Crime1TestCase.username + "'")
        cur.execute("DELETE FROM suspect WHERE username = '" + Crime1TestCase.username + "'")
        cur.execute("INSERT INTO suspect(username,password,rank,money,reputatie) VALUES('" + Crime1TestCase.username + "','" + Crime1TestCase.password + "',1,1000,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + Crime1TestCase.username + "',1,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + Crime1TestCase.username + "',2,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + Crime1TestCase.username + "',3,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + Crime1TestCase.username + "',4,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + Crime1TestCase.username + "',5,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + Crime1TestCase.username + "',6,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + Crime1TestCase.username + "',1,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + Crime1TestCase.username + "',2,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + Crime1TestCase.username + "',3,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + Crime1TestCase.username + "',4,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + Crime1TestCase.username + "',5,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + Crime1TestCase.username + "',6,0)")
        db.commit()
        db.close()
        pass

    def test_addMoney(self):
        userData.userData.money = 0
        db = Database.getDatabase()
        cur = db.cursor()
        cur.execute("UPDATE suspect SET money = 0 WHERE username = '" + Crime1TestCase.username + "'")
        db.commit()
        addmoney(10000)
        self.assertEqual(userData.userData.money, 10000)
        cur.execute("SELECT money FROM suspect WHERE username = '" + Crime1TestCase.username + "'")
        for rows in cur.fetchall():
            money = rows[0]
        self.assertEqual(money, 10000)



    def test_experience(self):
        userData.userData.crime1exp = 0
        db = Database.getDatabase()
        cur = db.cursor()
        cur.execute("UPDATE suspect_crimes SET experience = " + str(
            userData.userData.crime1exp) + " WHERE username = '" + Crime1TestCase.username + "' AND cId = 1")
        db.commit()
        addExperience()
        self.assertEqual(userData.userData.crime1exp,10)
        cur.execute("SELECT experience FROM suspect_crimes WHERE username = '" + str(Crime1TestCase.username) + "' AND cId = 1")
        for row in cur.fetchall():
            xp = row[0]
        self.assertEqual(xp,10)









