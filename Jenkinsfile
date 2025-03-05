pipeline {
    agent any
 
    environment {
        DOCKER_HUB_USER = "hariabjayon15"
        IMAGE_NAME = "${DOCKER_HUB_USER}/flask-app"
    }
 
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/hari-abjayon/flask-docker-app.git'
        }
 
        stage('Build Docker Image') {
            steps {
                script {
                    def BUILD_NUMBER = env.BUILD_NUMBER
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
                    sh "docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest"
                }
            }
        }
 
        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'docker-hub-token', variable: 'DOCKER_PASSWORD')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_HUB_USER} --password-stdin"
                        sh "docker push ${IMAGE_NAME}:${BUILD_NUMBER}"
                        sh "docker push ${IMAGE_NAME}:latest"
                    }
                }
            }
        }
    }
}