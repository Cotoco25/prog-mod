# -*- coding: utf-8 -*-

# a) Escreva uma função (não recursiva), denominada substituiVogais,
# que  receba uma string e um caractere e construa e retorne 
# uma nova string com todas as vogais da string original  
# substituídas pelo caractere recebido 
# OBS: substitui não é um BOM nome, pois não é possível 
# fazer  substituições na string recebida
# STRING é IMUTÁVEL 

def substituiVogais(st, novoc):
    ns=''
    for carac in st:
        if carac in 'aeiouAEIOU':
            ns = ns+ novoc    # ns+=novoc
        else:
            ns = ns + carac 
    return ns 

#BP
novaSt= substituiVogais('Roupa','*')
print(novaSt)
    