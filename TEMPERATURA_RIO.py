
# Pergunta ao usuário a temperatura do rio de janeiro e retorna se vai precisar de casaso ou não."""

def vouusarcasacohoje(): # Função que pergunta a temperatura atual no Rio de Janeiro

  temperatura = float(input("Qual a temperatura atual no Rio de Janeiro? ")) 
  return temperatura

def precisa_de_casaco(temperatura): # Função que retorna se vai precisar de casaco ou não
  
  if temperatura <= 26:
    return "É melhor colocar um casaco. Está um pouco frio!"
  else:
    return "Não precisa de casaco. O dia está quente!"

temperatura_atual = vouusarcasacohoje()
mensagem = precisa_de_casaco(temperatura_atual)
print(mensagem)