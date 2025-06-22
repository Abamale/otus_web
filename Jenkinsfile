pipeline {
    agent any

    environment {
        // Читаем .env однажды и делаем переменные доступными в скриптах
        ENV_VARS = sh(script: "cat .env | xargs", returnStdout: true).trim()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Start Containers') {
            steps {
                echo "Starting docker-compose services..."
                sh '''
                export ${ENV_VARS}
                docker-compose up -d
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python requirements..."
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                echo "Running API tests..."
                sh '''
                export ${ENV_VARS}
                pytest tests/tests_api/ --alluredir=allure-results/api
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                echo "Running UI tests..."
                sh '''
                export ${ENV_VARS}
                pytest tests/ --ignore=tests/tests_api --alluredir=allure-results/ui
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                echo "Publishing Allure reports..."
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [
                        [path: 'allure-results/api'],
                        [path: 'allure-results/ui']
                    ]
                ])
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh '''
            export ${ENV_VARS}
            docker-compose down
            '''
            archiveArtifacts artifacts: '**/allure-results/**/*.*', allowEmptyArchive: true
        }
    }
}
