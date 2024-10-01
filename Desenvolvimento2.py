import os 
from dataclasses import dataclass

os.system("cls || clear")
nome_do_arquivo = "pesquisa_prefeitura.txt"

@dataclass
class Pesquisa :
   nome :  str
   numero_de_filhos_por_familia : int
   salario : float



def maior_menor():
    menor = min(lista_de_salarios)
    maior = max(lista_de_salarios)
    return maior, menor

lista_de_familias = []
lista_de_salarios = []
familias = []

numero_ee_familias
contador_salario = len(lista_de_salarios)

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
           lista_de_salarios.append({familia.salario})
           lista_de_familias.append({familia.numero_de_filhos_por_familia})
           os.system("cls || clear")
           with open(nome_do_arquivo, "a") as pesquisa:
                for clthanos in familia:
                    pesquisa.write(f"{clthanos.nome}, {clthanos.sobrenome}, {clthanos.idade}, {clthanos.peso},{clthanos.altura}\n")
        case 2 :
            #exibindo dados
            print("\n=== Exibindo dados ===")
            for clthanos in familia:
                print(f"Nome: {clthanos.nome} ")
                print(f"Sobrenome: {clthanos.numero} ")
                print(f"Idade: {clthanos.idade} ")
                print(f"Seso: {clthanos.peso} ")
                print(f"Altura: {clthanos.altura} ")
            with open (nome_do_arquivo, "r") as todos_alunos:
                for linha in familia:
                  nome,sobrenome,idade,peso, altura = linha.strip().split(",")
                  familias.append(pesquisa(nome=nome,salario=int(), idade=int(idade),peso = float(peso), altura=float(altura)))
        case 3:
            #parando o codigo
            pesquisa.close()
            break

#Salvar em um arquivo chamado: pesquisa_prefeitura.txt


