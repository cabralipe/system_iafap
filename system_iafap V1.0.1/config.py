import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("iafap", os.urandom(24))  # Usa a variável ou gera uma aleatória
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Definir o banco de dados
    if os.getenv("DATABASE_URL"):
        SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # PostgreSQL no Render
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')}"  # SQLite local
