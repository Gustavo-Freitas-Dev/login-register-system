import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.connection import session
from database.models import Usuario

nome = 'Daff Optical'
data_nasc = '19/01/2004'
email = 'datauserdaff@gmail.com'
senha = 'Daff44217980'

def cadastrar_usuario():

    nome = input('Nome: ')
    data_nasc = input('Data de nascimento:')
    email = input('Email: ')
    senha = input('Senha: ')

    consulta = session.query(Usuario).filter(Usuario.email==email).first()

    if consulta:
        print(f'O email {email} já possui conta em nosso site')
    else:
        print('E-mail cadastrado com sucesso!!!')
        adicionar_conta = Usuario(nome, data_nasc, email, senha)
        session.add(adicionar_conta)
        session.commit()


if __name__ == "__main__":
    cadastrar_usuario()