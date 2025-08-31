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
        self.mirror_mode = False
    
    def ping(self) -> str:
        """
        Retorna "pong" (ou "ping" se mirror_mode estiver ativo)
        
        Returns:
            str: "pong" ou "ping" (dependendo do modo)
        """
        if self.mirror_mode:
            return "ping"
        return "pong"
    
    def pong(self) -> str:
        """
        Retorna "ping" (ou "pong" se mirror_mode estiver ativo)
        
        Returns:
            str: "ping" ou "pong" (dependendo do modo)
        """
        if self.mirror_mode:
            return "pong"
        return "ping"
    
    def mirror(self, enabled: bool = True) -> None:
        """
        Habilita ou desabilita o modo mirror
        
        Args:
            enabled: True para habilitar mirror mode, False para desabilitar
        """
        self.mirror_mode = enabled
    
    def is_mirror_enabled(self) -> bool:
        """
        Verifica se o modo mirror está ativo
        
        Returns:
            bool: True se mirror mode está ativo, False caso contrário
        """
        return self.mirror_mode


def main():
    """Função principal para uso como entry point"""
    service = PingService("PingApp")
    
    print("=== Modo Normal ===")
    print(f"Ping: {service.ping()}")
    print(f"Pong: {service.pong()}")
    
    print("\n=== Modo Mirror ===")
    service.mirror(True)
    print(f"Ping: {service.ping()}")
    print(f"Pong: {service.pong()}")
    
    print("\n=== Modo Normal (novamente) ===")
    service.mirror(False)
    print(f"Ping: {service.ping()}")
    print(f"Pong: {service.pong()}")


if __name__ == "__main__":
    main()
