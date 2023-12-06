pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t hello-app:latest .'
            }
        }
        stage('Run Image') {
            steps {
                sh 'docker stop my_hello_container || true'
                sh 'docker rm my_hello_container || true'
                sh 'docker run -d -p 5000:8081 --name my_hello_container hello-app:latest'
            }
        }

        stage('Testing') {
            steps {
                echo 'Testing..'
            }
        }
    }
}
