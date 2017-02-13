import threading
import time
import mysql.connector
import multiprocessing

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="root",
                                     db="dev6")

        while True:
            sql = "SELECT * FROM suspect_cd WHERE cooldown > 0"
            c = db.cursor()
            c.execute(sql)
            for rows in c.fetchall():
                c2 = db.cursor()
                c2.execute("UPDATE suspect_cd SET cooldown = " + str(rows[2] - 1) + " WHERE username = '" + rows[0] + "' AND cId = " + str(rows[1]))
                db.commit()
            time.sleep(1)


class cooldownStuff():

    def startCooldown(self):
        t = ThreadingExample
        p = multiprocessing.Process(target=ThreadingExample.run(t))
        p.start()