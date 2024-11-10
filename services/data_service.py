import json

from services.api_client import find_valid_fqdn, get_compute_hosts

def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_clusters():
    clusters_data = load_json_data('data/cluster-info.json')
    return clusters_data['clusters']

def get_host_by_serial_number(serial_number):
    print(serial_number)
    hosts_data = load_json_data('data/hosts-info.json')
    return next((host for host in hosts_data['hosts'] if host['serialNumber'] == serial_number), None)


def get_dynamic_cluster_data(cluster_name):
    cluster_fqdn=find_valid_fqdn(cluster_name)
    print(f'cluster fqdn passed to data layer is: ${cluster_fqdn}')
    if(cluster_fqdn == None):
        dynamic_data = {
            "cluster-fqdn":"unreachable",
            "orch-ver": "...",
            "cluster-runtime": "...",
            "edge-nodes": "..."
        }
    else:
        host_data = get_compute_hosts(cluster_fqdn)

        serial_numbers_list, version = get_hosts_data(host_data)
        print(serial_numbers_list,version)
        dynamic_data = {
                "cluster-fqdn":cluster_fqdn,
                "orch-ver": version,
                "cluster-runtime": "...",
                "edge-nodes": serial_numbers_list
            }
    return dynamic_data

def get_hosts_data(host_json_data):
    data_dict=host_json_data
    serial_numbers = []
    final_json = []
    version_number = None

    # Iterate through the hosts and extract the required information
    for host in data_dict['hosts']:
        serial_number = host['serialNumber']
        onboarding_status_message = host['onboardingStatus']['message']
        os_details= host['instance']['os']
        prodct_name=host['productName']
        uuid=host['uuid']
        
        # Extract the version number from the "name" field
        os_name = host['instance']['os']['name']
        version_start = os_name.find(" (") + 2 
        version_end = os_name.find(")", version_start) 
        if version_start != -1 and version_end != -1:
            version_number = os_name[version_start:version_end]
        
        # Append the serial number to the list
        serial_numbers.append(serial_number+'('+onboarding_status_message+')')
        
        # Append the extracted information to the final JSON object
        final_json.append({
            "serialNumber": serial_number,
            "onboardingStatus": onboarding_status_message,
            "osDetails": os_details,
            "productName":prodct_name,
            "uuid":uuid

        })

    print(final_json)
    update_or_append_host_data(final_json)
    
    return serial_numbers, version_number

def update_or_append_host_data(new_host_data):
    hosts_file_path = 'data/hosts-info.json'

    try:
        with open(hosts_file_path, 'r') as file:
            hosts_info = json.load(file)
    except FileNotFoundError:
        hosts_info = {'hosts': []}

    for new_host in new_host_data:
        serial_number = new_host['serialNumber']
        existing_host = next((host for host in hosts_info['hosts'] if host['serialNumber'] == serial_number), None)
        if existing_host:
            existing_host.update(new_host)
        else:
            hosts_info['hosts'].append(new_host)

    with open(hosts_file_path, 'w') as file:
        json.dump(hosts_info, file, indent=4)