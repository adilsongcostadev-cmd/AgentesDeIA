import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # Carrega as variáveis do .env para os.environ
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
models = client.models.list()

for model in models.data:
    print(model.id)
    