import requests
import json


class quiz:
	def __init__(self,response):
		self.get_response = response
		response = requests.get("https://opentdb.com/api.php?amount=10")
		print(response.status_code)
		dict_data = json.loads(response.text)
		json.dump(dict_data,open('qa1/raw/quiz.json','w'))
		print('data wirtten into a file')
	def __call__(self,request,*args,**kwargs):
		response = self.get_response(request)
		print('I m a call')
		return response