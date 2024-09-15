from flask import Blueprint, render_template
from services.data_service import get_clusters, get_host_by_serial_number
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