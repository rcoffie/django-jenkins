pipeline {
    agent any
    
    environment {
        // Use a more flexible Python version specification
        PYTHON_CMD = sh(script: 'which python3', returnStdout: true).trim()
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
                script {
                    if (!PYTHON_CMD) {
                        error "Python 3 not found. Please install Python 3 on the Jenkins server."
                    }
                }
                sh """
                    ${PYTHON_CMD} -m venv ${VENV_NAME}
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
                    pip install flake8 black  # Install linting tools if not in requirements.txt
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
