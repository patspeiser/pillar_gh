from django.http import HttpResponse
import requests

def index(request):
	return HttpResponse('github index')

def name(request, name):
	return HttpResponse('github name', name)

