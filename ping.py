#!/usr/bin/env python3
"""
Ping Application - Entry Point
Aplicativo experimental para testes de instalação de pacotes privados
"""

import sys
import os
from typing import Optional

# Adiciona o diretório src ao path para importação
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core import PingService


def main() -> int:
    """
    Função principal do aplicativo Ping
    
    Returns:
        int: Código de saída (0 para sucesso, 1 para erro)
    """
    try:
        print("🚀 Ping Application iniciado!")
        print(f"Python version: {sys.version}")
        print(f"Working directory: {os.getcwd()}")
        
        # Criando e usando o serviço Ping
        ping_service = PingService("ExperimentalPing")
        
        # Testando ping() -> "pong"
        ping_result = ping_service.ping()
        print(f"📡 ping() -> {ping_result}")
        
        # Testando pong() -> "ping"
        pong_result = ping_service.pong()
        print(f"📡 pong() -> {pong_result}")
        
        print("✅ Aplicativo executado com sucesso!")
        
        return 0
        
    except Exception as e:
        print(f"❌ Erro ao executar o aplicativo: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
