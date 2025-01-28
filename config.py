import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

if os.getenv('DATABASE_URL'):  # Quando estiver rodando no Heroku
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/database.db'
else:  # Quando estiver rodando localmente
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')

SQLALCHEMY_TRACK_MODIFICATIONS = False
