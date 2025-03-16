class PromptManager:
    def __init__(self):
        self.prompts = {
            "terraform": "Generate Terraform code for an AWS {resource_type} with the following configuration: {config}",
            "cloudformation": "Generate CloudFormation template for an AWS {resource_type} with the following configuration: {config}",
            "k8s_yaml": "Generate Kubernetes YAML for a {resource_type} with the following configuration: {config}",
            "dockerfile": "Generate a Dockerfile for an application with the following configuration: {config}",
            "aws_cli": "Generate AWS CLI command for {service} {action} with the following parameters: {parameters}",
            "azure_cli": "Generate Azure CLI command for {service} {action} with the following parameters: {parameters}",
            "kubectl": "Generate kubectl command for {action} {resource} with the following parameters: {parameters}",
            "analyze_logs": "Analyze the following logs and suggest fixes:\n{logs}",
            "check_iam": "Check the following IAM policies for misconfigurations:\n{policies}",
            "create_lambda": "Create an AWS Lambda function with the following details:\nName: {function_name}\nRuntime: {runtime}\nHandler: {handler}\nCode: {code}",
        }

    def get_prompt(self, prompt_type, **kwargs):
        return self.prompts[prompt_type].format(**kwargs)
