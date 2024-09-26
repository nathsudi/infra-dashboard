from flask import Flask
from controllers.cluster_controller import cluster_blueprint

app = Flask(__name__)
app.register_blueprint(cluster_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)