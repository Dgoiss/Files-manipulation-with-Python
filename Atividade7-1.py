import csv

with open('produtos.csv', 'w', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['Produto', 'Preco'])
    quant = int(input('Quantidade de produtos: '))
    for i in range(quant):
        nome_produto = str(input('Nome do produto: '))
        preco_produto = float(input('Preco do produto: '))
        writer.writerow([nome_produto, preco_produto])

soma = 0
with open('produtos.csv', 'r') as arquivo:
    reader = csv.reader(arquivo)
    next(reader)
    for linha in reader:
        preco = float(linha[1])
        soma += preco

media = soma/quant
print(media)