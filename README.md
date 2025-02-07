# API de Testes para Validações e Autorizações

Esta é uma API simples desenvolvida com Flask, utilizada exclusivamente para testes de validações e autorizações. **Não é recomendada para uso em produção.**

## Instalação e Execução

1. Clone este repositório:
   ```sh
   git clone https://github.com/caikecunha/flask-auth-tester.git
   ```

2. Instale as dependências (se necessário, ative um ambiente virtual antes):
   ```sh
   pip install flask
   ```

3. Execute a API:
   ```sh
   python auth_tester.py
   ```

A API será executada em `http://127.0.0.1:5000`.

## Endpoints

### `GET /`
Retorna aleatoriamente se a autorização foi concedida ou negada.

**Respostas possíveis:**
- `200 OK`
  ```json
  {
    "status": "ok",
    "message": "autorizado",
    "code": 200
  }
  ```
- `403 Forbidden`
  ```json
  {
    "status": "falha",
    "message": "negado",
    "code": 403
  }
  ```

### `GET /sempre-autorizado`
Sempre retorna uma resposta de autorização concedida.

**Resposta:**
- `200 OK`
  ```json
  {
    "status": "ok",
    "message": "autorizado",
    "code": 200
  }
  ```

### `GET /sempre-negado`
Sempre retorna uma resposta de autorização negada.

**Resposta:**
- `403 Forbidden`
  ```json
  {
    "status": "falha",
    "message": "negado",
    "code": 403
  }
  ```

## Observações

- O endpoint `/` retorna `True` ou `False` de forma aleatória para simular diferentes respostas.
- O código de status HTTP acompanha a resposta (`200` para autorizado, `403` para negado).
- Esta API deve ser utilizada apenas para fins de testes e validações.
