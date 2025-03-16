from transformers import pipeline
from .config import Config
from .prompt_manager import PromptManager

class CodeGenerator:
    def __init__(self):
        self.generator = pipeline("text2text-generation", model=Config.MODEL_NAME)
        self.prompt_manager = PromptManager()

    def generate_terraform(self, resource_type, config):
        prompt = self.prompt_manager.get_prompt("terraform", resource_type=resource_type, config=config)
        return self.generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']

    def generate_cloudformation(self, resource_type, config):
        prompt = self.prompt_manager.get_prompt("cloudformation", resource_type=resource_type, config=config)
        return self.generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']

    def generate_k8s_yaml(self, resource_type, config):
        prompt = self.prompt_manager.get_prompt("k8s_yaml", resource_type=resource_type, config=config)
        return self.generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']

    def generate_dockerfile(self, config):
        prompt = self.prompt_manager.get_prompt("dockerfile", config=config)
        return self.generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
