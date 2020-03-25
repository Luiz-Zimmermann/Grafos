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

def buscaP():
    visitadosList = []
    for x in dicio:
        visitadosList.append(dicio[x].id)

    for x in range(tan):
        for y in range(tan):
            if(matriz[x,y]==1):
                pass


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
nodesList = []

dicio = {}

#Pegando a quantidade de vertices e criando os objetos node
for x in range(tan):
    nodesList.append(node(vertices.split(",")[x],x))
    dicio[vertices.split(",")[x]] = node(vertices.split(",")[x], x)
for x in nodesList:
    print(x.name,x.id)

#Criando matriz
matriz = np.zeros((tan,tan))
print(matriz)

edges = input("Informe as ligações.(Ex: a:b,c,d ; b:a,c,f):")
s = edges.split(";")

#Pegando os vertices adjacentes de cada vertice
for x in s:   #x:y
   # vertList.append(x.split(":")[0])
    dicio[x.split(":")[0]].adj = x.split(":")[1].split(",")

#Fazendo as ligações, usando a lib
for x in dicio:
    print(dicio[x].name +": " + str(dicio[x].id))
    for y in dicio[x].adj:
        if(dic == "S"):
            matriz[dicio[x].id, dicio[y].id] = 1
        else:
            matriz[dicio[x].id, dicio[y].id] = 1
            matriz[dicio[y].id, dicio[x].id] = 1

        print(dicio[x].name +": "+y)
        edge = (dicio[x].name, y)
        G.add_edge(*edge)


if(input("Deseja realizar uma busca?(S ou N)")=="S"):
    if(input("Por profundidade ou largura?(P ou L)")=="P"):
        buscaP()
    else:
        buscaL()


print(matriz)
print("-------------------------------")

vertList = []
edgeList = []

print(G.edges())
nx.draw(G, with_labels="true")
plt.show() # display

#https://www.alura.com.br/artigos/trabalhando-com-o-dicionario-no-python