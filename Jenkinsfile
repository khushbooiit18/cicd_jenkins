pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-username/kafka-cicd-demo.git'
            }
        }

        stage('Start Kafka and Zookeeper') {
            steps {
                sh '''
                docker network create kafka-net || true

                docker run -d --name zookeeper --network kafka-net -e ALLOW_ANONYMOUS_LOGIN=yes -p 2181:2181 bitnami/zookeeper:latest

                docker run -d --name kafka --network kafka-net -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181 \
                    -e ALLOW_PLAINTEXT_LISTENER=yes -e KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT \
                    -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
                    -p 9092:9092 bitnami/kafka:latest

                sleep 15
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Producer') {
            steps {
                sh 'python3 producer.py'
            }
        }

        stage('Run Consumer') {
            steps {
                sh 'python3 consumer.py'
            }
        }
    }
}

