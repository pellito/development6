
from django.contrib.auth.models import User
import time
import mysql.connector


def cooldown():
    while True:
        db = mysql.connector.connect(host="localhost",
                                 user="root",
                                 passwd="root",
                                 db="dev6")
        cur = db.cursor()
        cur.execute(
            "SELECT * FROM suspect_cd WHERE cooldown > 0")
        for row in cur.fetchall():
            cd = row[2]
            if (cd > 0 and cd < 10):
                cd = 0
            else:
                cd = cd - 10
            cur2 = db.cursor()
            cur2.execute(
                "UPDATE suspect_cd SET cooldown = " + str(cd) + " WHERE username = '" + str(row[0]) + "' AND cId = " + str(
                    row[1]))
            db.commit()
        time.sleep(10)


# cur = cool.db.cursor()
#     cur.execute(
#         "SELECT * FROM suspect_cd WHERE cooldown > 0")
#     for row in cur.fetchall():
#         cd = row[2]
#         if (cd > 0 and cd < 10):
#             cd = 0
#         else:
#             cd = cd - 10
#         cur2 = cool.db.cursor()
#         cur2.execute(
#             "UPDATE suspect_cd SET cooldown = " + str(cd) + " WHERE username = '" + str(row[0]) + "' AND cId = " + str(
#                 row[1]))
#         cool.db.commit()
#     time.sleep(10)
