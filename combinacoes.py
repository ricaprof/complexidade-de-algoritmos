"""
Módulo responsável pela geração de todas as combinações possíveis de números para Lotofácil.
Corresponde ao PROGRAMA 1 do trabalho.
"""
import itertools
from math import comb

# Universo de números da Lotofácil (1 a 25)
UNIVERSO_NUMEROS = range(1, 26)

# Dicionário com os nomes dos arquivos de saída para cada valor de p
ARQUIVOS_COMBINACOES = {
    15: "S15.txt",
    14: "S14.txt",
    13: "S13.txt",
    12: "S12.txt",
    11: "S11.txt",
}

# Quantidade esperada de combinações para cada valor de p, conforme o enunciado
CONTAGENS_ESPERADAS = {
    15: 3268760,
    14: 4457400,
    13: 5200300,
    12: 5200300,
    11: 4457400
}

def gerar_e_salvar_combinacoes(n, p):
    """
    Gera todas as combinações C(n, p) e salva em um arquivo de texto.
    Também verifica se a contagem corresponde ao esperado no documento.
    
    Parâmetros:
    - n: tamanho do universo (deve ser 25)
    - p: tamanho das combinações (15, 14, 13, 12 ou 11)
    """
    nome_arquivo = ARQUIVOS_COMBINACOES.get(p)
    if not nome_arquivo:
        print(f"Tamanho de combinação {p} não é necessário.")
        return

    print(f"Iniciando a geração de sequências de {p} números (S{p})...")
    try:
        with open(nome_arquivo, "w") as f:
            count = 0
            # itertools.combinations gera todas as combinações possíveis de p elementos do universo
            for combo in itertools.combinations(UNIVERSO_NUMEROS, p):
                # Escreve a combinação no arquivo, separando os números por espaço
                f.write(" ".join(map(str, combo)) + "\n")
                count += 1
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso.")
        print(f"Total de combinações geradas: {count}")
        # Verificação: compara a quantidade gerada com a esperada
        if count == CONTAGENS_ESPERADAS.get(p):
            print(f"Contagem VERIFICADA com sucesso com o valor do documento: {CONTAGENS_ESPERADAS[p]}.")
        else:
            print(f"AVISO: Contagem {count} difere do valor esperado {CONTAGENS_ESPERADAS.get(p)}.")
    except Exception as e:
        print(f"Ocorreu um erro ao gerar o arquivo {nome_arquivo}: {e}")
    print("-" * 30)
