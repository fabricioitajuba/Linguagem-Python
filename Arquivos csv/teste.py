import csv

with open('profissoes.csv', 'w') as arquivo_csv:
    colunas = ['nome', 'profissao']
#    escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=',', lineterminator='\n')
    escrever = csv.DictWriter(arquivo_csv, fieldnames=colunas, delimiter=';', lineterminator='\n')
    escrever.writeheader()
    escrever.writerow({'nome': 'Renato', 'profissao': 'programador'})
    escrever.writerow({'nome': 'Yanka', 'profissao': 'programadora'})


