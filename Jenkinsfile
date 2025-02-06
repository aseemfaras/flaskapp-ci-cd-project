pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "aseemfaras/flask-webapp:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aseemfaras/flaskapp-ci-cd-project.git'
            }
        }

        stage('Build and Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest'  // If you have tests
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Docker Push') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials', url: '']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 $DOCKER_IMAGE'
            }
        }

         stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
            }
    }
}
