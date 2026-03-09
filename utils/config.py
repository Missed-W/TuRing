import json
import os

DEFAULT_CONFIG = {
    "models": {
        "default": "qwen2.5:7b",
        "reasoning": "deepseek-r1:7b",
        "vision": "minicpm-v:2.6"
    },
    "ollama": {
        "base_url": "http://127.0.0.1:11434"
    },
    "memory": {
        "redis_host": "localhost",
        "redis_port": 6379,
        "chroma_path": "./chroma_db"
    },
    "characters": {
        "turing": {"name": "图灵", "lang": "zh"},
        "deepseek": {"name": "DeepSeek", "lang": "zh"},
        "claude": {"name": "Claude", "lang": "en"}
    }
}

def load_config(path: str = "config.json") -> dict:
    if not os.path.exists(path):
        save_config(DEFAULT_CONFIG, path)
        return DEFAULT_CONFIG
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config: dict, path: str = "config.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)