nomes=["","","","","",""]
for i in range(len(nomes)):
    nomes[i]=input("digite os nomes que deseja: ")

for nome in nomes:
    print(nome)
nome=input("digite o nome que quer achar: ")
cont=0
for j in range(len(nomes)):
    if nome==nomes[j]:
        print(f"seu nome foi :{nome},encontrado na posição {j}!")
        cont+=1
if cont == 0:
    print("nome não encontrado")