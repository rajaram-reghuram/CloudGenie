from transformers import pipeline
from .config import Config
from .prompt_manager import PromptManager

class CLIGenerator:
    def __init__(self):
        self.generator = pipeline("text2text-generation", model=Config.MODEL_NAME)
        self.prompt_manager = PromptManager()

    def generate_aws_cli(self, service, action, parameters):
        prompt = self.prompt_manager.get_prompt("aws_cli", service=service, action=action, parameters=parameters)
        return self.generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']

    def generate_azure_cli(self, service, action, parameters):
        prompt = self.prompt_manager.get_prompt("azure_cli", service=service, action=action, parameters=parameters)
        return self.generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']

    def generate_kubectl(self, action, resource, parameters):
        prompt = self.prompt_manager.get_prompt("kubectl", action=action, resource=resource, parameters=parameters)
        return self.generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
