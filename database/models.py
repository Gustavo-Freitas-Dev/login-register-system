from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from datetime import datetime
from passlib.hash import bcrypt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.connection import Base, session

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
    # adicionar_conta = Usuario('Teste da Silva', '28/02/2012', 'testedasilva@gmail.com', 'silvinha123@')
    # session.add(adicionar_conta)
    # session.commit()

    # Verificador de usuário
    email = str(input('E-mail: '))
    senha = str(input('Senha: '))

    usuario = session.query(Usuario).filter(Usuario.email==email).first()

    if usuario and bcrypt.verify(senha, usuario.senha):
        print('Usuário cadastrado!!')
    else:
        print('Novo usuário cadastrado!!!!')
