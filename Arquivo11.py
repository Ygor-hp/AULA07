user=[""]*3
for i in range(3):
    user[i]=input("digite o nome para usar: ")
print("normal")
for nome in user:
    print(nome)
print("inverso:")
for x in range(2,-1,-1):
    print(user[x])