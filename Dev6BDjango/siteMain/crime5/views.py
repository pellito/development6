from django.shortcuts import render
from loggedin import views
import random
from extraMethods import Database, userData, cooldown
import time


def index(request):
    userData.userData.prepareData(userData.userData)
    crime51perc = round(userData.userData.crime5exp / 9, 2)
    crime52perc = round(userData.userData.crime5exp / 10, 2)
    crime53perc = round(userData.userData.crime5exp / 11, 2)
    crime54perc = round(userData.userData.crime5exp / 13, 2)
    return render(request, 'crime5/home.html', {'content': [crime51perc, crime52perc, crime53perc, crime54perc]})


def offroad(request):
    x = crimey5(request,1)
    return x

def binnenstad(request):
    x = crimey5(request,2)
    return x

def platteland(request):
    x = crimey5(request,3)
    return x

def snelweg(request):
    x = crimey5(request,4)
    return x

def crimey5(request,crimeN):


    cd = 0
    datum = ''
    tijd = ''
    db = Database.getDatabase()
    userData.userData.prepareData(userData.userData)
    crime51perc = round(userData.userData.crime5exp / 9,2)
    crime52perc = round(userData.userData.crime5exp / 10,2)
    crime53perc = round(userData.userData.crime5exp / 11,2)
    crime54perc = round(userData.userData.crime5exp / 13,2)
    if crime51perc > 100:
        crime51perc = 100
    if crime52perc > 100:
        crime52perc = 100
    if crime53perc > 100:
        crime53perc = 100
    if crime54perc > 100:
        crime54perc = 100

    if request.method == 'POST':

        if crimeN == 2:
            if userData.userData.reputatie < 10:
                return render(request, 'crime5/noRep.html',
                              {'content': [crime51perc, crime52perc, crime53perc, crime54perc]})
        elif crimeN == 3:
            if userData.userData.reputatie < 25:
                return render(request, 'crime5/noRep.html',
                              {'content': [crime51perc, crime52perc, crime53perc, crime54perc]})
        elif crimeN == 4:
            if userData.userData.reputatie < 50:
                return render(request, 'crime5/noRep.html',
                              {'content': [crime51perc, crime52perc, crime53perc, crime54perc]})


        cur = db.cursor()
        cur.execute("SELECT s.cooldown, s.datum, s.tijd FROM suspect_cd s WHERE s.username = '" + views.userpassword.username + "' AND s.cId = 5")
        for row in cur.fetchall():
            if row != None:
                cd = row[0]
                datum = row[1]
                tijd = row[2]
        cooldown.checkforCooldown(90, userData.userData.username, 5, tijd, datum)

        cur = db.cursor()
        cur.execute(
            "SELECT s.cooldown, s.datum, s.tijd FROM suspect_cd s WHERE s.username = '" + views.userpassword.username + "' AND s.cId = 5")
        for row in cur.fetchall():
            if row != None:
                cd = row[0]
                datum = row[1]
                tijd = row[2]

        if userData.userData.fakeCooldown > 0:
            return render(request, 'crime5/onCooldown.html',
                          {'content': [crime51perc, crime52perc, crime53perc, crime54perc]})
        else:
            tempTijd = time.strftime("%H:%M:%S")
            tempDatum = time.strftime("%d/%m/%y")

            cur = db.cursor()
            cur.execute("UPDATE suspect_cd SET cooldown = 90 WHERE username = '"+ userData.userData.username + "' AND cId = 5")
            curx = db.cursor()
            curx.execute(
                "UPDATE suspect_cd SET datum = '"+ tempDatum + "' WHERE username = '" + userData.userData.username + "' AND cId = 5")
            cury = db.cursor()
            cury.execute(
                "UPDATE suspect_cd SET tijd = '"+ tempTijd +"' WHERE username = '" + userData.userData.username + "' AND cId = 5")
            cur2 = db.cursor()
            cur2.execute("UPDATE suspect_crimes SET experience = " + str(userData.userData.crime5exp + 10) + " WHERE username = '" + userData.userData.username + "' AND cId = 5" )
            db.commit()
            crime5Round0 = 0
            if crimeN == 1:
                crime5Round0 = round(crime51perc,0)
            elif crimeN == 2:
                crime5Round0 = round(crime52perc,0)
            elif crimeN == 3:
                crime5Round0 = round(crime53perc,0)
            elif crimeN == 4:
                crime5Round0 = round(crime54perc,0)

            rnd = random.randint(1,100)
            rnd2 = random.randint(10000,25000)
            if rnd <= (crime5Round0):
                if crimeN == 1:
                    userData.userData.reputatie = userData.userData.reputatie + 1
                elif crimeN == 2:
                    userData.userData.reputatie = userData.userData.reputatie + 2
                elif crimeN == 3:
                    userData.userData.reputatie = userData.userData.reputatie + 3
                elif crimeN == 4:
                    userData.userData.reputatie = userData.userData.reputatie + 4
                rep = userData.userData.reputatie
                money = userData.userData.money = userData.userData.money + rnd2
                cu = db.cursor()
                cu.execute("UPDATE suspect SET reputatie = " + str(userData.userData.reputatie) + " WHERE username = '" + userData.userData.username + "'")
                cur2 = db.cursor()
                cur2.execute("UPDATE suspect SET money = " + str(money) + " WHERE username = '" + userData.userData.username + "'")
                db.commit()
                return (render(request, 'crime5/success.html',
                              {'content': [crime51perc, crime52perc, crime53perc, crime54perc,
                                           rnd2]}))
            else:
                if crimeN == 1:
                    userData.userData.reputatie = userData.userData.reputatie - 1
                elif crimeN == 2:
                    userData.userData.reputatie = userData.userData.reputatie - 2
                elif crimeN == 3:
                    userData.userData.reputatie = userData.userData.reputatie - 3
                elif crimeN == 4:
                    userData.userData.reputatie = userData.userData.reputatie - 4

                if userData.userData.reputatie < -9:
                    userData.userData.reputatie = -10

                rep = userData.userData.reputatie
                cu = db.cursor()
                cu.execute("UPDATE suspect SET reputatie = " + str(rep) + " WHERE username = '" + userData.userData.username + "'")
                db.commit()
                return render(request, 'crime5/failed.html', { 'content': [crime51perc,crime52perc,crime53perc,crime54perc]})
    else:
        return render(request, 'crime5/home.html', {'content': [crime51perc, crime52perc, crime53perc, crime54perc]})

