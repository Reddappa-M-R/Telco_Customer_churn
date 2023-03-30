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
                sh ' sudo chown -R jenkins:jenkins /home/jenkins && pip install -r requirements.txt'
            }
        }

        stage('Train model') {
            steps {
                sh 'python train.py'
            }
        }

        stage('Evaluate model') {
            steps {
                sh 'python evaluate.py'
            }
        }

        stage('Deploy model') {
            steps {
                sh 'python deploy.py'
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
