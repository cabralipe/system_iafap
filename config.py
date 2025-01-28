import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if os.getenv('DATABASE_URL'):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/database.db'  # Caminho correto no Heroku
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')  # Para rodar localmente
