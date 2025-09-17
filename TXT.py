import datetime

data_atual = datetime.date.today()

with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    palavras = texto.split()
    quant = len(palavras)
    
with open('texto.txt', 'a') as arquivo:
    arquivo.write(f'\nData: {data_atual}')
    arquivo.write(f'\nPalavras: {quant}')
