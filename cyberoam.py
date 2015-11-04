#!/usr/bin/python2.7
import sys
from urllib import urlencode
from urllib2 import urlopen
from time import sleep
from os import system
from bs4 import BeautifulSoup
import subprocess
import pynotify

''''' this cyberoam working on DA-IICT because i use DA IP
      even if you close terminal but process will running'''''


cyberoamIP = "10.100.56.55"   #The IP of the Cyberoam site of DA-IICT,
cyberoamPort = "8090"   #PORT number
neverQuit=True
sleeptime=10
pynotify.init("Cyberoam")
URL = 'https://'+cyberoamIP+":"+cyberoamPort+'/'+'httpclient.html'


n = pynotify.Notification("Cyberoam Login with valid DA_id and password")
n.show()
DA_id = raw_input("Enter your ID: ")
passwordd = raw_input("password: ")


def forprocide():
    URLLIVE='https://'+cyberoamIP+":"+cyberoamPort+'/live?'+'mode=192&username='+str(DA_id)
    info=urlopen(URLLIVE).read()
    bs = BeautifulSoup(info)
    data= bs.html.body
    ss=1

    if "exceeded" in data :
        ss=0

    elif "login again" in data:
        ss=0
    else:
        ss=1
    return ss

def Timerforlogin():
    sleep(sleeptime)

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


def loginLogout():
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
                #print forprocide()

            else:
                print "this Cyberoam don't recognise your error..please try again"



            if relogin:
                total=0
                while forprocide() != 0:
                 Timerforlogin()
                 total +=10
                 if(total==3600):
                   break


                if total==3600:
                 total=0
                 sys.argv="login"
                 loginLogout()

                else :
                    logout()
                    exit()




    except KeyboardInterrupt:
        logout()
        exit()
    except Exception as e:
        print e

    try :
        if "logout" in sys.argv:
            logout()
            exit()
    except Exception as e:
        print e


if __name__ == "__main__":

    loginLogout()