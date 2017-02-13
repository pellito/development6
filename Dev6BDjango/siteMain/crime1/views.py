from django.shortcuts import render
from loggedin import views
import random
from extraMethods import Database, userData, cooldown
from crime1 import functions
import time
# Create your views here.
def index(request):
    userData.userData.prepareData(userData.userData)
    crime11perc = round(userData.userData.crime1exp / 9)
    crime12perc = round(userData.userData.crime1exp / 11)
    crime13perc = round(userData.userData.crime1exp / 13)
    crime14perc = round(userData.userData.crime1exp / 15)
    crime15perc = round(userData.userData.crime1exp / 17)
    crime16perc = round(userData.userData.crime1exp / 21)

    if crime11perc >= 100:
        crime11perc = 100
    if crime12perc >= 100:
        crime12perc = 100
    if crime13perc >= 100:
        crime13perc = 100
    if crime14perc >= 100:
        crime14perc = 100
    if crime15perc >= 100:
        crime15perc = 100
    if crime16perc >= 100:
        crime16perc = 100

    functions.setCooldown()
    return render(request, 'crime1/home.html', {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})


def snoep(request):
    userData.userData.prepareData(userData.userData)
    crime11perc = round(userData.userData.crime1exp / 9)
    crime12perc = round(userData.userData.crime1exp / 11)
    crime13perc = round(userData.userData.crime1exp / 13)
    crime14perc = round(userData.userData.crime1exp / 15)
    crime15perc = round(userData.userData.crime1exp / 17)
    crime16perc = round(userData.userData.crime1exp / 21)

    if crime11perc >= 100:
        crime11perc = 100
    if crime12perc >= 100:
        crime12perc = 100
    if crime13perc >= 100:
        crime13perc = 100
    if crime14perc >= 100:
        crime14perc = 100
    if crime15perc >= 100:
        crime15perc = 100
    if crime16perc >= 100:
        crime16perc = 100

    functions.setCooldown()

    if userData.userData.tempCd > 0:
        return render(request, 'crime1/cooldown.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
    else:
        functions.updateCooldown()
        functions.addExperience()

        getal = random.randint(0,100)

        if getal <= crime11perc:

            functions.addmoney(1)

            return render(request, 'crime1/1true.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
        else:

            return render(request, 'crime1/1false.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})



def redbull(request):
    userData.userData.prepareData(userData.userData)
    crime11perc = round(userData.userData.crime1exp / 9)
    crime12perc = round(userData.userData.crime1exp / 11)
    crime13perc = round(userData.userData.crime1exp / 13)
    crime14perc = round(userData.userData.crime1exp / 15)
    crime15perc = round(userData.userData.crime1exp / 17)
    crime16perc = round(userData.userData.crime1exp / 21)

    if crime11perc >= 100:
        crime11perc = 100
    if crime12perc >= 100:
        crime12perc = 100
    if crime13perc >= 100:
        crime13perc = 100
    if crime14perc >= 100:
        crime14perc = 100
    if crime15perc >= 100:
        crime15perc = 100
    if crime16perc >= 100:
        crime16perc = 100

    functions.setCooldown()

    if userData.userData.crime1exp <= 250:
        return render(request, 'crime1/lowRank.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})

    if userData.userData.tempCd > 0:
        return render(request, 'crime1/cooldown.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
    else:
        functions.updateCooldown()
        functions.addExperience()

        getal = random.randint(0,100)

        if getal <= crime12perc:
            functions.addmoney(2)
            return render(request, 'crime1/1true.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
        else:
            return render(request, 'crime1/1false.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})


def telefoon(request):
    userData.userData.prepareData(userData.userData)
    crime11perc = round(userData.userData.crime1exp / 9)
    crime12perc = round(userData.userData.crime1exp / 11)
    crime13perc = round(userData.userData.crime1exp / 13)
    crime14perc = round(userData.userData.crime1exp / 15)
    crime15perc = round(userData.userData.crime1exp / 17)
    crime16perc = round(userData.userData.crime1exp / 21)

    if crime11perc >= 100:
        crime11perc = 100
    if crime12perc >= 100:
        crime12perc = 100
    if crime13perc >= 100:
        crime13perc = 100
    if crime14perc >= 100:
        crime14perc = 100
    if crime15perc >= 100:
        crime15perc = 100
    if crime16perc >= 100:
        crime16perc = 100

    functions.setCooldown()
    if userData.userData.crime1exp <= 500:

        return render(request, 'crime1/lowRank.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})

    if userData.userData.tempCd > 0:
        return render(request, 'crime1/cooldown.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
    else:
        functions.updateCooldown()
        functions.addExperience()

        getal = random.randint(0,100)

        if getal <= crime13perc:
            functions.addmoney(150)
            return render(request, 'crime1/1true.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
        else:
            return render(request, 'crime1/1false.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})


def klanten_telefoon(request):
    userData.userData.prepareData(userData.userData)
    crime11perc = round(userData.userData.crime1exp / 9)
    crime12perc = round(userData.userData.crime1exp / 11)
    crime13perc = round(userData.userData.crime1exp / 13)
    crime14perc = round(userData.userData.crime1exp / 15)
    crime15perc = round(userData.userData.crime1exp / 17)
    crime16perc = round(userData.userData.crime1exp / 21)

    if crime11perc >= 100:
        crime11perc = 100
    if crime12perc >= 100:
        crime12perc = 100
    if crime13perc >= 100:
        crime13perc = 100
    if crime14perc >= 100:
        crime14perc = 100
    if crime15perc >= 100:
        crime15perc = 100
    if crime16perc >= 100:
        crime16perc = 100

    functions.setCooldown()
    if userData.userData.crime1exp <= 750:

        return render(request, 'crime1/lowRank.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})

    if userData.userData.tempCd > 0:
        return render(request, 'crime1/cooldown.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
    else:
        functions.updateCooldown()
        functions.addExperience()

        getal = random.randint(0,100)

        if getal <= crime14perc:

            functions.addmoney(2000)
            return render(request, 'crime1/1true.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
        else:
            return render(request, 'crime1/1false.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})



def drugs(request):
    userData.userData.prepareData(userData.userData)
    crime11perc = round(userData.userData.crime1exp / 9)
    crime12perc = round(userData.userData.crime1exp / 11)
    crime13perc = round(userData.userData.crime1exp / 13)
    crime14perc = round(userData.userData.crime1exp / 15)
    crime15perc = round(userData.userData.crime1exp / 17)
    crime16perc = round(userData.userData.crime1exp / 21)

    if crime11perc >= 100:
        crime11perc = 100
    if crime12perc >= 100:
        crime12perc = 100
    if crime13perc >= 100:
        crime13perc = 100
    if crime14perc >= 100:
        crime14perc = 100
    if crime15perc >= 100:
        crime15perc = 100
    if crime16perc >= 100:
        crime16perc = 100

    functions.setCooldown()
    if userData.userData.crime1exp <= 1000:
        return render(request, 'crime1/lowRank.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})

    if userData.userData.tempCd > 0:
        return render(request, 'crime1/cooldown.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
    else:
        functions.updateCooldown()
        functions.addExperience()

        getal = random.randint(0,100)

        if getal <= crime15perc:

            functions.addmoney(5000)

            return render(request, 'crime1/1true.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
        else:
            return render(request, 'crime1/1false.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})


def container(request):
    userData.userData.prepareData(userData.userData)
    crime11perc = round(userData.userData.crime1exp / 9)
    crime12perc = round(userData.userData.crime1exp / 11)
    crime13perc = round(userData.userData.crime1exp / 13)
    crime14perc = round(userData.userData.crime1exp / 15)
    crime15perc = round(userData.userData.crime1exp / 17)
    crime16perc = round(userData.userData.crime1exp / 21)

    if crime11perc >= 100:
        crime11perc = 100
    if crime12perc >= 100:
        crime12perc = 100
    if crime13perc >= 100:
        crime13perc = 100
    if crime14perc >= 100:
        crime14perc = 100
    if crime15perc >= 100:
        crime15perc = 100
    if crime16perc >= 100:
        crime16perc = 100

    functions.setCooldown()

    if userData.userData.crime1exp <= 1500:

        return render(request, 'crime1/lowRank.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})

    if userData.userData.tempCd > 0:
        return render(request, 'crime1/cooldown.html',
                      {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
    else:
        functions.updateCooldown()
        functions.addExperience()

        getal = random.randint(0,100)

        if getal <= crime16perc:

            functions.addmoney(500000)

            return render(request, 'crime1/1true.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})
        else:
            return render(request, 'crime1/1false.html',
                          {'content': [crime11perc, crime12perc, crime13perc, crime14perc, crime15perc, crime16perc]})

