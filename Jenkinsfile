pipeline {
    agent any

    environment {
        PYTHON = "C:\\Program Files\\Python314\\python.exe"
        JENKINS_NODE_COOKIE = "dontKillMe"
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
                    python -m pytest --junitxml=relatorio-testes.xml --cov=app --cov-report=html --cov-report=xml
                """
            }
        }

        stage('Analise de Vulnerabilidades') {
    steps {
        dependencyCheck(
            odcInstallation: 'DependencyCheck',
            additionalArguments: '--scan .'
        )
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
                    C:\\Windows\\System32\\taskkill.exe /F /FI "WINDOWTITLE eq calculadora-jenkins" /T >nul 2>&1
                    exit /B 0
                """
            }
        }

        stage('Iniciar Aplicacao') {
            steps {
                bat """
                    set JENKINS_NODE_COOKIE=dontKillMe
                    start "calculadora-jenkins" cmd /c "call venv\\Scripts\\activate.bat && python -m app.main"
                    C:\\Windows\\System32\\ping.exe 127.0.0.1 -n 6 >nul
                """
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'relatorio-testes.xml'

            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'htmlcov',
                reportFiles: 'index.html',
                reportName: 'Cobertura de Testes'
            ])
        }
    }
}
