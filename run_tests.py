#!/usr/bin/env python3
"""
Script para executar testes unitários do Ping Application
"""

import sys
import os
import unittest

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def run_tests():
    """Executa todos os testes unitários"""
    print("🧪 Executando testes unitários do Ping Application...")
    print("=" * 50)
    
    # Descobre e executa todos os testes
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'tests')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Executa os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("=" * 50)
    if result.wasSuccessful():
        print("✅ Todos os testes passaram!")
        return 0
    else:
        print("❌ Alguns testes falharam!")
        return 1


if __name__ == '__main__':
    sys.exit(run_tests())
