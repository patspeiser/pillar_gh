# patspeiser, pillar, github

### Install 
1. `pip install -r requirements.txt`
2. `. env/bin/activate`
3. `cd github_pillar/pillar `
4. `python manage.py runserver`

### Setup
1. Add your github token to config.yml auth token field

or 

1. Set an environment variable GH_TOKEN 

### In browser
1. https://localhost:8000/orgs/<str:org_name>

`ex https://localhost:8000/orgs/patspeiser` 