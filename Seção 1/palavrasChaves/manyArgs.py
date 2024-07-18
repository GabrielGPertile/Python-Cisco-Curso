#Sem o end=""
print("Meu nome é", "Python.")
print("Monty Python.\n")

#Com o end="" com algum caracte
print("Meu nome é", "Python.", end=" ")
print("Monty Python.")

#Com o end="" mas sem caracte
print("Meu nome é ", end="")
print("Monty Python.")

#Utilizando o sep
#sep="" nas aspas sera coloca um ou mais carateces para demonstrar a separação
print("Meu", "nome", "é", "Monty", "Python.", sep="-")

#Misturando as palavras-chaves end e sep
print("Meu", "nome", "é", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

#Exercio 2.1.12   LAB   A função print() e seus argumentos
print("Programação","Essenciais","em", sep="***", end="...")
print("Python")
