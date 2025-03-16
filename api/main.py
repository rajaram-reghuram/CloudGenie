import sys
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from agent.code_generator import CodeGenerator
from agent.cli_generator import CLIGenerator
from agent.troubleshooting_agent import TroubleshootingAgent
from agent.compliance_checker import ComplianceChecker
from agent.automation_manager import AutomationManager

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

@app.post("/analyze-logs")
def analyze_logs(logs: str):
    return troubleshooter.analyze_logs(logs)

@app.get("/")
def home():
    return FileResponse("../content/web/index.html")

app.mount("/web", StaticFiles(directory="../content/web"), name="web")
