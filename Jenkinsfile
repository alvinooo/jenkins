pipeline {
    agent any
    stages {
        stage('Fast Test') {
            steps {
                echo 'Running Fast Tests'
                python3.6 -m "nose" test_tuorial.py
            }
        }
        stage('Slow Test') {
            steps {
                echo 'Running Slow Tests'
            }
        }
        stage('Feature Tests') {
            steps {
                echo 'Running Feature Tests'
            }
        }
    }
}
