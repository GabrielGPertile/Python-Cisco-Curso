#Pergunta 2: Qual é a saída do seguinte programa?
#jeito errado
#print(sep="&", "peixe", "salgadinhos") 

# Resposta:
#Vai dar um erro, pois o posicionamento do sep está fora de ordem.
#Primeiro tem que vir o "peixe", "salgadinhos" e por fim a 
#palavra chave sep="&"

#jeito certo
print("peixe", "salgadinhos", sep="&")

