palavras = ["maça", "banana", "maça", "laranja", "banana", "banana"]

estudantes = {
    "João": 8.5,
    "Maria": 9.0,
    "Pedro": 7.5
}

d = {}

def conta (p):
    for i in p:
        d[i] = d.get(i,0) + 1

#conta(palavras)

alunos = {}

def add(nome = None, nota=None):
    alunos[nome] = nota

def remove(nome = None):
    alunos.pop(nome)

'''add("lucas", 9.5)

print(alunos)

remove("lucas")

print(alunos)'''

produtos = [("maçã", 2.5), ("banana", 1.0), ("laranja", 3.0)]

def LforD(lista):
    for key in lista:
        print(key)
        d[key[0]] = key[1] 

LforD(produtos)

print(d)