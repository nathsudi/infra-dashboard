import json

def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_clusters():
    clusters_data = load_json_data('data/cluster-info.json')
    return clusters_data['clusters']

def get_host_by_serial_number(serial_number):
    hosts_data = load_json_data('data/hosts-info.json')
    return next((host for host in hosts_data['hosts'] if host['host-serial'] == serial_number), None)