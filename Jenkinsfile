pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Build steps go here
               // echo 'Building...'
                sh 'pip 3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Test steps go here
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy steps go here
                echo 'Deploying...'
            }
        }
    }
}
