# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:16:46 2026

@author: joisa
"""

def calcular_valor_final(capital_inicial, taxa_mensal, meses):
    """
    Calcula o valor final de um investimento com juros compostos mensais.
    
    Args:
        capital_inicial (float): Valor inicial investido (R$)
        taxa_mensal (float): Taxa de rendimento mensal (%)
        meses (int): Número de meses do investimento
    
    Returns:
        float: Valor final do investimento (R$)
    """
    return capital_inicial * (1 + taxa_mensal / 100) ** meses


def avalia_dois_investimentos(inv1_capital, inv1_taxa, inv1_meses, 
                               inv2_capital, inv2_taxa, inv2_meses):
    """
    Avalia e compara dois investimentos, exibindo seus detalhes e qual teve mais lucro.
    
    Args:
        inv1_capital (float): Capital inicial do primeiro investimento
        inv1_taxa (float): Taxa mensal do primeiro investimento (%)
        inv1_meses (int): Meses do primeiro investimento
        inv2_capital (float): Capital inicial do segundo investimento
        inv2_taxa (float): Taxa mensal do segundo investimento (%)
        inv2_meses (int): Meses do segundo investimento
    """
    # Calculando valores finais usando a função do item (a)
    valor_final1 = calcular_valor_final(inv1_capital, inv1_taxa, inv1_meses)
    valor_final2 = calcular_valor_final(inv2_capital, inv2_taxa, inv2_meses)
    
    # Calculando lucros
    lucro1 = valor_final1 - inv1_capital
    lucro2 = valor_final2 - inv2_capital
    
    # Exibindo resultados do primeiro investimento
    print("\n" + "="*50)
    print("INVESTIMENTO 1")
    print("="*50)
    print(f"Capital inicial: R$ {inv1_capital:.2f}")
    print(f"Valor final: R$ {valor_final1:.2f}")
    print(f"Lucro: R$ {lucro1:.2f}")
    
    # Exibindo resultados do segundo investimento
    print("\n" + "="*50)
    print("INVESTIMENTO 2")
    print("="*50)
    print(f"Capital inicial: R$ {inv2_capital:.2f}")
    print(f"Valor final: R$ {valor_final2:.2f}")
    print(f"Lucro: R$ {lucro2:.2f}")
    
    # Comparando os lucros
    print("\n" + "="*50)
    print("COMPARAÇÃO")
    print("="*50)
    
    if lucro1 > lucro2:
        print("▶ O primeiro investimento teve MAIS lucro")
        print(f"  Diferença: R$ {lucro1 - lucro2:.2f}")
    elif lucro2 > lucro1:
        print("▶ O segundo investimento teve MAIS lucro")
        print(f"  Diferença: R$ {lucro2 - lucro1:.2f}")
    else:
        print("▶ Ambos os investimentos tiveram o MESMO lucro")
    
    print("="*50)


# Bloco principal
print("\n" + "="*50)
print("COMPARADOR DE INVESTIMENTOS")
print("="*50)

# Leitura do primeiro investimento
print("\n--- PRIMEIRO INVESTIMENTO ---")
inv1_capital = float(input("Capital inicial (R$): "))
inv1_taxa = float(input("Taxa mensal (%): "))
inv1_meses = int(input("Número de meses: "))

# Leitura do segundo investimento
print("\n--- SEGUNDO INVESTIMENTO ---")
inv2_capital = float(input("Capital inicial (R$): "))
inv2_taxa = float(input("Taxa mensal (%): "))
inv2_meses = int(input("Número de meses: "))

# Chamando a função de avaliação
avalia_dois_investimentos(inv1_capital, inv1_taxa, inv1_meses,
                           inv2_capital, inv2_taxa, inv2_meses)