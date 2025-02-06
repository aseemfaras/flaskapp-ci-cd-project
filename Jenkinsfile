pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "aseemfaras/flask-webapp:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/aseemfaras/flaskapp-ci-cd-project.git'

            }
        }

        stage('Build and Test') {
    steps {
        sh 'python3 -m pip install --break-system-packages -r requirements.txt'
        sh 'pytest'
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
}
