pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'aseemfaras/flask-webapp'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                git 'https://github.com/aseemfaras/flaskapp-ci-cd-project.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
        }
    }
}
