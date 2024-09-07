pipeline {
    agent any

    environment {
        SUDO_PASSWORD = credentials('nana') // Use Jenkins credentials for sudo password
    }

    stages {
        stage('Install Python') {
            steps {
                script {
                    sh '''
                    echo "$SUDO_PASSWORD" | sudo -S apt-get update
                    echo "$SUDO_PASSWORD" | sudo -S apt-get install -y python3 python3-venv python3-pip
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}
