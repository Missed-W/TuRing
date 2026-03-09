from abc import ABC, abstractmethod

class DeviceInterface(ABC):
    """设备控制基础接口"""
    
    @abstractmethod
    def connect(self):
        """连接设备"""
        pass
    
    @abstractmethod
    def disconnect(self):
        """断开设备"""
        pass
    
    @abstractmethod
    def send(self, data: str):
        """发送数据到设备"""
        pass
    
    @abstractmethod
    def receive(self) -> str:
        """从设备接收数据"""
        pass
    
    @abstractmethod
    def is_connected(self) -> bool:
        """是否已连接"""
        pass