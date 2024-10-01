import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pesquisa :
    total_de_familias : int
    media_salario_populacao : float
    media_numero_de_filhos : int 
    maior_salario : float
    menor_salario : float

PESQUISA_DIGITALIZADA = int (input ("Digite a quantidade de familias"))
lista_de_clientes = []

for i in range (PESQUISA_DIGITALIZADA):

    total_de_familias = int (input ("Digite o total de familias: "))
    media_salario_populacao = input ("A quantidade de média da população: ")
    media_numero_de_filhos = input ("A quantidade da média de filhos: ")
    maior_salario = int (input ("Maior salário: "))
    menor_salario = int (input ("Menor salário: "))
    