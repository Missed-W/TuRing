from abc import ABC, abstractmethod

class SkillInterface(ABC):
    """技能插件基础接口"""
    
    @abstractmethod
    def name(self) -> str:
        """技能名称"""
        pass
    
    @abstractmethod
    def description(self) -> str:
        """技能描述"""
        pass
    
    @abstractmethod
    def run(self, input: str, **kwargs) -> str:
        """执行技能"""
        pass
    
    @abstractmethod
    def can_handle(self, input: str) -> bool:
        """判断是否能处理这个输入"""
        pass