from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy.orm import relationship

class Curso(db.Model):
    __tablename__ = "curso"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome = db.Column(db.String(200))
