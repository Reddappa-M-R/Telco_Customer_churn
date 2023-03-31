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
                sh 'python3 train.py'
            }
        }

        stage('Evaluate model') {
            steps {
                sh 'python3 evaluate.py'
            }
        }

        stage('Deploy model') {
            steps {
                sh 'python3 streamlit run App.py'
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
