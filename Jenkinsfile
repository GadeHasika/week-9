 pipeline { 
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
               bat "docker build -t quiz-app:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                bat 'docker login -u hasikagade123 -p Hasika@123'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
               bat 'docker tag quiz-app:v1 hasikagade123/quiz:hasika1' 
                bat 'docker push hasikagade123/quiz:hasika1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes..."
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }

    post {
        success {
            echo "Deployment successful! quiz App is now live on Kubernetes."
        }
        failure {
            echo "Deployment failed. Check Jenkins logs for errors."
        }
    }

}









