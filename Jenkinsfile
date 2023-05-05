pipeline {
    agent any
    stages {
        stage('Tesr Docker on machine') {
            steps {
                sh 'docker --version'
            }
        }
        stage('Build Docker Image') {
            steps {
//                 git branch: 'main', url: 'https://github.com/Daniel-Modilevsky/devops_practice_ex.git'
                sh 'docker rm danielmodilevsky/auth:1.0 '
                sh 'docker build -t danielmodilevsky/auth:1.0 .'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'docker run -d --name test-auth -p 5002:5000 danielmodilevsky/auth:1.0'
                sh 'sleep 5'
                sh 'curl localhost:5002'
                sh 'docker kill test-auth'
            }
        }
        stage('Upload push image'){
            steps {
                sh 'docker push danielmodilevsky/auth:1.0'
            }
        }
    }
}
