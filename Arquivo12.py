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
