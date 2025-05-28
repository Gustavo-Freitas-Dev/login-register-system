import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.connection import session
from database.models import Usuario

nome = 'Guuh Black'
data_nasc = '19/01/2004'
email = 'Guuh_black02@gmail.com'
senha = 'Guuh2163k@'

def cadastrar_usuario(nome, data_nasc, email, senha):

    consulta = session.query(Usuario).filter(Usuario.email==email).first()

    if consulta:
        print(f'O email {email} já possui conta em nosso site')
    else:
        print('E-mail cadastrado com sucesso!!!')
        adicionar_conta = Usuario(nome, data_nasc, email, senha)
        session.add(adicionar_conta)
        session.commit()

cadastrar_usuario(nome, data_nasc, email, senha)