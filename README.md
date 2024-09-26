# infra-dashboard

## Cluster and Host Management Dashboard

This Flask application provides a web interface for managing and viewing clusters and their associated host details. It uses a service layer to interact with data sources, which currently fetch data from JSON files but can be extended to work with APIs or databases.

## Dockerization

This application can be easily run inside a Docker container. Follow the steps below to build and run the application using Docker.

### Prerequisites

- Docker installed on your machine. For installation instructions, refer to the [official Docker documentation](https://docs.docker.com/get-docker/).

### Building the Docker Image

To build the Docker image for the application, navigate to the root directory of the project where the `Dockerfile` is located and run the following command:

```bash
docker build -t infra-dash-app .
```

