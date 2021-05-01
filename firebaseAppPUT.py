
from firebase import firebase
from datetime import datetime as date

class Put():

    def __init__(self,firebase,args=['empty',date.today().strftime('%Y-%m-%d')]):
        self.firebase = firebase
        self.args = args

    def performPut(self,field,toUpdate):

        result = self.firebase.put("/user",field,toUpdate)
        print("Database updated.")