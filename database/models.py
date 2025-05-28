from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from datetime import datetime
from passlib.hash import bcrypt
from connection import Base, session

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=True)
    data_nasc = Column(Date, nullable=True)
    email = Column(String, nullable=True)
    senha = Column(String, nullable=True)
    ativo = Column(Boolean, default=True)
    data_cadastro = Column(DateTime, default=datetime.utcnow())
    ultimo_acesso = Column(DateTime)

    def __init__(self, nome, data_nasc, email, senha, ativo=True):
        self.nome = nome
        self.data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y').date()
        self.email = email
        self.senha = bcrypt.hash(senha)
        self.ativo = ativo


#Testando a aplicação 
if __name__ == '__main__':
    adicionar_conta = Usuario('Teste Testando2', '28/02/2012', 'testetestestando@gmail.com', 'teste123@')
    session.add(adicionar_conta)
    session.commit()