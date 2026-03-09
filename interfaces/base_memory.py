from abc import ABC, abstractmethod

class MemoryInterface(ABC):
    """记忆系统基础接口"""
    
    @abstractmethod
    def save(self, content: str, metadata: dict = None):
        """存入记忆"""
        pass
    
    @abstractmethod
    def search(self, query: str, top_k: int = 5) -> list:
        """检索记忆"""
        pass
    
    @abstractmethod
    def clear(self):
        """清空记忆"""
        pass