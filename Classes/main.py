# -*- coding: utf-8 -*-

#Fabricio de Lima Ribeiro
#01/12/2020
#Exemplo de uso de classes
#para executar: $ python main.py

from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

a = PessoaFisica('111.222.333-4', nome='Alfredo', idade=22)

print(a.getCPF())
print(a.getNome())
print(a.getIdade())

b = PessoaJuridica('64.614.527/0001-99', nome='Empresa X', idade=22)

print(b.getCNPJ())
print(b.getNome())
print(b.getIdade())

b.setIdade(40)

print(b.getCNPJ())
print(b.getNome())
print(b.getIdade())