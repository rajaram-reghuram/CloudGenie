from transformers import pipeline
from .config import Config
from .prompt_manager import PromptManager

class AutomationManager:
    def __init__(self):
        self.generator = pipeline("text2text-generation", model=Config.MODEL_NAME)
        self.prompt_manager = PromptManager()

    def create_lambda_function(self, function_name, runtime, handler, code):
        prompt = self.prompt_manager.get_prompt("create_lambda", function_name=function_name, runtime=runtime, handler=handler, code=code)
        return self.generator(prompt, max_length=200)[0]['generated_text']
