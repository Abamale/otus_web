pipeline {
    agent any

    environment {
        ENV_VARS = sh(script: 'grep -v "^#" .env | xargs', returnStdout: true).trim()
        DOCKER_BIN = '/usr/bin/docker'  // <-- поменяйте путь, если докер в другом месте
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
                echo "PATH = $PATH"
                which docker
                docker --version
                docker compose version || echo "docker compose command not found"
                ${DOCKER_BIN} compose down || true
                ${DOCKER_BIN} compose up -d
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing Python requirements..."
                sh '''
                set -e
                export ${ENV_VARS}
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run API Tests') {
            steps {
                echo "Running API tests..."
                sh '''
                set -e
                export ${ENV_VARS}
                pytest tests/tests_api/ --alluredir=allure-results/api
                '''
            }
        }

        stage('Run UI Tests') {
            steps {
                echo "Running UI tests..."
                sh '''
                set -e
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
            set +e
            export ${ENV_VARS}
            ${DOCKER_BIN} compose down || true
            '''
            archiveArtifacts artifacts: '**/allure-results/**/*.*', allowEmptyArchive: true
        }
    }
}
