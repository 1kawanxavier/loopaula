tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha: ")
    if senha == "senha123":
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta. Tente novamente")
        tentativas +=1
else:
    print("você execedeu o número máximo de tentativas.")
    