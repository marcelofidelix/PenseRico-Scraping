# -*- coding: utf-8 -*-
import pandas as pd

f = open('dados.txt', 'r')

#Lê o arquivo, remove os \t e cria uma lista com um elemento para cada linha
s = f.read().replace('\t', '').split('\n')
#Fecha o arquivo
f.close()
#Remove elementos vazios
s = [el for el in s if el != '']

#Captura os anos em uma lista e remove o espaço em branco
anos = s[0].split(' ')
anos.remove('')
#Removemos oprimeiro elemento da lista (os anos)
s = s[1:]
#Substitui . por '' (valores maiores que 1.000!)
s = [el.replace('.', '') for el in s]
#Substitui as , por .
s = [el.replace(',', '.') for el in s]

#Remove os número (dados agrupados por ano)
inds = [el for el in s if el[0].isalpha()]
#Remove os itens que são índices
s = [el for el in s if el not in inds]

#Lista com os trimestres
trims = ['1T', '2T', '3T', '4T']
#Valores iniciais para os índices
cont_ano = -1
cont_trim = -1
cont_ind = -1
#Listas vazias para receber os dados
lista_anos = []
lista_trims = []
lista_inds = []
#Define os primentos valores das listas
ano = anos[0]
trim = trims[0]
ind = inds[0]

for i in range(len(s)):
    
    if s[i][:2] not in trims:
        try:
            cont_ano += 1
            ano = anos[cont_ano]
        except:
            cont_ano = 0
            ano = anos[cont_ano]
            
            cont_ind += 1
            ind = inds[cont_ind]
            
    lista_anos.append(ano)
    lista_inds.append(ind)

    if s[i][:2] in trims:
        try:
            cont_trim += 1
            trim = trims[cont_trim]        
        except:
            cont_trim = 0
            trim = trims[cont_trim]
    lista_trims.append(trim)

#Remove as linhas com os valores anuais
#Índices dos elementos a serem removidos
rem_ind = []
for i in range(len(s)):
    if s[i][1] != 'T':
        rem_ind.append(i)
#Itera sobre a lista de índices a remover e remove os elementos correspondentes
for i in rem_ind:
    lista_anos[i] = "Remover!"
    lista_inds[i] = "Remover!"
    lista_trims[i] = "Remover!"
    s[i] = "Remover!"
#Remove os itens marcados para remoção
lista_anos = [el for el in lista_anos if el !='Remover!']
lista_inds = [el for el in lista_inds if el !='Remover!']
lista_trims = [el for el in lista_trims if el !='Remover!']
s = [el for el in s if el !='Remover!']
#Remove os símbolos de %
s = [el[:-1] if '%' in el else el for el in s]
#Transforma os elementos da lista s em números
s = [float(el[3:]) for el in s ]

dic = {'Ano': lista_anos,
       'Trim': lista_trims,
       'Ind': lista_inds,
       'Valor': s}

df = pd.DataFrame(dic)

print(df)
