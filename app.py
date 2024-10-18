from flask import Flask
from controllers.cluster_controller import cluster_blueprint
from services.infra_repo_service import initialize_cluster_info

app = Flask(__name__)
app.register_blueprint(cluster_blueprint)

initialized = False

@app.before_request
def initialize():
    global initialized
    if not initialized:
        initialize_cluster_info()
        initialized = True


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)