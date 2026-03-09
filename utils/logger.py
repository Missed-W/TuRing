import logging
import os
from logging.handlers import RotatingFileHandler

def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)
    
    # 控制台输出
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(
        '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    ))
    
    # 文件输出
    os.makedirs('logs', exist_ok=True)
    file_handler = RotatingFileHandler(
        'logs/turing.log', maxBytes=5*1024*1024, backupCount=3, encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '[%(asctime)s] %(name)s - %(levelname)s - %(message)s'
    ))
    
    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger