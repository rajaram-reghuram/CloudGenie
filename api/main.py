import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch  # Ensures model compatibility

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from agent.code_generator import CodeGenerator
from agent.cli_generator import CLIGenerator
from agent.troubleshooting_agent import TroubleshootingAgent
from agent.compliance_checker import ComplianceChecker
from agent.automation_manager import AutomationManager

# Load FLAN-T5 Model for enhanced CLI and IaC generation
MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

app = FastAPI()

code_gen = CodeGenerator()
cli_gen = CLIGenerator()
troubleshooter = TroubleshootingAgent()
compliance_checker = ComplianceChecker()
automation_manager = AutomationManager()

@app.post("/generate-terraform")
def generate_terraform(config: dict):
    return code_gen.generate_terraform("resource", config)

@app.post("/generate-dockerfile")
def generate_dockerfile(config: dict):
    return code_gen.generate_dockerfile(config)

@app.post("/generate-aws-cli")
def generate_aws_cli(service: str, action: str, parameters: dict):
    return cli_gen.generate_aws_cli(service, action, parameters)

@app.post("/generate-command")
def generate_command(prompt: str):
    """New Route for AI Command Generation using FLAN-T5"""
    try:
        input_ids = tokenizer(prompt, return_tensors="pt").input_ids
        output = model.generate(input_ids, max_length=100, num_return_sequences=1)
        return {"command": tokenizer.decode(output[0], skip_special_tokens=True)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating command: {str(e)}")

@app.post("/analyze-logs")
def analyze_logs(logs: str):
    return troubleshooter.analyze_logs(logs)

@app.get("/")
def home():
    return FileResponse("../content/web/index.html")

app.mount("/web", StaticFiles(directory="../content/web"), name="web")
