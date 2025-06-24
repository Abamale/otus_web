pipeline {
    agent any

    environment {
        ENV_VARS = sh(script: 'grep -v "^#" .env | xargs', returnStdout: true).trim()
        CHROME_BIN = '/usr/bin/google-chrome-stable'
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
                script {
                    apiStatus = sh(
                        script: '''
                            set -e
                            export ${ENV_VARS}
                            pytest tests/tests_api/ --alluredir=allure-results/api
                        ''',
                        returnStatus: true
                    )
                }
            }
        }

        stage('Run UI Tests') {
            steps {
                echo "Running UI tests..."
                script {
                    uiStatus = sh(
                        script: '''
                            set -e
                            export ${ENV_VARS}
                            pytest tests/ --ignore=tests/tests_api --alluredir=allure-results/ui
                        ''',
                        returnStatus: true
                    )
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up containers..."
            sh '''
                set +e
                export ${ENV_VARS}
                docker compose down || true
            '''

            echo "Archiving Allure results..."
            archiveArtifacts artifacts: '**/allure-results/**/*.*', allowEmptyArchive: true

            echo "Publishing Allure report..."
            allure([
                commandline: 'Allure Commandline', // вот ЭТО строка новая!
                includeProperties: false,
                jdk: '',
                results: [
                    [path: 'allure-results/api'],
                    [path: 'allure-results/ui']
                ]
            ])

            script {
                if (apiStatus != 0 || uiStatus != 0) {
                    currentBuild.result = 'UNSTABLE'
                }
            }
        }
    }
}
