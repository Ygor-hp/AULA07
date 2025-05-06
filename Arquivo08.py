user=[""]*1
senha=[0]*1
for i in range(len(user)):
    user[i]=input("Digite usuario: ")
    senha[i]=input("digite senha:")
login=input("user:")
password=input("password:")
for i in range(len(user)):
    if user[i]==login and senha[i]==password:
        login=True
        print("login efetuado com sucesso!")
        break
else:
    print("acesso negado")