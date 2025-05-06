n=[0]*3
for i in range(3):
    n[i]=int(input("digite um valor: "))
a=int(input("digite mais um valor: "))
contador=0
for j in range(3):
    if n[j]==a:
        contador+=1
print(f"o numero {a} aparece {contador} vez(es) no vetor.")