from extensions import db
from flask_login import UserMixin
from datetime import datetime
<<<<<<< HEAD
from werkzeug.security import check_password_hash

class Usuario(db.Model, UserMixin):
    """
    Modelo para armazenar os usuários do sistema.
    """
=======
from app import db
from werkzeug.security import check_password_hash

class Usuario(db.Model, UserMixin):
>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
<<<<<<< HEAD
    senha = db.Column(db.String(255), nullable=False)
    formacao = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(20), nullable=False, default='participante')

    inscricoes = db.relationship('Inscricao', back_populates='usuario', cascade="all, delete-orphan")
    checkins = db.relationship('Checkin', back_populates='usuario', cascade="all, delete-orphan")

    def verificar_senha(self, senha):
        """Verifica a senha do usuário"""
        return check_password_hash(self.senha, senha)

    def __repr__(self):
        return f'<Usuario {self.nome} - {self.email}>'

class Oficina(db.Model):
    """
    Modelo para armazenar as oficinas disponíveis.
    """
=======
    senha = db.Column(db.String(255), nullable=False) 
    formacao = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(20), nullable=False, default='participante')
    
    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)  # Para validar no login

class Oficina(db.Model):
>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    ministrante = db.Column(db.String(100), nullable=False)
    vagas = db.Column(db.Integer, nullable=False)
    carga_horaria = db.Column(db.String(10), nullable=False)
<<<<<<< HEAD
    estado = db.Column(db.String(2), nullable=False)  # Sigla do estado
    cidade = db.Column(db.String(100), nullable=False)  # Nome da cidade
    qr_code = db.Column(db.String(255), nullable=True)

    dias = db.relationship('OficinaDia', back_populates='oficina', cascade="all, delete-orphan")
    inscritos = db.relationship('Inscricao', back_populates='oficina', cascade="all, delete-orphan")
    checkins = db.relationship('Checkin', back_populates='oficina', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Oficina {self.titulo} - {self.cidade}/{self.estado}>'

class OficinaDia(db.Model):
    """
    Modelo para armazenar os dias e horários das oficinas.
    """
=======
    estado = db.Column(db.String(2), nullable=False)  # Estado (sigla)
    cidade = db.Column(db.String(100), nullable=False)  # Cidade
    qr_code = db.Column(db.String(255), nullable=True)
    

    def __repr__(self):
        return f'<Oficina {self.titulo}>'

class OficinaDia(db.Model):
>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)
    id = db.Column(db.Integer, primary_key=True)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    horario_inicio = db.Column(db.String(5), nullable=False)
    horario_fim = db.Column(db.String(5), nullable=False)
    palavra_chave_manha = db.Column(db.String(50), nullable=True)  # Palavra-chave para manhã
    palavra_chave_tarde = db.Column(db.String(50), nullable=True)  # Palavra-chave para tarde

<<<<<<< HEAD
    oficina = db.relationship('Oficina', back_populates='dias')
=======

    oficina = db.relationship('Oficina', backref=db.backref('dias', lazy=True))
>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)

    def __repr__(self):
        return f'<OficinaDia {self.data} {self.horario_inicio}-{self.horario_fim}>'

class Inscricao(db.Model):
<<<<<<< HEAD
    """
    Modelo para registrar inscrições de usuários em oficinas.
    """
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)

    usuario = db.relationship('Usuario', back_populates='inscricoes')
    oficina = db.relationship('Oficina', back_populates='inscritos')

    def __repr__(self):
        return f'<Inscricao Usuario: {self.usuario_id} Oficina: {self.oficina_id}>'

class Checkin(db.Model):
    """
    Modelo para armazenar os check-ins dos usuários nas oficinas.
    """
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)  # Corrigido para `utcnow` sem `()`
    palavra_chave = db.Column(db.String(50), nullable=False)

    usuario = db.relationship('Usuario', back_populates='checkins')
    oficina = db.relationship('Oficina', back_populates='checkins')

    def __repr__(self):
        return f'<Checkin Usuario: {self.usuario_id}, Oficina: {self.oficina_id}, Data: {self.data_hora}>'
=======
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'))

    usuario = db.relationship('Usuario', backref='inscricoes')
    oficina = db.relationship('Oficina', backref='inscritos')

    def __repr__(self):
        return f'<Inscricao Usuario: {self.usuario_id} Oficina: {self.oficina_id}>'
    
class Checkin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    oficina_id = db.Column(db.Integer, db.ForeignKey('oficina.id'), nullable=False)
    data_hora = db.Column(db.DateTime, default=lambda: datetime.utcnow())
    palavra_chave = db.Column(db.String(50), nullable=False)

    usuario = db.relationship('Usuario', backref=db.backref('checkins', lazy=True))
    oficina = db.relationship('Oficina', backref=db.backref('checkins', lazy=True))

    def __repr__(self):
        return f'<Checkin Usuario: {self.usuario_id}, Oficina: {self.oficina_id}, Data: {self.data_hora}>'


>>>>>>> 54c2bed (Adiciona .gitignore para proteger arquivos sensíveis)
