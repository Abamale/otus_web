pipeline {
    agent any

    environment {
        ENV_VARS = sh(script: 'grep -v "^#" .env | xargs', returnStdout: true).trim()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Start Containers') {
            steps {
                echo "Starting docker compose services..."
                sh '''
                set -e
                export ${ENV_VARS}
                docker compose down || true
                docker compose up -d

