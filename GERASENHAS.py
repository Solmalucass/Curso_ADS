
# Gerador de senha aleatória com random

import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation # Caracteres que podem ser usados na senha

    senha = []

    for _ in range(tamanho):
        senha.append(random.choice(caracteres))# Adiciona caracteres aleatórios a senha

    return ''.join(senha)# Retorna a senha como uma string

senha_gerada = gerar_senha(16) # Gera uma senha de 16 caracteres
print("Senha nova gerada:", senha_gerada)


