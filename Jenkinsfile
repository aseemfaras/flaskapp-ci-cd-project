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
        // Optionally, stop any container running on port 5000
        sh 'docker ps -q --filter "publish=5000" | xargs -r docker rm -f'
        // Now run the new container
        sh 'docker run -d -p 5000:5000 aseemfaras/flask-webapp:latest'
            }
        }


        stage('Deploy to Kubernetes') {
    steps {
        // If using a kubeconfig stored as a Jenkins secret:
        withCredentials([file(credentialsId: 'kubeconfig-file', variable: 'KUBECONFIG_FILE')]) {
            // Copy the kubeconfig to the default location
            sh 'mkdir -p ~/.kube && cp $KUBECONFIG_FILE ~/.kube/config'
        }
        // Apply the Kubernetes deployment
        sh 'kubectl apply -f k8s/deployment.yaml'
    }
}

    }
}
