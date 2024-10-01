#nome dos componentes: bruno henrique alves santos, joao vitor mendes
#n° da turma: 933313

import os 
from dataclasses import dataclass

os.system("cls || clear")


@dataclass
#cria uma classe 
class Pesquisa :
   nome :  str
   numero_de_filhos_por_familia : int
   salario : float
#medias para salario e o menor e maior salario
def media(a,b):
      mediafim = a/b 
      return mediafim
def maior_menor(a):
    menor = min(lista_de_salarios)
    maior = max(lista_de_salarios)
    return maior, menor

lista_de_familias = []
lista_de_salarios = []

#adicionando os contadores
numero_de_familias = 0
contador_salario = 0
contador_filhos = 0

#começando o laço de repetição
while True:
    print("""
            === Menu ===
    |Código |     Descrição     |            
    |   1   | Adicionar família |                
    |   2   | Exibir resultados |          
    |   3   | Sair              |  
    """)
    menu = int(input("Digite uma opção: "))
    os.system("cls || clear")
    match menu:
        case 1:
           #solicitando dados
           familia = Pesquisa(
               nome = input("Digite seu nome: "),
               numero_de_filhos_por_familia = int(input("digite o números de filhos na sua familia: ")),
               salario = float(input("Digite seu salário: "))
           )
           lista_de_familias.append(familia)
           lista_de_salarios.append(familia.salario)
           contador_salario += 1
           numero_de_familias += 1
           
           os.system("cls || clear")
           
        case 2 :
            #exibindo dados
            print("\n=== Exibindo dados ===")
            for clthanos in lista_de_familias:
                print(f"Nome: {clthanos.nome} ")
                print(f"numeros de filho: {clthanos.numero_de_filhos_por_familia} ")
                print(f"salario: {clthanos.salario} ")
             # Exibindo maior e menor salário
            if contador_salario > 1:
        
                maior_salario, menor_salario = maior_menor(lista_de_salarios)
                media_salario = media(sum(lista_de_salarios),(len(lista_de_salarios)))
                print(f"\nMaior salário: {maior_salario:.2f}")
                print(f"\nMenor salário: {menor_salario:.2f}")
                print(f"\nA média dos salários foram: {media_salario}")
            if numero_de_familias > 1:
                    
                    quantidade_familias = len(lista_de_familias)
                    contador_filhos = 0
                    for familia in lista_de_familias:
                        contador_filhos += familia.numero_de_filhos_por_familia

                    media_filhos = media(contador_filhos, quantidade_familias)
                    print(f"\nMédia de filhos por família: {media_filhos:.2f}")
            
        case 3:
            #colocando os aruivos no txt
            # #Salvar em um arquivo chamado: pesquisa_prefeitura.txt
            nome_do_arquivo = "pesquisa_prefeitura.txt"
            with open(nome_do_arquivo, "a") as Pesquisadts:
                            for clthanos in lista_de_familias:
                                Pesquisadts.write(f"{clthanos.nome}, {clthanos.salario}, {clthanos.numero_de_filhos_por_familia}\n")
            break




                
                
with open (nome_do_arquivo, "r") as todos_alunos:
                for linha in lista_de_familias:
                  nome,salario, numero_de_filhos_por_familia = linha.strip().split(",")
                  lista_de_familias.append(Pesquisadts(nome=nome,salario=float(salario), numero_de_familias=int(numero_de_filhos_por_familia)))

print("\n=== exibindo dados das familias ===")
for clthanos in lista_de_familias:
    for clthanos in lista_de_familias:
                print(f"Nome: {clthanos.nome} ")
                print(f"numeros de filho: {clthanos.numero_de_filhos_por_familia} ")
                print(f"salario: {clthanos.salario} ")

#parando o codigo
Pesquisadts.close()