from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import datetime
import os

# Importar extensões corretamente
from extensions import db, login_manager, migrate

# Inicializando a aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Boa prática
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '12303')

# Configurar extensões
db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

# Configuração do Flask-Login
login_manager.login_view = "login"
login_manager.session_protection = "strong"

# Definição do filtro para formatação de datas
@app.template_filter('string_to_date')
def string_to_date(value):
    try:
        return datetime.strptime(value, '%Y-%m-%d').strftime('%d/%m/%Y')
    except (ValueError, TypeError):
        return value  # Retorna a string original se não puder converter

# Criar o banco de dados dentro do contexto da aplicação (se não existir)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Importações atrasadas para evitar importação circular
    from models import Usuario  
    from routes import *  

    # Carregamento do usuário no Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    app.run(debug=True)
