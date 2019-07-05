import yaml
import os
import requests

class Github:
    def __init__(self):
        print('Github class initialized')
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
        #w/ req url check for token then make request
        if url:
            header = {}
            token = os.environ['GH_TOKEN'] if 'GH_TOKEN' in os.environ else self.config['auth']['token']

            #get token for req
            if token:
                header['Authorization'] = token
                response = requests.get(url, header)
            else: 
                return

            #handle res
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
        org = self.make_request(req_url)
        return self.get_repos(org) 

    def get_repos(self, org):
        print('org', org)
        repos_url = org['repos_url']
        repos = self.make_request(repos_url)
        repo_data = {}
        if repos:
            for repo in repos:
                repo['name'] = self.get_repo_data(repo)
                print(repo)

    def get_repo_data(self, repo):
        repo_config = self.config['orgs']['repos']
        desired_data = repo_config['endpoints'].keys()        
        repo_data = {}
        for data in desired_data:
            datapoint = data + '_count'            
            repo_id = repo['id']
            repo_data[repo_id][datapoint] = repo[datapoint]

        return repo_data 