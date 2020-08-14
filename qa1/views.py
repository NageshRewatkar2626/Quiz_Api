from django.shortcuts import render
import json
from Quiz_Api.settings import quiz_file
from qa1.models import Quiz, Question, Answer
from django.contrib import messages
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

def ShowIndex(request):
	d = json.loads (open(quiz_file).read())
	que_dict={}
	que_dict.update(d)
	questions={'q1':que_dict['results'][0]['question'],'q2':que_dict['results'][1]['question'],
			   'q3':que_dict['results'][2]['question'],'q4':que_dict['results'][3]['question'],
			   'q5':que_dict['results'][4]['question'],'q6':que_dict['results'][5]['question'],
			   'q7':que_dict['results'][6]['question'],'q8':que_dict['results'][7]['question'],
			   'q9':que_dict['results'][8]['question'],'q10':que_dict['results'][9]['question']
			  }
	correct_ans={'a1':que_dict['results'][0]['correct_answer'],'a2':que_dict['results'][1]['correct_answer'],
			   	 'a3':que_dict['results'][2]['correct_answer'],'a4':que_dict['results'][3]['correct_answer'],
			   	 'a5':que_dict['results'][4]['correct_answer'],'a6':que_dict['results'][5]['correct_answer'],
			   	 'a7':que_dict['results'][6]['correct_answer'],'a8':que_dict['results'][7]['correct_answer'],
			   	 'a9':que_dict['results'][8]['correct_answer'],'a10':que_dict['results'][9]['correct_answer']}
	for x in que_dict['results']:
		in_ans=x['incorrect_answers']
	print(in_ans,end=',')

		
	return render(request,'quiz.html',{'ques':questions,'c_ans':correct_ans})

