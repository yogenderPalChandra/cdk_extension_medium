pipeline {
    agent {
        dockerfile {
            label 'linux'
            filename 'Dockerfile'
            args '-u root:root'
        }
    }
    options {
        timestamps()
    }
    environment {
        REPOSITORY = fn.getRepository()
        PIP_PACKAGE_NAME = 'lib-cdk'

        AWS_DEFAULT_REGION = 'eu-central-1'
    }
    stages {
        stage('artifactory') {
            steps {
                script {
                    fn.createArtifactoryPipConf()
                }
            }
        }
        stage('test') {
            steps {
                withCredentials(bindings: [usernamePassword(credentialsId: 'artifactory-s2a-jenkins', usernameVariable: 'PYPI_USER', passwordVariable: 'PYPI_PASS')]) {
                    sh '''
                    echo '---- install ----'
                    make install
                    echo '---- lint ----'
                    make lint
                    echo '---- test ----'
                    make test JUNIT_XML=test-reports/report/$PIP_PACKAGE_NAME.xml COV_REPORT_HTML=test-reports/coverage/$PIP_PACKAGE_NAME/
                    '''
                }
                archiveArtifacts artifacts: "test-reports/coverage/${PIP_PACKAGE_NAME}/**/*", onlyIfSuccessful: true
                junit allowEmptyResults: true, testResults: "test-reports/report/${PIP_PACKAGE_NAME}.xml"
            }
        }
        stage('publish test results') {
            steps {
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: true, keepAll: false, reportDir: 'test-reports/coverage/', reportFiles: "${PIP_PACKAGE_NAME}/index.html", reportName: 'HTML Report', reportTitles: "${PIP_PACKAGE_NAME}"])
            }
        }
        stage('bundle') {
            steps {
                sh 'make bundle'
            }
        }
        stage('deliver') {
            when {
                anyOf {
                    branch 'master'
                }
            }
            steps {
                script {
                    fn.publishArtifactoryPip()
                }
            }
        }
    }
    post {
        always {
            cleanWs()
            chuckNorris()
        }
    }
}
