# Flask Web Application with CI/CD Pipeline

This project is a Flask web application that demonstrates how to implement a Continuous Integration and Continuous Deployment (CI/CD) pipeline using Jenkins, Docker, Kubernetes, and GitHub. The application is a simple Flask app exposed on port 5000.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Build the Docker Image](#2-build-the-docker-image)
  - [3. Push the Docker Image to Docker Hub](#3-push-the-docker-image-to-docker-hub)
  - [4. Set Up Kubernetes](#4-set-up-kubernetes)
  - [5. Access the Application](#5-access-the-application)
- [CI/CD Pipeline](#cicd-pipeline)
  - [1. Jenkins Setup](#1-jenkins-setup)
  - [2. Pipeline Stages](#2-pipeline-stages)
- [Deployment](#deployment)
  - [1. Kubernetes Deployment](#1-kubernetes-deployment)
  - [2. Port Forwarding](#2-port-forwarding)
- [Troubleshooting](#troubleshooting)

## Overview

This project is designed to demonstrate how to automate the deployment of a Flask web application using modern CI/CD practices. The CI/CD pipeline is configured using Jenkins to automate tasks such as:

- Code checkout from GitHub
- Building a Docker image of the application
- Pushing the image to Docker Hub
- Deploying the application to Kubernetes

## Technologies Used

- **Flask**: A lightweight Python web framework to create the application.
- **Docker**: Containerizes the application and its dependencies.
- **Kubernetes**: Manages the deployment of the application in a containerized environment.
- **Jenkins**: Automates the CI/CD pipeline.
- **GitHub**: Source control for managing the application code.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- Docker
- Kubernetes
- Jenkins
- Git
- A GitHub account
- Docker Hub account

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/aseemfaras/flaskapp-ci-cd-project.git
cd flaskapp-ci-cd-project
