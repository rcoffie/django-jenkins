pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.9'  // Specify your Python version
        VENV_NAME = 'django_venv'
        PYENV_ROOT = "$HOME/.pyenv"
        PATH = "$PYENV_ROOT/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
         stage('Install Python') {
            steps {
                // sh '''
                // sudo apt-get update
                // sudo apt-get install -y python3.9 python3.9-venv python3.9-dev
                // python3.9 --version
                // '''
                sh '''
                curl https://pyenv.run | bash
                export PATH="$HOME/.pyenv/bin:$PATH"
                eval "$(pyenv init --path)"
                eval "$(pyenv init -)"
                pyenv install 3.9.10
                pyenv global 3.9.10
                '''
            }
        }
        stage('Check Python Version') {
            steps {
                sh '''
                export PATH="$HOME/.pyenv/bin:$PATH"
                eval "$(pyenv init --path)"
                eval "$(pyenv init -)"
                python --version
                '''
            }
        }

        stage('Set up Python environment') {
            steps {
                sh """
                    python${PYTHON_VERSION} -m venv ${VENV_NAME}
                    . ${VENV_NAME}/bin/activate
                    pip install --upgrade pip
                """
            }
        }

        stage('Install dependencies') {
            steps {
                sh """
                    . ${VENV_NAME}/bin/activate
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run tests') {
            steps {
                sh """
                    . ${VENV_NAME}/bin/activate
                    python manage.py test
                """
            }
        }

        stage('Code quality checks') {
            steps {
                sh """
                    . ${VENV_NAME}/bin/activate
                    flake8 .
                    black --check .
                """
            }
        }

        stage('Collect static files') {
            steps {
                sh """
                    . ${VENV_NAME}/bin/activate
                    python manage.py collectstatic --noinput
                """
            }
        }

        stage('Deploy to staging') {
            when {
                branch 'develop'
            }
            steps {
                echo 'Deploying to staging server...'
                // Add your deployment steps here
            }
        }

        stage('Deploy to production') {
            when {
                branch 'main'
            }
            steps {
                echo 'Deploying to production server...'
                // Add your production deployment steps here
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh "rm -rf ${VENV_NAME}"
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}