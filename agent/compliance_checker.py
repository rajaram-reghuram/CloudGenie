from transformers import pipeline
from .config import Config
from .prompt_manager import PromptManager

class ComplianceChecker:
    def __init__(self):
        self.generator = pipeline("text2text-generation", model=Config.MODEL_NAME)
        self.prompt_manager = PromptManager()

    def check_iam_policies(self, policies):
        prompt = self.prompt_manager.get_prompt("check_iam", policies=policies)
        return self.generator(prompt, max_length=200)[0]['generated_text']
