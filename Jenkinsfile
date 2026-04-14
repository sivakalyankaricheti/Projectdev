pipeline {
    agent any

    environment {
        CONTAINER_ID = ''
        TEST_FILE_PATH = 'test_variables.txt'
    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t my-python-sum .'
            }
        }

        stage('Run') {
            steps {
                script {
                    CONTAINER_ID = sh(
                        script: 'docker run -dit my-python-sum',
                        returnStdout: true
                    ).trim()
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def testLines = readFile(TEST_FILE_PATH).split('\n')

                    for (line in testLines) {
                        def vars = line.split(' ')
                        def arg1 = vars[0]
                        def arg2 = vars[1]
                        def expectedSum = vars[2].toFloat()

                        def output = sh(
                            script: "docker exec ${CONTAINER_ID} python /app/sum.py ${arg1} ${arg2}",
                            returnStdout: true
                        ).trim()

                        def result = output.toFloat()

                        if (result == expectedSum) {
                            echo "Test passed for ${arg1} + ${arg2}"
                        } else {
                            error "Test failed for ${arg1} + ${arg2}"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            sh "docker stop ${CONTAINER_ID} || true"
            sh "docker rm ${CONTAINER_ID} || true"
        }
    }
}
