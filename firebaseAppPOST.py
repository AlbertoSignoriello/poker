
from firebase import firebase
from datetime import datetime as date
from datetime import timedelta

class Post():

	def __init__(self,firebase,args=['empty',date.today().strftime('%Y-%m-%d')]):
		self.firebase = firebase
		self.args = args

	def performPost(self):

		print('\n------------------NEW ACTION------------------')
		
		for i in range(1):

			data = {
				'food': self.args[0],
				'expiring': self.args[1]
			}

			result = self.firebase.post("/new_game",data)

		print("\nElement added.")