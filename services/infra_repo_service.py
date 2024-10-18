import requests
import yaml
import json
import os
from constants.repo_config import *

def fetch_yaml_file():
    url = f'https://raw.githubusercontent.com/{GITHUB_REPO}/{BRANCH}/{YAML_FILE_PATH}'
    headers = {'Authorization': f'token {KEY}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    return response.text

def convert_yaml_to_json(yaml_content):
    yaml_data = yaml.safe_load(yaml_content)
    
    clusters = []
    for key, value in yaml_data.get('cluster', {}).items():
        cluster_info = {
            "orch-plat": value.get('type'),
            "setup": "Internal",
            "cluster-name": key,
            "jump-host": "x.x.x.x"  
        }
        clusters.append(cluster_info)
    
    json_content = {"clusters": clusters}
    
    with open(JSON_FILE_PATH, 'w') as json_file:
        json.dump(json_content, json_file, indent=4)

def initialize_cluster_info():
    yaml_content = fetch_yaml_file()
    convert_yaml_to_json(yaml_content)