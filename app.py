from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import datetime
from routes import *  # Importa todas as rotas
import os


# Inicializando a aplicação
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Boa prática
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', '12303')

# Inicializando extensões
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)

# Configuração do Flask-Login
login_manager.login_view = "login"
login_manager.session_protection = "strong"

# Definição do modelo de usuário
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(150), nullable=False)

    def get_id(self):
        return str(self.id)

# Criar o banco de dados dentro do contexto da aplicação
with app.app_context():
    db.create_all()

# Carregamento do usuário no Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("index.html")

# Definição do filtro para formatação de datas
@app.template_filter('string_to_date')
def string_to_date(value):
    try:
        return datetime.strptime(value, '%Y-%m-%d').strftime('%d/%m/%Y')
    except (ValueError, TypeError):
        return value  # Retorna a string original se não puder converter

if __name__ == '__main__':
    from routes import *  # Importação atrasada para evitar circularidade
    app.run(debug=True)
