# Redis Study

Projeto de estudos sobre Redis utilizando FastAPI e Python.

## 📋 Requisitos

- Python >= 3.13
- Docker e Docker Compose
- UV (gerenciador de pacotes Python)

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd redis_study
```

2. Instale as dependências:
```bash
uv sync
```

3. Inicie o Redis com Docker Compose:
```bash
docker compose up -d
```

Ou use o comando do taskipy:
```bash
uv run task up
```

## 🛠️ Uso

### Iniciar a aplicação

```bash
uv run task start
```

A aplicação estará disponível em `http://localhost:8000`

### Parar o Redis

```bash
uv run task down
```

## 📦 Estrutura do Projeto

```
redis_study/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── services/
│   └── main.py
├── docker-compose.yaml
├── pyproject.toml
└── README.md
```

## 🔧 Comandos Disponíveis

- `uv run task format` - Formata o código
- `uv run task lint` - Verifica o código
- `uv run task test` - Executa os testes
- `uv run task up` - Inicia o Redis
- `uv run task down` - Para o Redis
- `uv run task start` - Inicia a aplicação FastAPI

## 🔌 Redis

O Redis está configurado para:
- Porta: `6379`
- Persistência: AOF (Append Only File) habilitado
- Volume: Dados persistidos em `redis_data`

## 📚 Tecnologias

- **FastAPI** - Framework web moderno e rápido
- **Redis** - Banco de dados em memória
- **Python 3.13+** - Linguagem de programação
- **Docker Compose** - Orquestração de containers

