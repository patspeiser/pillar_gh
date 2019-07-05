from django.http import HttpResponse
import requests
import classes.github

def index(request):
	return HttpResponse('/')

def name(request, name):
	github = classes.github.Github()
	orgs = github.get_organization_data(name)
	return orgs
