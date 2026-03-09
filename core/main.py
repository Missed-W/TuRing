import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_logger, load_config
from interfaces import ModelInterface, MemoryInterface, SkillInterface, DeviceInterface

logger = get_logger("turing.core")

class TuringCore:
    """图灵核心调度器"""
    
    def __init__(self):
        self.config = load_config()
        self.model: ModelInterface = None
        self.memory: MemoryInterface = None
        self.skills: list[SkillInterface] = []
        self.devices: list[DeviceInterface] = []
        logger.info("图灵核心初始化完成")
    
    def chat(self, message: str) -> str:
        if self.model is None:
            logger.warning("模型未加载")
            return "模型未加载"
        return self.model.chat(message)
    
    def register_skill(self, skill: SkillInterface):
        self.skills.append(skill)
        logger.info(f"技能注册: {skill.name()}")
    
    def register_device(self, device: DeviceInterface):
        self.devices.append(device)
        logger.info(f"设备注册: {device.__class__.__name__}")


if __name__ == "__main__":
    core = TuringCore()
    logger.info("图灵启动成功")
    print("图灵框架已就绪，等待模型接入...")