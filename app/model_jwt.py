#pip install PyJWT
import datetime
import os
import jws

# Gera a chave secreta aleatória uma vez e a armazena em uma variável global
chave_secreta = os.urandom(32)

def gerar_token_administrador(administrador_id):
    try:
        # Define as informações a serem incluídas no token
        payload = {
            'administrador_id': administrador_id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Define o tempo de expiração do token
        }

        # Gera o token JWT usando a chave secreta aleatória
        token = jwt.encode(payload, chave_secreta, algorithm='HS256')

        return token.decode()  # Retorna o token como uma string decodificada

    except Exception as e:
        # Ocorreu um erro ao gerar o token
        print("Erro ao gerar o token:", str(e))
        return None

print(gerar_token_administrador(1))
