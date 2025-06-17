"""
Módulo responsável pelo cálculo do custo financeiro dos subconjuntos de apostas.
Corresponde ao ITEM 7 do trabalho.
"""

# Valor fixo do cartão da Lotofácil
CUSTO_POR_APOSTA = 3.00

# Dicionário com os nomes dos arquivos dos subconjuntos gerados
ARQUIVOS_SUBSET = {
    14: "SB15_14.txt",
    13: "SB15_13.txt",
    12: "SB15_12.txt",
    11: "SB15_11.txt",
}

def calcular_custo_financeiro():
    """
    Calcula o custo para jogar os subconjuntos de apostas encontrados.
    Para cada arquivo de subconjunto, conta o número de apostas e multiplica pelo valor do cartão.
    Imprime o resultado para cada cenário.
    """
    print("\n--- Item 7: Cálculo de Custo Financeiro ---")
    print(f"Considerando que cada aposta custa R$ {CUSTO_POR_APOSTA:.2f}.\n")
    for t, nome_arquivo in ARQUIVOS_SUBSET.items():
        cenario = f"SB15_{t}"
        try:
            # Conta o número de linhas (apostas) no arquivo
            with open(nome_arquivo, 'r') as f:
                num_apostas = sum(1 for line in f)
            custo_total = num_apostas * CUSTO_POR_APOSTA
            print(f"Custo para o subconjunto {cenario}:")
            print(f"  - Número de apostas: {num_apostas:,}")
            print(f"  - Custo total: R$ {custo_total:,.2f}")
        except FileNotFoundError:
            print(f"Arquivo '{nome_arquivo}' não encontrado. Execute o programa correspondente primeiro.")
        except Exception as e:
            print(f"Não foi possível calcular o custo para {nome_arquivo}: {e}")
        print("-" * 20)
