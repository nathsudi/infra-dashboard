import requests

# Keycloak credentials and client configuration
KEYCLOAK_CLIENT_ID = 'system-client'
KEYCLOAK_USERNAME = 'all-groups-example-user'
KEYCLOAK_PASSWORD = 'ChangeMeOn1stLogin!'
KEYCLOAK_SCOPE = 'openid profile email groups'

# Function to get the API token
def get_api_token(cluster_fqdn):
    keycloak_url = f'https://keycloak.{cluster_fqdn}/realms/master/protocol/openid-connect/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'password',
        'client_id': KEYCLOAK_CLIENT_ID,
        'username': KEYCLOAK_USERNAME,
        'password': KEYCLOAK_PASSWORD,
        'scope': KEYCLOAK_SCOPE
    }
    response = requests.post(keycloak_url, headers=headers, data=data, verify=False)
    response.raise_for_status() 
    return response.json().get('access_token')

# Function to get the compute hosts data
def get_compute_hosts(cluster_fqdn):
    api_token = get_api_token(cluster_fqdn)
    if api_token:
        headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {api_token}'
        }
        compute_hosts_url = f'https://iaas.{cluster_fqdn}/edge-infra.orchestrator.apis/v1/compute/hosts'
        response = requests.get(compute_hosts_url, headers=headers, verify=False)
        response.raise_for_status()  
        return response.json()
    return None


CLUSTER_FQDN='validation5.espd.infra-host.com'
print(f'{get_api_token(CLUSTER_FQDN)}')
print(f'{get_compute_hosts(CLUSTER_FQDN)}')