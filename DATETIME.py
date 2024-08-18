
#Função que retorna uma saudação de acordo com a hora atual do sitema."""

import datetime

def saudaçao():
    agora = datetime.datetime.now() #Pega a hora atual do sistema
    hora = agora.hour

    if 5 <= hora < 12:
        return "Pelo o horario do seu sistema está de dia, então, Bom dia!"
    elif 12 <= hora < 18:
        return "Pelo o horario do seu sistema está de tarde, então, Boa tarde!"
    else:
        return "Pelo o horario do seu sistema está de noite, então, Boa noite!"

sauda = saudaçao()
print(sauda)
