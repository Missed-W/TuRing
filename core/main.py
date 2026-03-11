import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_logger, load_config
from interfaces import ModelInterface, MemoryInterface, SkillInterface, DeviceInterface
from models import ModelManager, OllamaModel

logger = get_logger("turing.core")

class TuringCore:
    """图灵核心调度器"""
    
    def __init__(self):
        self.config = load_config()
        self.model_manager = ModelManager()
        self.memory: MemoryInterface = None
        self.skills: list[SkillInterface] = []
        self.devices: list[DeviceInterface] = []
        self._init_models()
        logger.info("图灵核心初始化完成")
    
    def _init_models(self):
        """注册所有模型"""
        cfg = self.config["models"]
        ollama_url = self.config["ollama"]["base_url"]
        
        self.model_manager.register("qwen", OllamaModel(cfg["default"], ollama_url))
        self.model_manager.register("deepseek", OllamaModel(cfg["reasoning"], ollama_url))
        self.model_manager.load("qwen")
    
    def chat(self, message: str, history: list = None) -> str:
        return self.model_manager.chat(message, history)
    
    def register_skill(self, skill: SkillInterface):
        self.skills.append(skill)
        logger.info(f"技能注册: {skill.name()}")
    
    def register_device(self, device: DeviceInterface):
        self.devices.append(device)
        logger.info(f"设备注册: {device.__class__.__name__}")


if __name__ == "__main__":
    core = TuringCore()
    print("图灵框架已就绪")
    
    # 测试qwen
    reply = core.chat("你好，你是谁？")
    print(f"Qwen：{reply}")
    
    # 测试切换到deepseek
    core.model_manager.load("deepseek")
    reply = core.chat("你好，你是谁？")
    print(f"DeepSeek：{reply}")