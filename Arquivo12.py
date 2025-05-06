from AULA07.Arquivo05 import media

n=[0]*10
for i in range(10):
    n[i]=int(input("digite um numero:"))
print("\nnumeros pares")
for numero in n:
    if numero % 2 == 0:
        print(numero)
maior=n[0]
menor=n[0]
for x in range(1,10):
    if n[x]<menor:
        menor=n[x]
    if n[x]>maior:
        maior=n[x]
print(f"\nmenor valor:{menor}")
print(f"\nmaior valor: {maior}")
soma=0
for k in range(10):
    soma+=n[k]
media=soma/10
maiorquemrdia=0
for p in range(10):
    if n[p]>media:
        maiorquemrdia+=1
print(f" media dos valores:{media}")
print(f"quantidade de valores maior que media es media:{maiorquemrdia}")