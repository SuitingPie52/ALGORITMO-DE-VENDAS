# a) Menu para chamada das opções;
# b) Ler os dados e quantidades vendidas
# c) Cálculo do faturamento
# d) Impressão do faturamento discriminando as mercadorias e preços, bem como a
# totalização de vendas conforme a equação número 1.
# e) Percentuais de vendas por mercadoria sobre o total faturado.
# f) Gravar os dados das vendas em arquivos tipo txt.
# g) Imprimir gráfico de vendas para as cinco mercadorias mais vendidas no referido mês. No
# eixo x do gráfico deverá conter as mercadorias e no eixo y do gráfico as quantidades
# vendidas. *\

import random
import matplotlib.pyplot as plt


def menu():  # a)

    opcao = 0

    while opcao != -1:

        print("\n|=========================================|\n"
              "|   BEM-VINDO, O QUE VOCÊ DESEJA FAZER?   |\n"
              "|=========================================|\n"
              "| 1 - Ler os dados e quantidades vendidas |\n"
              "| 2 - Cálculo do faturamento              |\n"
              "| 3 - Impressão dos dados                 |\n"
              "| 4 - % de vendas/faturamento             |\n"
              "| 5 - Gravar em .txt                      |\n"
              "| 6 - Gráfico dos mais vendidos           |\n"
              "|=========================================|\n"
              "| -1 - Encerrar programa                  |\n"
              "|=========================================|\n\n")

        opcao = int(input("Qual comando você deseja executar? "))

        if opcao == 1:

            p = inputDados()

        elif opcao == 2:

            print("Seu faturamento total foi:", faturamento(p))

        elif opcao == 3:

            printTotalizacao(p)

        elif opcao == 4:

            mercadoriaPorTotal(p)

        elif opcao == 5:

            passarParaTexto(p)

        elif opcao == 6:

            grafico(p)


def inputDados():  # b)
    produtos = {

    }

    for i in range(1, 101):
        # fiz de forma randomica para não precisar digitar os dados 100 vezes, mas caso queira inserir o valor
        # manualmente, é so substituir os random.randint() por int(input())

        print("\nQual é o valor do produto ", i, "?", sep="", end="")
        x = random.randint(1, 100)
        print("\nE a quantidade de produtos ", i, " que foram vendidos?\n", sep="", end="")
        y = random.randint(1, 10)

        z = {

            str(i): (x, y)  # o primeiro valor da chave vai ser o preço, e o segundo a quantidade vendida

        }

        produtos.update(z)

    return produtos


def faturamento(produtos):  # c)
    soma = 0

    for _, valor in produtos.items():
        x, y = valor
        soma += x * y

    return soma


def printTotalizacao(produtos):  # d)
    soma = 0
    vendidos = 0

    for chave, valor in produtos.items():
        x, y = valor
        print("\nO produto ", chave, " tem preço ", x, " foi vendido ", y, " vezes, e teve faturamento de ",
              x * y, sep="", end="")

        soma += x * y
        vendidos += y

    print("\nO TOTAL DE PRODUTOS VENDIDOS É:", vendidos, "\nO TOTAL FATURADO É:", soma)


def mercadoriaPorTotal(produtos):  # e)
    total = faturamento(produtos)

    for chave, valor in produtos.items():
        x, y = valor

        print("A chave", chave, "representa", ((x * y) / total)*100, " por cento do total do faturamento")


def passarParaTexto(produtos):  # f)

    vendidos = 0
    total = faturamento(produtos)

    with open('arquivo.txt', 'w') as arquivo:
        for chave, valor in produtos.items():
            x, y = valor
            arquivo.write("\nProduto: " + str(chave) + "/ Preco: " + str(x) + "/ Qtd vendida: " + str(y) +
                          "/ Faturamento: " + str(x * y) + "/ Percentual do total: " + str((x * y / total)*100))
            vendidos += y

        arquivo.write("\nTOTAL DE PRODUTOS VENDIDOS: " + str(vendidos) + "\nTOTAL FATURADO: " + str(total))


def grafico(produtos):  # g)

    # Classifica as chaves com base nos valores de y em ordem decrescente
    maiores5 = sorted(produtos.items(), key=lambda item: item[1][1], reverse=True)

    # Pega as 5 primeiras chaves e seus respectivos valores
    maiores5 = maiores5[:5]

    x = []
    y = []

    for i in maiores5:
        x.append(i[0])
        y.append(i[1][1])

    plt.plot(x, y)
    plt.show()


menu()
