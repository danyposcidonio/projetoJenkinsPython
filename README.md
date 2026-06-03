# Projeto Jenkins Calculadora Web

Projeto Python com Flask para demonstrar CI/CD com Jenkins.

A aplicação abre uma calculadora simples no navegador.

## Rodar localmente no Windows

Entre na raiz do projeto e execute:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m pytest
py -m app.main
```

Acesse:

```text
http://localhost:5000
```

## Rodar os testes

```powershell
py -m pytest
```

## Build simples

```powershell
py -m compileall app
```

## Jenkins

O Jenkinsfile foi preparado para Windows e usa `py`.

A cada commit, o Jenkins irá:

1. Criar ambiente virtual.
2. Instalar dependências.
3. Executar testes.
4. Fazer build com compileall.
5. Derrubar a versão anterior da aplicação na porta 5000.
6. Subir a calculadora web novamente.

Depois do build, acesse:

```text
http://IP_DO_SERVIDOR_JENKINS:5000
```
