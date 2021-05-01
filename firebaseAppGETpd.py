
from firebase import firebase
import pandas as pd
from datetime import datetime as date

def createDF(result,filt,flag):
	if (bool(result)!=True and flag):
		print("Empty database! Add some food.")
	else:
		df = pd.DataFrame.from_dict(result).transpose().reset_index().drop(['index'],axis=1)
		df['expiring'] = pd.to_datetime(df['expiring'])
		print('\nALL THE FOOD:\n')
		print(df)
		print('\n\n')
		foodClassifier(df)

def foodClassifier(df):
	today = date.today().strftime('%Y-%m-%d')
	good = limit = bad = pd.DataFrame()

	good = df[df['expiring']>today]
	print('GOOD FOOD:\n')
	print(good)
	print('\n\n')

	limit = df[df['expiring']==today]
	print('LIMIT FOOD:\n')
	print(limit)
	print('\n\n')

	bad = df[df['expiring']<today]
	print('BAD FOOD:\n')
	print(bad)
	print('\n')


class Get():

	def __init__(self,firebase):
		self.firebase = firebase

	def performGet(self,filt=[],flag=True):

		if flag:
			print('\n------------------NEW ACTION------------------')
		
		# firebase = firebase.FirebaseApplication(self.url,None)
		self.result = self.firebase.get("/user",'')
		createDF(self.result,filt,flag)
		# good.to_csv('/Users/edoardoroba/Desktop/edo/PYTHON/resultFOOD/goodFood.csv',index=False)
		# limit.to_csv('/Users/edoardoroba/Desktop/edo/PYTHON/resultFOOD/limitFood.csv',index=False)
		# bad.to_csv('/Users/edoardoroba/Desktop/edo/PYTHON/resultFOOD/badFood.csv',index=False)
