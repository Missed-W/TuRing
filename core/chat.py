import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_logger
from core.main import TuringCore

logger = get_logger("turing.chat")

def chat_loop():
    core = TuringCore()
    history = []
    current_char = "qwen"
    
    print("\n" + "="*50)
    print("  图灵 已启动")
    print("  /switch qwen      切换到Qwen")
    print("  /switch deepseek  切换到DeepSeek")
    print("  /clear            清空对话历史")
    print("  /exit             退出")
    print("="*50 + "\n")
    
    while True:
        try:
            user_input = input("你：").strip()
            if not user_input:
                continue
            
            # 指令处理
            if user_input.startswith("/"):
                parts = user_input.split()
                cmd = parts[0]
                
                if cmd == "/exit":
                    print("图灵：再见。")
                    break
                
                elif cmd == "/clear":
                    history = []
                    print("图灵：对话历史已清空。")
                
                elif cmd == "/switch" and len(parts) > 1:
                    target = parts[1]
                    if target in core.model_manager.list_models():
                        core.model_manager.load(target)
                        current_char = target
                        print(f"图灵：已切换到 {target}。")
                    else:
                        print(f"图灵：没有找到模型 {target}。")
                
                else:
                    print(f"图灵：未知指令 {cmd}。")
                continue
            
            # 对话
            history.append({"role": "user", "content": user_input})
            reply = core.chat(user_input, history)
            history.append({"role": "assistant", "content": reply})
            print(f"图灵：{reply}\n")
        
        except KeyboardInterrupt:
            print("\n图灵：再见。")
            break

if __name__ == "__main__":
    chat_loop()