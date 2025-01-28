<<<<<<< HEAD
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import datetime
import os

# Importando extensões corretamente
from extensions import db, login_manager, migrate


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '12303')

    # Inicializando extensões dentro do app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Configuração do Flask-Login
    login_manager.login_view = "routes.login"
    login_manager.session_protection = "strong"

    # Importação e registro das rotas
    from routes import routes
    app.register_blueprint(routes)

    return app

app = create_app()

# 🔹 Agora podemos chamar app.app_context() porque o app já foi definido
with app.app_context():
    db.create_all()  # Criando as tabelas no SQLite se não existirem

# Configurações globais
SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

# Carregamento do usuário no Flask-Login
from models import Usuario  # Agora podemos importar sem erro

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("index.html")
=======
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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Adicione esta linha
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '12303')

# Configurar extensões
db.init_app(app)
login_manager.init_app(app)
migrate.init_app(app, db)

login_manager.login_view = "login"
login_manager.session_protection = "strong"
>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)

# Definição do filtro para formatação de datas
@app.template_filter('string_to_date')
def string_to_date(value):
    try:
        return datetime.strptime(value, '%Y-%m-%d').strftime('%d/%m/%Y')
    except (ValueError, TypeError):
        return value  # Retorna a string original se não puder converter

<<<<<<< HEAD
=======
# Importações que dependem do `db`
from models import Usuario  # Agora funciona sem erro de ciclo!
from routes import *  # Importa rotas depois de inicializar o app

# Carregamento do usuário
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Criar o banco de dados dentro do contexto da aplicação (se não existir)
with app.app_context():
    db.create_all()

>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)
if __name__ == '__main__':
    app.run(debug=True)
