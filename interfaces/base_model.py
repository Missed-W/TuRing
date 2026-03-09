from abc import ABC, abstractmethod

class ModelInterface(ABC):
    """所有LLM模型的基础接口"""
    
    @abstractmethod
    def load(self):
        """加载模型"""
        pass
    
    @abstractmethod
    def unload(self):
        """卸载模型，释放显存"""
        pass
    
    @abstractmethod
    def chat(self, message: str, history: list = None) -> str:
        """对话"""
        pass
    
    @abstractmethod
    def is_loaded(self) -> bool:
        """是否已加载"""
        pass