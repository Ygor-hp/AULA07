def imprime_nome(nome):
    print(f"nome:{nome}")

def solicitar_nome():
    nome=input("Digite seu nome: ")
    return nome

def piramid(num):
    for i in range(1, num + 1, 1):
        for x in range(0, i):
            print(i, end=" ")
        print()

def vogais (text):
    cont = 0
    vogai="aeiouAEIOU"
    for i in range(0, len(text)):
        if text[i] in  vogai:
            cont = cont + 1
            print(cont)

def stoque(produto,quantidade,valor1):
    valortotal=quantidade*valor1
    print(valortotal)


def positivo(numero):
    if numero != 0:
        if numero > 0:
            return "P"
        else:
            return "N"
    else:
        return "Z"

def soma(*a):
    soma=0
    for x in range(len(a)):
        soma=soma+a[x]
    print(soma)    