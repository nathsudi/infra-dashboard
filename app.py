from flask import Flask, render_template
import json

#TODO: 1. move the routing to controller layer
#TODO: 2. move the data processing to service like layer
#TODO: 3. move route names to constant file
app = Flask(__name__)

# Load the data from JSON files
def load_json_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

@app.route('/')
def clusters():
    clusters_data = load_json_data('data/cluster-info.json')
    return render_template('clusters.html', clusters=clusters_data['clusters'])

@app.route('/hosts/<serial_number>')
def hosts(serial_number):
    hosts_data = load_json_data('data/hosts-info.json')
    # Find the host with the matching 'serial_number' value
    host_details = next((host for host in hosts_data['hosts'] if host['host-serial'] == serial_number), None)
    if host_details:
        return render_template('hosts.html', host=host_details)
    else:
        return "Host not found", 404

if __name__ == '__main__':
    app.run(debug=True)