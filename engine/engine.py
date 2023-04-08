from abc import ABC, abstractmethod
    
    
class Engine:
    def __init__(self):
        pass
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass