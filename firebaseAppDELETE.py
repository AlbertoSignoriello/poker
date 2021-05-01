
from firebase import firebase
from firebaseAppGETpd import *

class Delete():
    
    def __init__(self,firebase,element=''):
        self.firebase = firebase
        self.element = element
        if len(element)>0:
            self.element = element[0]

    def performDelete(self):

        print('\n------------------NEW ACTION------------------')
        getter = Get(self.firebase)
        key = ''
        self.result = self.firebase.get("/user",'')
        if bool(self.result)!=True:
            print("\nEmpty database.")
        else:
            if len(self.element)>0:
                for k,v in self.result.items():
                    if self.element in v['food']:
                        key = k
                        print(self.element + ' cancellato!')
                result = self.firebase.delete("/user/"+key,'') #It removes the given element
                getter.performGet(flag=False)
                print("\nElement deleted.")
            else:
                result = self.firebase.delete("/user",'')
                print("\nDatabase deleted.")