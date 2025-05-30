from connection import session
from models import Usuario

def consultar():
    email = input('Email: ')

    consulta = session.query(Usuario).filter(Usuario.email==email).first()

    if consulta:
        print(
            f'ID: {consulta.id}\n'
            f'Nome: {consulta.nome}\n'
            f'Data de Nascimento: {consulta.data_nasc.strftime("%d/%m/%Y")}\n'
            f'Ativo: {consulta.ativo}\n'
            f'Data do cadastro: {consulta.data_cadastro}'
        )

def login():
    email = input('Email: ')
    senha = input('Senha: ')

    session.query(Usuario).filter(Usuario==email, Usuario.senha==senha)

if __name__ == '__main__':
    consultar()