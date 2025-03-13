import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    descricao = Column(VARCHAR(100), nullable=False)
    valor_unitario = Column(Integer, nullable=False)
    foto = Column(VARCHAR(100), nullable=False)
 
    def __init__(self, id_produto, descricao, valor_unitario, foto):
        self.id_produto = id_produto
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        self.foto = foto
     