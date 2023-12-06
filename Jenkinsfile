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
                def containerName = "my_hello_container_${BUILD_ID}"
                sh "sudo docker run -d -p 5000:80 --name ${containerName} hello-app:latest"
            }
        }

        stage('Testing') {
            steps {
                echo 'Testing..'
            }
        }
    }
}
