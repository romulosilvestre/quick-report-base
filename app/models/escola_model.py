from app import db #SQLAlchemy - Migrate:Migrar Classe para Tabela
from sqlalchemy.orm import relationship

class Escola(db.Model):
    __tablename__ = "escola"
    #id = db.Column(tipo,chave,auto)
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nome  = db.Column(db.String(200))
    fk_curso_id= db.Column(db.Integer,db.ForeignKey('curso.id'))
  