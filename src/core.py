"""
Core implementation for Ping Application
Implementação principal do aplicativo Ping
"""


class PingService:
    """
    Serviço principal do aplicativo Ping
    Implementação simples: ping() retorna "pong", pong() retorna "ping"
    """
    
    def __init__(self, name: str = "PingService"):
        """
        Inicializa o serviço Ping
        
        Args:
            name: Nome do serviço
        """
        self.name = name
    
    def ping(self) -> str:
        """
        Retorna "pong"
        
        Returns:
            str: "pong"
        """
        return "pong"
    
    def pong(self) -> str:
        """
        Retorna "ping"
        
        Returns:
            str: "ping"
        """
        return "ping"
