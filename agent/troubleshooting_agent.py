from transformers import pipeline
from .config import Config
from .prompt_manager import PromptManager

class TroubleshootingAgent:
    def __init__(self):
        self.generator = pipeline("text2text-generation", model=Config.MODEL_NAME)
        self.prompt_manager = PromptManager()

    def analyze_logs(self, logs):
        prompt = self.prompt_manager.get_prompt("analyze_logs", logs=logs)
        return self.generator(prompt, max_length=200)[0]['generated_text']
