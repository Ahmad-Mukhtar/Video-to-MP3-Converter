# Video to MP3 Converter Service


This is a backend service for converting videos to MP3 format using the Python Flask framework. The service leverages a microservices architecture for scalability and runs as a Docker container within a Kubernetes cluster. It offers various features including authentication, communication gateway, file conversion, MongoDB storage with support for large files (using GridFS), and user notification.

## Features

- **Scalability**: Seamlessly scale the service by deploying it as a pod within a Kubernetes cluster.
- **Authentication**: Secure user authentication with JWT.
- **Gateway Service**: Provides an interface for external connections and frontend communication.
- **File Conversion**: Converts video files to MP3 format.
- **Large File Support**: Utilizes the GridFS specification for storing and handling large files.
- **Database Storage**: Stores converted files in a MongoDB database for later retrieval.
- **Notification Service**: Notifies users via email when the converted file is ready for download.
- **Microservices Architecture**: Microservices communicate with each other through API calls and RabbitMQ for seamless integration.

## Prerequisites

Before running this service, make sure you have the following:

- Docker installed
- Kubernetes cluster set up (for scaling)
- MongoDB instance for storing converted files (with GridFS support)
- RabbitMQ for inter-microservice communication


## Installation

Follow these steps to deploy the service:

1. Clone this repository.
2. Build the Docker image: `docker build -t video-to-mp3-converter .`
3. Add tag to the image using docker tag <'Your Image tag'>
4. Deploy the image to docker hub using docker push <'Your Image tag'>
5. Deploy the service to your Kubernetes cluster by adding yourusername/imagetag inside .yaml file..

## Configuration

Configure the service by modifying the relevant configuration files:

- `auth-deploy.yaml`: Specify authentication settings and other service configurations.
- `deploy.yaml`: Configure the converter configurations.
- `gateway-deploy.yaml`: Configure the communication gateway.
- `notification.yaml`: Configure the email notification service.
- `statefulset.yaml`: Set up RabbitMQ for communication between microservices.


This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Special thanks to the open-source community for their contributions and support.
