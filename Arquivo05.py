nota=[0,0,0,0,0]
soma=0
cont=0
for i in range(len(nota)):
    nota[i]=float(input("Digite a nota dos alunos:"))
    soma+=nota[i]
media=soma/i

for x in range(len(nota)):
    if nota[x] > media:
        cont+=1
print(media)
print(cont)