from django.shortcuts import render
from django.http import HttpResponse
import mysql


# Create your views here.
def index(request):
    return render(request, 'crime3/home.html')


def brink(request):

    db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 db="dev6")
    username = request.GET['username']
    print(username)


    # cur = db.cursor()
    # cur.execute("SELECT suspect.rank FROM suspect WHERE username = '" + username + "'")
    # for row in cur.fetchall():
    #     if row[2] == 1:
    #         return HttpResponse("<h2>It works!</h2>")
    #     else:
    #         return HttpResponse("<h2>It failed</h2>")

    db.close()


# return HttpResponse("<h2>HEY!</h2>")

def tankstation(request):
    # TODO: Implement logic for robbery
    return HttpResponse("<h2>Tankstation overvallen!</h2>")


def woning(request):
    # TODO: Implement logic for robbery
    return HttpResponse("<h2>Woning overvallen!</h2>")


def kind(request):
    # TODO: Implement logic for robbery
    return HttpResponse("<h2>Kind overvallen!</h2>")
