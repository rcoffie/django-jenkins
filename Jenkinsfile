pipeline {
    agent any
    
    environment {
        PYTHON_CMD = sh(script: 'which python3', returnStdout: true).trim()
        VENV_NAME = 'django_venv'
        // Define your environment variables here
        DJANGO_SECRET_KEY = credentials('django-secret-key')
        DJANGO_DEBUG = 'False'  // Set to 'True' for development, 'False' for production
        // Add any other environment variables your Django project needs
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
                    pip list  # Debug: List installed packages
                """
            }
        }
        
        stage('Debug Information') {
            steps {
                sh """
                    . ${VENV_NAME}/bin/activate
                    echo "Current directory: \$(pwd)"
                    echo "Directory contents:"
                    ls -la
                    echo "Python version:"
                    python --version
                    echo "Django version:"
                    python -m django --version
                """
            }
        }
        
        stage('Run tests') {
            steps {
                withEnv([
                    "SECRET_KEY=${DJANGO_SECRET_KEY}",
                    "DEBUG=${DJANGO_DEBUG}"
                    // Add any other environment variables here
                ]) {
                    sh """
                        . ${VENV_NAME}/bin/activate
                        if [ -f manage.py ]; then
                            python manage.py check  # Run Django system check
                            python manage.py test
                        else
                            echo "manage.py not found in the current directory"
                            exit 1
                        fi
                    """
                }
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
                withEnv([
                    "SECRET_KEY=${DJANGO_SECRET_KEY}",
                    "DEBUG=${DJANGO_DEBUG}"
                    // Add any other environment variables here
                ]) {
                    sh """
                        . ${VENV_NAME}/bin/activate
                        python manage.py collectstatic --noinput
                    """
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Deploying the application..."
            }
        }
    }
    
    post {
        always {
            sh "rm -rf ${VENV_NAME}"
        }
    }
}
