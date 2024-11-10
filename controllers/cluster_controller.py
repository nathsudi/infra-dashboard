from flask import Blueprint, jsonify, render_template, request, url_for
from services.data_service import get_clusters, get_host_by_serial_number, get_dynamic_cluster_data
from constants.routes import *

cluster_blueprint = Blueprint('cluster', __name__)

@cluster_blueprint.route(CLUSTERS_ROUTE)
def clusters():
    clusters_data = get_clusters()
    return render_template('clusters.html', clusters=clusters_data)

@cluster_blueprint.route(HOSTS_ROUTE + '/<serial_number>')
def hosts(serial_number):
    formated_serial_number=serial_number.split('(')[0]
    host_details = get_host_by_serial_number(formated_serial_number)
    if host_details:
        return render_template('hosts.html', host=host_details)
    else:
        return "Host not found", 404

@cluster_blueprint.route(CLUSTER_DYNAMIC_DATA)
def api_clusters_dynamic_data():
    cluster_name = request.args.get('cluster-name')
    if not cluster_name:
        return "Cluster name not provided", 400
    dynamic_data = get_dynamic_cluster_data(cluster_name)
    return jsonify(dynamic_data)