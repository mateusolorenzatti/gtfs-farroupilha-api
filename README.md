# GTFS-Farroupilha-API

API dedicada ao acesso dos dados de GTFS da cidade de Farroupilha/RS.

#### Configurações

Basta criar um ambiente virtual Python e importar os requirements do projeto:

```python
# Rodar no terminal no diretório base do projeto

python3 -m venv venv

source venv/bin/activate # Linux
source ./venv/Scripts/activate # Windows

python3 -m pip install -r src/requirements.txt

```

Para a conexão com o banco de dados, crie um arquivo na raiz do projeto com o nome '.env' da seguinte maneira:

```bash

POSTGRES_SERVER="localhost"
POSTGRES_USER="gtfsfarroupilha"
POSTGRES_PASSWORD="gtfsfarroupilha2020"
POSTGRES_DB="gtfsfarroupilha"

```

#### Utilização

```python
# Navegando até a pasta src/app

python3 main.py

```

Configurações de execução do servidor local podem ser alteradas no final do script:

```python

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8081)
    
```

