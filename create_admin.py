<<<<<<< HEAD
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from app import app, db  # Certifique-se de que o `app` está configurado corretamente
from models import Usuario

# Certifique-se de que o contexto do aplicativo está ativo
with app.app_context():
    # Verifica se o administrador já existe
    admin_existente = Usuario.query.filter_by(email="admin@exemplo.com").first()
    
    if admin_existente:
        print("Administrador já existe no banco de dados.")
    else:
        # Criando um Administrador Padrão
        admin = Usuario(
            nome="Administrador",
            cpf="000.000.000-00",  # Certifique-se de colocar um CPF válido
            email="admin@exemplo.com",
            senha=generate_password_hash("123456", method='pbkdf2:sha256'),
            formacao="Gestão",
            tipo="admin"
        )

        # Adicionando ao banco de dados
        db.session.add(admin)
        db.session.commit()

        print("Administrador criado com sucesso!")
=======
from app import db
from models import Usuario
from werkzeug.security import generate_password_hash

# Criando um Administrador Padrão
admin = Usuario(
    nome="Administrador",
    cpf="000.000.000-00",  # Certifique-se de colocar um CPF válido
    email="admin@exemplo.com",
    senha=generate_password_hash("123456", method='pbkdf2:sha256'),
    formacao="Gestão",
    tipo="admin"
)

# Adicionando ao banco de dados
db.session.add(admin)
db.session.commit()

print("Administrador criado com sucesso!")
>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)
