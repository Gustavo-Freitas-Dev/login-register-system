import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.connection import session
from database.models import Usuario

# adicionar_conta = Usuario('Guuh Black', '19/01/2004', 'Guuh_black@gmail.com', 'Guuh2163k@')
# session.add(adicionar_conta)
# session.commit()

nome = 'Guuh Black'
data_nasc = '19/01/2004'
email = 'Guuh_black02@gmail.com'
senha = 'Guuh2163k@'

def cadastrar_usuario(email):

    consulta = session.query(Usuario).filter(Usuario.email==email).first()

    if consulta:
        print('Esse email já possui conta em nosso site')
    else:
        print('E-mail cadastrado com sucesso!!!')

cadastrar_usuario(email)