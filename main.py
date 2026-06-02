# votos = [0, 0, 0, 0, 0, 0]

# print("1 - Windows Server")
# print("2 - Unix")
# print("3 - Linux")
# print("4 - Netware")
# print("5 - Mac OS")
# print("6 - Outro")

# voto = int(input("Digite seu voto (0 para encerrar): "))

# while voto != 0:

#     if voto >= 1 and voto <= 6:
#         votos[voto - 1] += 1
#     else:
#         print("Voto inválido!")

#     voto = int(input("Digite seu voto (0 para encerrar): "))

# total = sum(votos)

# print("\nSistema Operacional\tVotos\t%")
# print("------------------------------------")

# print("Windows Server\t\t", votos[0], "\t", round(votos[0] * 100 / total, 2), "%")
# print("Unix\t\t\t", votos[1], "\t", round(votos[1] * 100 / total, 2), "%")
# print("Linux\t\t\t", votos[2], "\t", round(votos[2] * 100 / total, 2), "%")
# print("Netware\t\t\t", votos[3], "\t", round(votos[3] * 100 / total, 2), "%")
# print("Mac OS\t\t\t", votos[4], "\t", round(votos[4] * 100 / total, 2), "%")
# print("Outro\t\t\t", votos[5], "\t", round(votos[5] * 100 / total, 2), "%")

# print("------------------------------------")
# print("Total:", total)

# maior = votos[0]
# vencedor = "Windows Server"

# if votos[1] > maior:
#     maior = votos[1]
#     vencedor = "Unix"

# if votos[2] > maior:
#     maior = votos[2]
#     vencedor = "Linux"

# if votos[3] > maior:
#     maior = votos[3]
#     vencedor = "Netware"

# if votos[4] > maior:
#     maior = votos[4]
#     vencedor = "Mac OS"

# if votos[5] > maior:
#     maior = votos[5]
#     vencedor = "Outro"

# print("\nO Sistema Operacional mais votado foi o",
#       vencedor, "com", maior, "votos.")






# def solicitaSalario():
#   salario = float(input("Salário: "))
#   return salario

# salarios = []
# abonos = []

# salario = solicitaSalario()

# while salario != 0:

#   salarios.append(salario)

#   abono = salario * 0.20

#   if abono < 100:
#       abono = 100

#   abonos.append(abono)

#   salario = solicitaSalario()

# print("\nSalário - Abono")

# i = 0
# while i < len(salarios):
#   print("R$", salarios[i], "- R$", abonos[i])
#   i += 1

# print("\nForam processados", len(salarios), "colaboradores")

# total = 0
# for abono in abonos:
#   total += abono

# print("Total gasto com abonos: R$", total)

# minimo = 0
# for abono in abonos:
#   if abono == 100:
#       minimo += 1

# print("Valor mínimo pago a", minimo, "colaboradores")

# maior = 0
# for abono in abonos:
#   if abono > maior:
#       maior = abono

# print("Maior valor de abono pago: R$", maior)






# # --- ENTRADA DE DADOS ---
# # Criando as listas com os modelos e consumos fornecidos no exemplo
# modelos = ["Fusca", "Gol", "Uno", "Vectra", "Peugeout"]
# consumos = [7.0, 10.0, 12.5, 9.0, 14.5]

# # Constantes do problema
# distancia = 1000
# preco_gasolina = 2.25

# for i in range(5):
#     print(f"Veículo {i + 1}")
#     print(f"Nome: {modelos[i]}")
#     print(f"Km por litro: {consumos[i]}")

# # Variáveis para descobrir qual é o carro mais econômico
# maior_km_por_litro = consumos[0]
# indice_mais_economico = 0

# # Laço para calcular o consumo de cada carro e imprimir a linha
# for i in range(5):
#     # Calcula quantos litros precisa para andar 1000 km
#     litros_necessarios = distancia / consumos[i]
#     # Calcula o custo total com base nos litros calculados
#     custo_total = litros_necessarios * preco_gasolina

#     # Imprime a linha do relatório formatada com uma casa decimal para litros e duas para dinheiro
#     print(f"{i + 1} - {modelos[i]} - {consumos[i]} - {litros_necessarios:.1f} litros - R$ {custo_total:.2f}")

#     # Lógica simples para testar qual carro faz mais km por litro
#     if consumos[i] > maior_km_por_litro:
#         maior_km_por_litro = consumos[i]
#         indice_mais_economico = i

# # Imprime o carro que gasta menos combustível
# carro_economico = modelos[indice_mais_economico]
# print(f"O menor consumo é do {carro_economico}.")







# mouses = [0, 0, 0, 0]

# defeito = int(input("Digite o defeito (1 a 4) ou 0 para sair: "))

# while defeito != 0:

#     if defeito == 1:
#         mouses[0] += 1

#     elif defeito == 2:
#         mouses[1] += 1

#     elif defeito == 3:
#         mouses[2] += 1

#     elif defeito == 4:
#         mouses[3] += 1

#     defeito = int(input("Digite o defeito (1 a 4) ou 0 para sair: "))

# total = mouses[0] + mouses[1] + mouses[2] + mouses[3]

# print("\nQuantidade de mouses testados:", total)

# print("\nSituação\t\tQuantidade\tPercentual")

# print("1 - necessita da esfera\t", mouses[0], "\t\t", round(mouses[0] * 100 / total), "%")
# print("2 - necessita de limpeza", mouses[1], "\t\t", round(mouses[1] * 100 / total), "%")
# print("3 - troca cabo/conector", mouses[2], "\t\t", round(mouses[2] * 100 / total), "%")
# print("4 - quebrado/inutilizado", mouses[3], "\t\t", round(mouses[3] * 100 / total), "%")