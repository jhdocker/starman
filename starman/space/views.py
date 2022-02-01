from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
import requests

def people_in_space(people):
	if people['message'] =='success':
		return people
	else:
		print(f'there seems to be a problem with the astronauts endpoint')

def get_iss_position(position):
	if(position['message'] == 'success'):
		return position
	else:
		print(f'there seems to be a problem with the position endpoint')

def index(request):

	template = loader.get_template('space/index.html')
	latest_question_list = Question.objects

	people = requests.get("http://api.open-notify.org/astros.json").json()
	iss = requests.get("http://api.open-notify.org/iss-now.json").json()
	context = {
		'people': people_in_space(people),
		'iss': get_iss_position(iss)
	}
	return render(request, 'space/index.html', context)
