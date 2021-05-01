from firebaseAppDELETE import *
from firebaseAppGETpd import *
from firebaseAppPOST import *
from firebaseAppPUT import *
from firebase import firebase

# url = "https://firstcreation-25776-default-rtdb.firebaseio.com/"
url = 'https://esempio-5dd51.firebaseio.com/'
firebase = firebase.FirebaseApplication(url,None)

pastAction = ""

print("PARTITA A POKER.")

fbObj = Post(firebase,args)

action = "prova"

while action!="fine":

    fileRead = open("puntata.txt",'r')
    action = fileRead.read()
    fileRead.close()
    # args = action.split()[1:]
    # #print(args)
    # if action!=pastAction:

    # # print(action)
    #     pastAction = action

    #     if 'INSERISCI' in action.upper():
    #         fbObj = Post(firebase,args)
    #         fbObj.performPost()

    #     if 'MOSTRA' in action.upper():
    #         filters = action.split()
    #         fbObj = Get(firebase)
    #         if len(action)==1:
    #             fbObj.performGet()
    #         else:
    #             fbObj.performGet(filters)

    #     if 'PUT' in action.upper():
    #         fbObj = Put(firebase,args)
    #         fbObj.performPut(field,toUpdate)

fbObj = Delete(firebase,args)
fbObj.performDelete()