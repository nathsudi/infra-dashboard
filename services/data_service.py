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

def get_dynamic_cluster_data():
    # Simulated dynamic data returned from an API
    dynamic_data = [
        {
            "orch-ver": "v24.08.1",
            "cluster-runtime": "14d",
            "edge-nodes": ["jHNMF3", "kHNMF4"]
        },
        {
            "orch-ver": "v24.09.0",
            "cluster-runtime": "30d",
            "edge-nodes": ["1MNR45"]
        },
        {
            "orch-ver": "v24.08.0",
            "cluster-runtime": "30d",
            "edge-nodes": ["1MNR45"]
        },
        {
            "orch-ver": "v24.11.0",
            "cluster-runtime": "30d",
            "edge-nodes": ["1MNR45"]
        },
        {
            "orch-ver": "v24.11.0",
            "cluster-runtime": "30d",
            "edge-nodes": ["1MNR45"]
        }
        
    ]
    return dynamic_data