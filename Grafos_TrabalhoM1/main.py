import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class node:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    name =""
    id = 0
    visit = 0
    adj = []

def buscaPr(ver):
    pilha = []
    visitados =[]
    pilha.append(ver)
    while pilha:
        v = pilha.pop()
        print("sequencia: "+v)
        if v == "d":
            print("encontrado")
            return
        for vizinho in grafo[v].adj:
            if vizinho not in visitados:
                visitados.append(vizinho)
                pilha.append(vizinho)




def buscaP(verticeInic, verticeProc):
    visitadosList = [verticeInic]

    def buscaRecur(verticeI, verticeP):
        for node in grafo[verticeI].adj:
            if grafo[node].name not in visitadosList:
                visitadosList.append(node)
                print("sequencia: "+node)

                if verticeP == node:
                    print("Vertice "+node+" encontrado!!")
                    #variavel para dizer se foi encontrado ou nao
                    findSuc = 1
                    return
                else:
                    buscaRecur(node, verticeP)

    buscaRecur(verticeInic,verticeProc)

    #verificar se o vertice foi achado na busca anterior
    while(1==1):
        for x in grafo:
            if(grafo[x].name not in visitadosList):
                buscaRecur(grafo[x].name, verticeProc)

        if(len(visitadosList) == tan):
            break;

    print("Vertice não encontrado no grafo!!!!")



def buscaL():
    pass


dic = input("O grafo é direcional ou não?(S ou N):")
if dic == "S":
    G = nx.DiGraph()
else:
    G = nx.Graph()

vertices = input("Informe os vertices.(Ex: a,b,c,d):")
G.add_nodes_from(vertices.split(","))
tan = len(vertices.split(","))

grafo = {}

#Pegando a quantidade de vertices e criando os objetos node para cada vertice
for x in range(tan): #key          value: nome e id
    grafo[vertices.split(",")[x]] = node(vertices.split(",")[x], x)
    print(vertices.split(",")[x], x)

#Criando matriz
matriz = np.zeros((tan,tan))
print(matriz)

edges = input("Informe as ligações.(Ex: a:b,c,d ; b:a,c,f):")
s = edges.split(";")

#Pegando os vertices adjacentes de cada vertice
for x in s:   #x:y
    grafo[x.split(":")[0]].adj = x.split(":")[1].split(",")

#Fazendo as ligações, usando a lib e preenchendo a matriz
for x in grafo:
    print(grafo[x].name + ": " + str(grafo[x].id))
    for y in grafo[x].adj:
        if(dic == "S"):
            matriz[grafo[x].id, grafo[y].id] = 1
        else:
            matriz[grafo[x].id, grafo[y].id] = 1
            matriz[grafo[y].id, grafo[x].id] = 1

        print(grafo[x].name + ": " + y)
        edge = (grafo[x].name, y)
        G.add_edge(*edge)

buscaPr("a")

if(input("Deseja realizar uma busca?(S ou N)")=="S"):
    if(input("Por profundidade ou largura?(P ou L)")=="P"):
        buscaP(input("Deseja começar por qual vertice?: "),input("Procurar vertice: "))
    else:
        buscaL()

print(matriz)
print("-------------------------------")

print(G.edges())
nx.draw(G, with_labels="true")
plt.show() # display

#https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python
#https://www.caelum.com.br/apostila-python-orientacao-objetos/funcoes/#funo-com-retorno
#https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/busca-profundidade