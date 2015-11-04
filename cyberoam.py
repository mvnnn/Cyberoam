#!/usr/bin/python2.7
import sys
from urllib import urlencode
from urllib2 import urlopen
from time import sleep
from os import system
import subprocess
import pynotify

''''' this cyberoam working on DA-IICT because i use my collage IP
      even if you close terminal but process not kill'''''


cyberoamIP = "10.100.56.55"   #The IP of the Cyberoam site of DA-IICT,
cyberoamPort = "8090"   #PORT number
neverQuit=True
sleeptime=3600
pynotify.init("Cyberoam")
URL = 'https://'+cyberoamIP+":"+cyberoamPort+'/'+'httpclient.html'


n = pynotify.Notification("Cyberoam Login with valid DA_id and password")
n.show()
DA_id = raw_input("Enter your ID: ")
passwordd = raw_input("password: ")


def forLogin(user,passs):
        params = urlencode({'mode': 191, 'username': user, 'password': passs})
        res = urlopen(URL, params)
        aa=res.read()
        print "login success"
        return aa


def forLogout(user):
        params = urlencode({'mode': 193, 'username': user})
        res = urlopen(URL, params)
        aa=res.read()
        print "logout success"
        return aa


def logout():
        info = forLogout(DA_id)
        if 'off' in info:
            n = pynotify.Notification("logout")
            n.show()
            exit()


if __name__ == "__main__":
    relogin=False
    try:

        if "login" in sys.argv:
            info=forLogin(DA_id,passwordd)
            if "could not" in info:
                n = pynotify.Notification("enter valid DA_id and password and run file")
                n.show()
                exit()
            elif "Maximum" in info:
                n = pynotify.Notification("Maximum data limit")
                n.show()
                exit()
            elif "exceeded" in info:
                n = pynotify.Notification("data limit exceeded")
                n.show()
                exit()
            elif "successfully logged in" in info :
                n = pynotify.Notification("login success")
                n.show()
                relogin=True
                print "Press Ctrl + C to logout"

            else:
                print "Request Failed, Please try again later"


            if relogin:
                min=0;
                ss=0
                while True:
                   if min !=3600 :
                    sleep(sleeptime)
                    min=3600
                    ss=1

                    if ss==1:
                     min=0
                     ss=0
                     print "Logging in again"
                     n = pynotify.Notification("enter valid DA_id and password and run file")
                     n.show()
                     data = forLogin(DA_id,passwordd)



    except KeyboardInterrupt:
        logout()
        exit()
    except Exception as e:
        print e

    if "logout" in sys.argv:
        logout()



