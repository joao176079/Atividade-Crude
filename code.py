import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pesquisa:
    nome: str
    numero_de_filhos_por_familia: int
    salario: float

def media(a, b):
    return a / b if b > 0 else 0

def maior_menor(lista):
    menor = min(lista) if lista else 0
    maior = max(lista) if lista else 0
    return maior, menor

lista_de_familias = []
lista_de_salarios = []

# Começando o laço de repetição
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
            # Solicitando dados
            familia = Pesquisa(
                nome=input("Digite seu nome: "),
                numero_de_filhos_por_familia=int(input("Digite o número de filhos na sua família: ")),
                salario=float(input("Digite seu salário: "))
            )
            lista_de_familias.append(familia)
            lista_de_salarios.append(familia.salario)
            os.system("cls || clear")

        case 2:
            # Exibindo dados
            print("\n=== Exibindo dados ===")
            for clthanos in lista_de_familias:
                print(f"Nome: {clthanos.nome}")
                print(f"Número de filhos: {clthanos.numero_de_filhos_por_familia}")
                print(f"Salário: {clthanos.salario}")

            # Exibindo maior e menor salário
            if lista_de_salarios:
                maior_salario, menor_salario = maior_menor(lista_de_salarios)
                print(f"\nMaior salário: {maior_salario:.2f}")
                print(f"Menor salário: {menor_salario:.2f}")

            # Cálculo da média
            if lista_de_familias:
                total_filhos = sum(familia.numero_de_filhos_por_familia for familia in lista_de_familias)
                media_filhos = media(total_filhos, len(lista_de_familias))
                print(f"\nMédia de filhos por família: {media_filhos:.2f}")

        case 3:
            nome_do_arquivo = "pesquisa_prefeitura.txt"
            with open(nome_do_arquivo, "a") as pesquisatds:
                for clthanos in lista_de_familias:
                    pesquisatds.write(f"{clthanos.nome}, {clthanos.salario}, {clthanos.numero_de_filhos_por_familia}\n")
            break

# Lendo do arquivo e exibindo dados
print("\n=== Exibindo dados das famílias a partir do arquivo ===")
with open("pesquisa_prefeitura.txt", "r") as todos_alunos:
    for linha in todos_alunos:
        nome, salario, numero_de_filhos_por_familia = linha.strip().split(",")
        lista_de_familias.append(Pesquisa(nome=nome, salario=float(salario), numero_de_filhos_por_familia=int(numero_de_filhos_por_familia)))

for clthanos in lista_de_familias:
    print(f"Nome: {clthanos.nome}")
    print(f"Número de filhos: {clthanos.numero_de_filhos_por_familia}")
    print(f"Salário: {clthanos.salario}")
