pipeline{
    agent any
    stages{
        stage("build"){
            sh 'pip3 install -r reqqirements.txt'
        }
        stage('test'){
            steps{
                sh 'python3 manage.py test'
            }
        }
        stage('Deploy'){
            steps{
                echo 'deploying '
            }
        }
    }
}