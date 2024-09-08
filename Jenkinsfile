pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.9'
        VENV_NAME = 'django_venv'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Set up Python environment') {
            steps {
                sh """
                    python${PYTHON_VERSION} -m venv ${VENV_NAME}
                    . ${VENV_NAME}/bin/activate
                    pip install --upgrade pip
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
        
        stage('Build') {
            steps {
                sh """
                    . ${VENV_NAME}/bin/activate
                    python manage.py collectstatic --noinput
                """
            }
        }
        
        stage('Deploy') {
            steps {
                // Add your deployment steps here
                echo "Deploying the application..."
            }
        }
    }
    
    post {
        always {
            // Clean up the virtual environment
            sh "rm -rf ${VENV_NAME}"
        }
    }
}
