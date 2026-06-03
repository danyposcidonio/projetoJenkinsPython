pipeline {
    agent any

    stages {
        stage('Preparar ambiente') {
            steps {
                bat '''
                    if exist venv rmdir /S /Q venv
                    py -m venv venv
                    call venv\Scripts\activate
                    py -m pip install --upgrade pip
                    py -m pip install -r requirements.txt
                '''
            }
        }

        stage('Executar testes') {
            steps {
                bat '''
                    call venv\Scripts\activate
                    py -m pytest --junitxml=relatorio-testes.xml
                '''
            }
        }

        stage('Build') {
            steps {
                bat '''
                    call venv\Scripts\activate
                    py -m compileall app
                '''
            }
        }

        stage('Parar aplicacao anterior') {
            steps {
                bat '''
                    for /f "tokens=5" %%a in ('netstat -ano ^| findstr :5000 ^| findstr LISTENING') do taskkill /F /PID %%a
                    exit /B 0
                '''
            }
        }

        stage('Iniciar aplicacao web') {
            steps {
                bat '''
                    call venv\Scripts\activate
                    start "calculadora-jenkins" /B waitress-serve --host=0.0.0.0 --port=5000 app.main:app > aplicacao.log 2>&1
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'relatorio-testes.xml'
            archiveArtifacts artifacts: 'aplicacao.log', allowEmptyArchive: true
        }
    }
}
