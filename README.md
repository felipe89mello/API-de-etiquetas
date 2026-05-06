# API de etiquetas
API de etiquetas com CRUD completo


API REST desenvolvida com FastAPI e Python para gerenciamento de etiquetas.

## Tecnologias
- Python
- FastAPI
- SQLAlchemy
- SQLite

## Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/felipe89mello/API-de-etiquetas.git
cd API-de-etiquetas

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install fastapi uvicorn sqlalchemy

# Rode a API
uvicorn main:app --reload
```

Acesse a documentação em: http://localhost:8000/docs

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /etiquetas | Lista todas as etiquetas |
| POST | /etiquetas | Cadastra uma nova etiqueta |
| PUT | /etiquetas/{id} | Atualiza uma etiqueta |
| DELETE | /etiquetas/{id} | Remove uma etiqueta |