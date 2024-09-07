pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Name of the virtual environment directory
        DJANGO_SETTINGS_MODULE = 'myproject.settings' // Set your Django settings file
        PIP_CACHE = "${WORKSPACE}/.pip-cache" // To cache pip dependencies
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Checkout the code from source control
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
                // Example packaging step, customize based on your needs
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
                branch 'main' // Only deploy on the main branch
            }
            steps {
                // Add your deployment steps (e.g., using rsync, SSH, Docker, etc.)
                sh '''
                echo "Deploying the Django application to the server"
                # Example deployment command
                # rsync -avz . user@yourserver.com:/path/to/deploy/
                '''
            }
        }
    }

    post {
        always {
            // Cleanup the workspace after the build
            cleanWs()
        }
        success {
            echo 'Build was successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
