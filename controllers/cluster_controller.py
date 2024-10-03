from flask import Blueprint, jsonify, render_template, url_for
from services.data_service import get_clusters, get_host_by_serial_number, get_dynamic_cluster_data
from constants.routes import CLUSTERS_ROUTE, HOSTS_ROUTE

cluster_blueprint = Blueprint('cluster', __name__)

@cluster_blueprint.route(CLUSTERS_ROUTE)
def clusters():
    clusters_data = get_clusters()
    return render_template('clusters.html', clusters=clusters_data)

@cluster_blueprint.route(HOSTS_ROUTE + '/<serial_number>')
def hosts(serial_number):
    host_details = get_host_by_serial_number(serial_number)
    if host_details:
        return render_template('hosts.html', host=host_details)
    else:
        return "Host not found", 404

@cluster_blueprint.route('/api/clusters/dynamic')
@cluster_blueprint.route('/api/clusters/dynamic')
def api_clusters_dynamic_data():
    dynamic_data = get_dynamic_cluster_data()
    # Construct the full URLs for the edge nodes
    for cluster in dynamic_data:
        cluster['edge-nodes'] = [
            {
                'id': edge_node,
                'url': url_for('cluster.hosts', serial_number=edge_node)
            }
            for edge_node in cluster['edge-nodes']
        ]
    return jsonify(dynamic_data)