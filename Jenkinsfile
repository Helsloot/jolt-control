pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Hello') {
            steps {
                sh 'python --version'
            }
        }
        stage('Testing') {
            steps {
                sh 'export PYTHONPATH="./src"'
                sh 'python3 src/jolt/driver/test/driver_test.py'
            }
        }
    }
}