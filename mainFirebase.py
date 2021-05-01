from firebaseAppDELETE import *
from firebaseAppGETpd import *
from firebaseAppPOST import *
from firebaseAppPUT import *
from firebase import firebase

url = "https://firstcreation-25776-default-rtdb.firebaseio.com/"
firebase = firebase.FirebaseApplication(url,None)

pastAction = ""

while True:
    
    fileRead = open("testoFirebase.txt",'r')
    action = fileRead.read()
    fileRead.close()
    args = action.split()[1:]
    #print(args)
    if action!=pastAction:

    # print(action)
        pastAction = action

        if 'INSERISCI' in action.upper():
            fbObj = Post(firebase,args)
            fbObj.performPost()

        if 'MOSTRA' in action.upper():
            filters = action.split()
            fbObj = Get(firebase)
            if len(action)==1:
                fbObj.performGet()
            else:
                fbObj.performGet(filters)

        if 'PUT' in action.upper():
            fbObj = Put(firebase,args)
            fbObj.performPut(field,toUpdate)

        if 'ELIMINA' in action.upper():
            fbObj = Delete(firebase,args)
            fbObj.performDelete()