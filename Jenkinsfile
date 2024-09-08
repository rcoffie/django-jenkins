pipeline {
    agent any
    
    environment {
        PYTHON_CMD = sh(script: 'which python3', returnStdout: true).trim()
        VENV_NAME = 'django_venv'
        DJANGO_SECRET_KEY = credentials('django-secret-key')
        DJANGO_DEBUG = 'False'
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
                    pip install flake8 black
                    pip list
                """
            }
        }
        
        stage('Code formatting and quality checks') {
            steps {
                sh """
                    . ${VENV_NAME}/bin/activate
                    black .
                    flake8 . --max-line-length=99 --extend-ignore=E503,W503 --exclude=*/migrations/*,*/django_venv/*,*/.venv/*,*/src/*,*/site-packages/*
                """
            }
        }
        
        stage('Run tests') {
            steps {
                withEnv([
                    "SECRET_KEY=${DJANGO_SECRET_KEY}",
                    "DEBUG=${DJANGO_DEBUG}"
                ]) {
                    sh """
                        . ${VENV_NAME}/bin/activate
                        python manage.py check
                        python manage.py test
                    """
                }
            }
        }
        
        stage('Build') {
            steps {
                withEnv([
                    "SECRET_KEY=${DJANGO_SECRET_KEY}",
                    "DEBUG=${DJANGO_DEBUG}"
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
