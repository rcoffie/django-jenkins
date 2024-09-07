pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DJANGO_SETTINGS_MODULE = 'myproject.settings'
        PIP_CACHE = "${WORKSPACE}/.pip-cache"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/your-user/your-django-repo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
                pip install --cache-dir=${PIP_CACHE} -r requirements.txt
                '''
            }
        }

        stage('Linting') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                python manage.py test --settings=${DJANGO_SETTINGS_MODULE} --verbosity=2
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Build and Package') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                python manage.py migrate --noinput
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/*.py', allowEmptyArchive: true
            }
        }

        stage('Deployment') {
            when {
                branch 'main'
            }
            steps {
                // Replace this with actual deployment steps
                sh 'echo "Deploying the Django application to the server"'
            }
        }
    }

    post {
        always {
            cleanWs()  // Clean the workspace after each run
        }
        success {
            echo 'Build was successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
