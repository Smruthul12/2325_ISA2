pipeline {
    agent any

    stages {
    
        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t smruthul/img ."
                }
            }
        }
        stage('Build and Run Docker Container') {
            steps {
                script {
                    bat "docker rm -f 2325 || exit 0"
                    bat "docker run -d --2325 smruthul/img"
                }
            }
        }
    }
}
