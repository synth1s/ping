"""
Unit tests for PingService
Testes unitários para o PingService
"""

import unittest
import sys
import os

# Adiciona o diretório src ao path para importação
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.core import PingService


class TestPingService(unittest.TestCase):
    """Testes para a classe PingService"""
    
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.ping_service = PingService("TestPingService")
    
    def test_ping_returns_pong(self):
        """Testa se ping() retorna 'pong'"""
        result = self.ping_service.ping()
        self.assertEqual(result, "pong")
        self.assertIsInstance(result, str)
    
    def test_pong_returns_ping(self):
        """Testa se pong() retorna 'ping'"""
        result = self.ping_service.pong()
        self.assertEqual(result, "ping")
        self.assertIsInstance(result, str)
    
    def test_ping_and_pong_are_different(self):
        """Testa se ping() e pong() retornam valores diferentes"""
        ping_result = self.ping_service.ping()
        pong_result = self.ping_service.pong()
        self.assertNotEqual(ping_result, pong_result)
    
    def test_service_initialization(self):
        """Testa se o serviço é inicializado corretamente"""
        service = PingService("CustomName")
        self.assertEqual(service.name, "CustomName")
    
    def test_default_service_name(self):
        """Testa se o nome padrão é aplicado quando não especificado"""
        service = PingService()
        self.assertEqual(service.name, "PingService")
    
    def test_multiple_calls_consistency(self):
        """Testa se múltiplas chamadas retornam o mesmo resultado"""
        ping_result1 = self.ping_service.ping()
        ping_result2 = self.ping_service.ping()
        self.assertEqual(ping_result1, ping_result2)
        
        pong_result1 = self.ping_service.pong()
        pong_result2 = self.ping_service.pong()
        self.assertEqual(pong_result1, pong_result2)
    
    def test_mirror_mode_enable(self):
        """Testa se o modo mirror é habilitado corretamente"""
        self.ping_service.mirror(True)
        self.assertTrue(self.ping_service.is_mirror_enabled())
    
    def test_mirror_mode_disable(self):
        """Testa se o modo mirror é desabilitado corretamente"""
        self.ping_service.mirror(False)
        self.assertFalse(self.ping_service.is_mirror_enabled())
    
    def test_mirror_mode_default(self):
        """Testa se o modo mirror é habilitado por padrão"""
        self.ping_service.mirror()
        self.assertTrue(self.ping_service.is_mirror_enabled())
    
    def test_ping_with_mirror_enabled(self):
        """Testa se ping() retorna 'ping' quando mirror está ativo"""
        self.ping_service.mirror(True)
        result = self.ping_service.ping()
        self.assertEqual(result, "ping")
    
    def test_pong_with_mirror_enabled(self):
        """Testa se pong() retorna 'pong' quando mirror está ativo"""
        self.ping_service.mirror(True)
        result = self.ping_service.pong()
        self.assertEqual(result, "pong")
    
    def test_mirror_mode_behavior(self):
        """Testa o comportamento completo do modo mirror"""
        # Modo normal
        self.assertEqual(self.ping_service.ping(), "pong")
        self.assertEqual(self.ping_service.pong(), "ping")
        
        # Modo mirror
        self.ping_service.mirror(True)
        self.assertEqual(self.ping_service.ping(), "ping")
        self.assertEqual(self.ping_service.pong(), "pong")
        
        # Volta ao modo normal
        self.ping_service.mirror(False)
        self.assertEqual(self.ping_service.ping(), "pong")
        self.assertEqual(self.ping_service.pong(), "ping")


class TestPingServiceIntegration(unittest.TestCase):
    """Testes de integração para PingService"""
    
    def test_ping_pong_cycle(self):
        """Testa o ciclo completo ping -> pong -> ping"""
        service = PingService("IntegrationTest")
        
        # Primeiro ping
        result1 = service.ping()
        self.assertEqual(result1, "pong")
        
        # Depois pong
        result2 = service.pong()
        self.assertEqual(result2, "ping")
        
        # Novamente ping
        result3 = service.ping()
        self.assertEqual(result3, "pong")
        
        # Verifica que o ciclo é consistente
        self.assertEqual(result1, result3)
        self.assertNotEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()
