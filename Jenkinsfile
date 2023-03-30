pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train model') {
            steps {
                sh 'train.py'
            }
        }

        stage('Evaluate model') {
            steps {
                sh 'evaluate.py'
            }
        }

        stage('Deploy model') {
            steps {
                sh 'deploy.py'
            }
        }
    }

    post {
        always {
            junit 'test-results.xml'
            archiveArtifacts 'model.pkl'
        }
    }
}
