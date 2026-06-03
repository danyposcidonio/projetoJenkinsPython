from app import create_app


def test_home_status_code():
    app = create_app()
    client = app.test_client()

    resposta = client.get("/")

    assert resposta.status_code == 200
    assert b"Calculadora Jenkins" in resposta.data


def test_health_status_code():
    app = create_app()
    client = app.test_client()

    resposta = client.get("/health")

    assert resposta.status_code == 200
    assert resposta.get_json() == {"status": "ok"}


def test_calculo_soma_pela_interface():
    app = create_app()
    client = app.test_client()

    resposta = client.post(
        "/",
        data={"numero1": "10", "numero2": "5", "operacao": "somar"},
    )

    assert resposta.status_code == 200
    assert b"Resultado" in resposta.data
    assert b"15" in resposta.data
