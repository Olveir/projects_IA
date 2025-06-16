import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Certifique-se de que sua GOOGLE_API_KEY está definida
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

for model in genai.list_models():
    if "generateContent" in model.supported_generation_methods:
        print(f"Nome do Modelo: {model.name}")
        print(f"Descrição: {model.description}")
        print(f"Métodos Suportados: {model.supported_generation_methods}")
        print("-" * 20)