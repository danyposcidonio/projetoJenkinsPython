pipeline {
    agent any

    environment {
        PYTHON = "C:\\Users\\Diego\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe"
    }

    stages {

        stage('Preparar Ambiente') {
            steps {
                bat """
                    "%PYTHON%" -m venv venv

                    call venv\\Scripts\\activate.bat

                    python -m pip install --upgrade pip

                    python -m pip install -r requirements.txt
                """
            }
        }

        stage('Executar Testes') {
            steps {
                bat """
                    call venv\\Scripts\\activate.bat

                    python -m pytest --junitxml=relatorio-testes.xml
                """
            }
        }

        stage('Build') {
            steps {
                bat """
                    call venv\\Scripts\\activate.bat

                    python -m compileall app
                """
            }
        }

        stage('Parar Aplicacao Antiga') {
            steps {
                bat """
                    C:\\Windows\\System32\\taskkill.exe /F /IM python.exe /T >nul 2>&1
                    C:\\Windows\\System32\\taskkill.exe /F /IM pythonw.exe /T >nul 2>&1

                    exit /B 0
                """
            }
        }

        stage('Iniciar Aplicacao') {
            steps {
                bat """
                    start "" venv\\Scripts\\pythonw.exe -m app.main
                """
            }
        }

        stage('Aguardar Inicializacao') {
            steps {
                bat """
                    ping 127.0.0.1 -n 6 > nul
                """
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'relatorio-testes.xml'
        }
    }
}