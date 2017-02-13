from django.shortcuts import render
import mysql.connector
from extraMethods import userData

class userpassword:
    username = ''
    password = ''
    crime1exp = 0
    crime2exp = 0
    crime3exp = 0
    crime4exp = 0
    crime5exp = 0
    crime6exp = 0


def index(request):
    if request.method == 'GET':
        if (request.GET.get('username') != None):
            userpassword.username = request.GET.get('username')
            userData.userData.username = request.GET.get('username')
        if (request.GET.get('password') != None):
            userpassword.password = request.GET.get('password')
            userData.userData.password = request.GET.get('password')

    amount = 0
    money = -1
    correctness = -1
    rank = 'Dit is een test, word niet boos aub!'
    money = 0
    user = 'ikke'
    reputatie = 0

    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 db="dev6")
    cur = db.cursor()
    cur.execute("SELECT * FROM suspect WHERE username = '" + userpassword.username + "'")
    for row in cur.fetchall():
        amount = amount + 1
        if (userpassword.username == row[0] and userpassword.password == row[1]):
            correctness = 1
            rank = row[2]
            money = row[3]
            #reputatie = row[4]

        else:
            correctness = 0
    cur.execute("SELECT crimes.cDesc from suspect, crimes, suspect_crimes WHERE suspect_crimes.username = '" + userpassword.username + "' AND suspect_crimes.cId = crimes.cId AND suspect.rank = crimes.cId")
    for row in cur.fetchall():
        rank = row[0]
    cur.execute("SELECT * FROM suspect_crimes WHERE username = '" + userpassword.username + "'")
    for row in cur.fetchall():
        if row[1] == 1:
            userpassword.crime1exp = row[2]
        if row[1] == 2:
            userpassword.crime2exp = row[2]
        if row[1] == 3:
            userpassword.crime3exp = row[2]
        if row[1] == 4:
            userpassword.crime4exp = row[2]
        if row[1] == 5:
            userpassword.crime5exp = row[2]
        if row[1] == 6:
            userpassword.crime6exp = row[2]

    db.close()
    if (amount == 1 and correctness == 1):
        return render(request, 'loggedin/home.html',
                      {'content': [rank, userpassword.crime1exp, userpassword.crime2exp, userpassword.crime3exp, userpassword.crime4exp, userpassword.crime5exp, userpassword.crime6exp,userpassword.username,money,reputatie]})
    else:
        return render(request, 'loggedin/loginfail.html')

def registercomplete(request):
    amount = 0
    username = request.GET['username']
    password = request.GET['passwordd']
    password2 = request.GET['password2']
    amount = 0
    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 db="dev6")
    cur2 = db.cursor()
    cur2.execute("SELECT * FROM suspect WHERE username = '" + username + "'")
    data = cur2.fetchall()
    for row in data:
        amount = amount + 1
    if (amount == 0 and password == password2):
        cur = db.cursor()
        cur.execute("INSERT INTO suspect(username,password,rank,money,reputatie) VALUES('" + username + "','" + password + "',1,1000,0)")

        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + username + "',1,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + username + "',2,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + username + "',3,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + username + "',4,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + username + "',5,0)")
        cur.execute("INSERT INTO suspect_cd(username,cId,cooldown) VALUES('" + username + "',6,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + username + "',1,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + username + "',2,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + username + "',3,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + username + "',4,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + username + "',5,0)")
        cur.execute("INSERT INTO suspect_crimes(username,cId,experience) VALUES('" + username + "',6,0)")

        db.commit()
        db.close()
        return render(request, 'loggedin/registercomplete.html')
    else:
        return render(request,'loggedin/registerfail.html')