pipeline {
    agent any

    environment {
        PYTHON   = 'python3'
        VENV_DIR = '.venv'
        PIP_CACHE_DIR = "${WORKSPACE}/.pip-cache"
    }

    options {
        timestamps()
        ansiColor('xterm')
        timeout(time: 10, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python env') {
            steps {
                sh '''
                    set -euo pipefail
                    ${PYTHON} --version
                    ${PYTHON} -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate

                    mkdir -p "${PIP_CACHE_DIR}"
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run pytest') {
            steps {
                sh '''
                    set -euo pipefail
                    . ${VENV_DIR}/bin/activate
                    mkdir -p reports
                    pytest -v --junitxml=reports/junit-report.xml
                '''
            }
        }
    }

    post {
        always {
            // Publikacja wyników testów w Jenkinsie (wymaga pluginu "JUnit")
            junit allowEmptyResults: true, testResults: 'reports/junit-report.xml'
            archiveArtifacts artifacts: 'reports/junit-report.xml', allowEmptyArchive: true
        }
        success {
            echo 'Tests passed 🎉'
        }
        failure {
            echo 'Tests failed ❌'
        }
    }
}
