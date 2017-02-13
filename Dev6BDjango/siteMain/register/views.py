from django.shortcuts import render
from siteMain import async

def index(request):

    return render(request,'register/register.html')
    # username = request.GET['username']
    # password = request.GET['password']
    # password2 = request.GET['password2']
    # amount = 0
    # db = mysql.connector.connect(host="145.24.222.175",
    #                              user="suspect",
    #                              passwd="dev6",
    #                              db="dev6")
    #
    # cur = db.cursor()
    # if (password == password2):
    # # Use all the SQL you like
    #     cur.execute("INSERT INTO suspect(username,password,rank) VALUES('" + username + "','" + password + "','NOOBIE')")
    #     db.close()
    #     return render(request, 'register/register.html')
    # # print all the first cell of all the rows
    # else:
    #     return render(request,'register/register2.html')




