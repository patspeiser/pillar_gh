import yaml
import os
import requests

class Github:
    def __init__(self):
        self.config = self.get_config()['github']

    def get_config(self, path=None):
    	config_path = path if path else '../config.yml'
    	with open(config_path) as conf:
    		try:
    			config = yaml.safe_load(conf)
    		except Exception as e: 
    			print('Exception in Github.get_config', e)
    			return e
    	return config

    def make_request(self, url=None):
        if url:
            header = {}
            header['Authorization'] = self.config['auth']['token']
            response = requests.get(url, header)
            if response.status_code == 200:
                return response.json()
            else: 
                return response.raise_for_status()
        else:
            return 

    def get_organization_data(self, organization):
        org_data = {}
        org = organization if organization else 'no organization supplied'
        req_url = os.path.join(self.config['base_url'], self.config['orgs']['path'], org)
        print(req_url) 
        org = self.make_request(req_url)
        self.get_repos(org) 

    def get_repos(self, org):
        org = org if org else 'no org in get_repos'
        repos_url = org['repos_url']
        repos = self.make_request(repos_url)
        print('here') 
        repo_data = {}
        if repos:
            for repo in repos:
                repo['name'] = self.get_repo_data(repo)
                print(repo)

    def get_repo_data(self, repo):
        repo_config = self.config['orgs']['repos']
        print('REPO!', repo)
        desired_data = repo_config['endpoints'].keys()        
        for data in desired_data:
            datapoints = data + '_count'            
            print(datapoints)
            print(repo[datapoint])


G = Github()
data = G.get_organization_data('netflix')
print(data)


