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
                bat 'docker build -t hello-app:latest .'
            }
        }
        stage('Run Image') {
            steps {
                bat 'docker run -d -p 5000:5000 --name my_hello_container hello-app:latest'
            }
        }
        stage('Testing') {
            steps {
                echo 'Testing..'
            }
        }
    }
}
