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

### Executar exemplos de uso

O projeto inclui exemplos práticos de uso do Redis em `app/utils/redis_basics.py`:

```bash
uv run python3 -m app.utils.redis_basics
```

## 📦 Estrutura do Projeto

```
redis_study/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── services/
│   ├── infra/
│   │   ├── cache/
│   │   │   ├── connection.py      # Classe de conexão com Redis
│   │   │   └── repo/
│   │   │       └── redis_repo.py  # Repositório com operações Redis
│   │   └── depends.py             # Dependências para injeção
│   ├── main.py                     # Aplicação FastAPI
│   └── utils/
│       └── redis_basics.py         # Exemplos de uso do Redis
├── configs/
│   └── __init__.py                 # Configurações (Settings)
├── docker-compose.yaml
├── pyproject.toml
└── README.md
```

## 🏗️ Arquitetura

### RedisConnection

Classe responsável por gerenciar a conexão com o Redis. Configurações são carregadas de `configs/settings` ou variáveis de ambiente.

### RedisRepo

Repositório que encapsula operações comuns do Redis, fornecendo uma interface simplificada:

- **Operações básicas:**
  - `set(key, value)` - Define um valor
  - `get(key)` - Obtém um valor (retorna string decodificada ou None)
  - `delete(key)` - Remove uma chave

- **Operações com Hash:**
  - `hset(hash_name, key, value)` - Define um campo em um hash
  - `hget(hash_name, key)` - Obtém um campo de um hash (retorna string decodificada ou None)
  - `hdelete(hash_name, key)` - Remove um campo de um hash

### Exemplo de Uso

```python
from app.infra.depends import get_redis_repo

redis_repo = get_redis_repo()

# Operações básicas
redis_repo.set("chave", "valor")
valor = redis_repo.get("chave")

# Operações com Hash
redis_repo.hset("hash_1", "nome", "joao")
redis_repo.hset("hash_1", "idade", 21)
nome = redis_repo.hget("hash_1", "nome")
```

## ⚙️ Configuração

As configurações do Redis podem ser definidas através de variáveis de ambiente ou arquivo `.env`:

```env
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```

As configurações padrão estão definidas em `configs/__init__.py`.

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
- **Pydantic Settings** - Gerenciamento de configurações

