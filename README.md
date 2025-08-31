# Ping Application

Um aplicativo Python simples que implementa funcionalidades básicas de ping/pong.

## Funcionalidades

- `ping()` → retorna "pong"
- `pong()` → retorna "ping"

## Estrutura do Projeto

```
ping/
├── ping.py              # Entrypoint do aplicativo
├── run_tests.py         # Script para executar testes
├── src/
│   ├── __init__.py      # Pacote principal
│   └── core.py          # PingService com ping() e pong()
└── tests/
    ├── __init__.py      # Pacote de testes
    └── test_core.py     # Testes unitários
```

## Instalação

### Opção 1: GitHub (Público)
```bash
# Clone o repositório
git clone git@github.com:synth1s/ping.git
cd ping

# Execute o aplicativo
python ping.py
```

### Opção 2: Azure DevOps (Privado)
```bash
# Clone o repositório
git clone git@ssh.dev.azure.com:v3/RDOr-Corp/RDOr-Inovacao/regua3-sync-engine
cd regua3-sync-engine

# Execute o aplicativo
python ping.py
```

## Uso

```python
from ping_app.core import PingService

# Criar instância do serviço
service = PingService("MyPingService")

# Usar as funções
result1 = service.ping()  # Retorna "pong"
result2 = service.pong()  # Retorna "ping"

print(result1)  # "pong"
print(result2)  # "ping"
```

### Ou usando o comando CLI:

```bash
ping-app
```

## Instalação via pip

### GitHub (Público)
```bash
pip install git+https://github.com/synth1s/ping.git
```

### Azure DevOps (Privado)
```bash
pip install git+ssh://git@ssh.dev.azure.com/v3/RDOr-Corp/RDOr-Inovacao/regua3-sync-engine
```

## Testes

```bash
# Executar todos os testes
python run_tests.py

# Ou usando unittest diretamente
python -m unittest discover tests
```

## Desenvolvimento

Este projeto segue as melhores práticas de desenvolvimento Python:

- ✅ Código limpo e bem documentado
- ✅ Testes unitários completos
- ✅ Type hints para melhor documentação
- ✅ Estrutura modular com separação de responsabilidades
- ✅ Tratamento de erros adequado

## Licença

MIT License
