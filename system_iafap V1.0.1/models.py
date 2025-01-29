from extensions import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuario'  # Define o nome da tabela explicitamente

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    formacao = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(20), nullable=False, default='participante')

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f"<Usuario {self.nome}>"


class Oficina(db.Model):
    __tablename__ = 'oficina'  # Define o nome da tabela explicitamente

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    ministrante = db.Column(db.String(100), nullable=False)
    vagas = db.Column(db.Integer, nullable=False)
    carga_horaria = db.Column(db.String(10), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    qr_code = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Oficina {self.titulo}>"


class OficinaDia(db.Model):
    __tablename__ = 'oficina_dia'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    horario_inicio = db.Column(db.String(5), nullable=False)
    horario_fim = db.Column(db.String(5), nullable=False)
    palavra_chave_manha = db.Column(db.String(50), nullable=True)
    palavra_chave_tarde = db.Column(db.String(50), nullable=True)

    oficina = db.relationship('Oficina', backref=db.backref('dias', lazy=True))

    def __repr__(self):
        return f"<OficinaDia {self.data} {self.horario_inicio}-{self.horario_fim}>"


class Inscricao(db.Model):
    __tablename__ = 'inscricao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('inscricoes', lazy=True))
    oficina = db.relationship('Oficina', backref=db.backref('inscritos', lazy=True))

    def __repr__(self):
        return f"<Inscricao Usuario: {self.usuario_id}, Oficina: {self.oficina_id}>"


class Checkin(db.Model):
    __tablename__ = 'checkin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    palavra_chave = db.Column(db.String(50), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('checkins', lazy=True))
    oficina = db.relationship('Oficina', backref=db.backref('checkins', lazy=True))

    def __repr__(self):
        return f"<Checkin Usuario: {self.usuario_id}, Oficina: {self.oficina_id}, Data: {self.data_hora}>"
