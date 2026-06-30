import os

from dotenv import load_dotenv

load_dotenv()

# 예: postgresql+psycopg://user:password@localhost:5432/dbname
DATABASE_URL = os.getenv("DATABASE_URL")

# n8n 발송 채널 (Gmail 자격증명은 n8n이 보유)
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook/sherlock-email")
N8N_WEBHOOK_TOKEN = os.getenv("N8N_WEBHOOK_TOKEN", "")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
