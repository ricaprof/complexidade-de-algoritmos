"""
Módulo responsável por encontrar subconjuntos de S15 que cobrem todas as combinações de S14, S13, S12 ou S11.
Corresponde aos PROGRAMAS 2, 3, 4 e 5 do trabalho.
"""
import itertools
import os
import time

# Universo de números da Lotofácil (1 a 25)
UNIVERSO_NUMEROS = range(1, 26)

# Dicionários com nomes dos arquivos de entrada e saída
ARQUIVOS_COMBINACOES = {
    15: "S15.txt",
    14: "S14.txt",
    13: "S13.txt",
    12: "S12.txt",
    11: "S11.txt",
}
ARQUIVOS_SUBSET = {
    14: "SB15_14.txt",
    13: "SB15_13.txt",
    12: "SB15_12.txt",
    11: "SB15_11.txt",
}

def encontrar_conjunto_de_cobertura(v, k, t):
    """
    Implementa uma heurística gulosa para encontrar um conjunto de cobertura C(v, k, t).
    v: total de números (25)
    k: tamanho do conjunto de apostas (15)
    t: tamanho das sequências a serem cobertas (11, 12, 13 ou 14)
    """
    arquivo_t = ARQUIVOS_COMBINACOES.get(t)
    arquivo_saida_sb = ARQUIVOS_SUBSET.get(t)

    print(f"\n--- Iniciando PROGRAMA para Cenário C(v={v}, k={k}, t={t}) ---")
    print(f"Objetivo: Encontrar {os.path.basename(arquivo_saida_sb)}, o menor subconjunto de S15 que cobre todas as sequências em S{t}.")
    print("\nAVISO: Este processo é EXTREMAMENTE demorado e pode levar horas ou dias.")
    print("O algoritmo carregará todas as combinações a serem cobertas na memória.")
    try:
        # Carrega todas as sequências-alvo (t-subsets) na memória para acesso rápido
        print(f"Carregando sequências do arquivo '{arquivo_t}' para a memória...")
        with open(arquivo_t, 'r') as f:
            # Cada linha do arquivo é convertida em uma tupla de inteiros
            t_subsets_a_cobrir = {tuple(map(int, line.strip().split())) for line in f}
        print(f"{len(t_subsets_a_cobrir):,} sequências de tamanho {t} carregadas.")
    except FileNotFoundError:
        print(f"\nERRO: O arquivo de combinações '{arquivo_t}' não foi encontrado.")
        print("Por favor, execute a geração de combinações primeiro.")
        return

    conjunto_cobertura_final = set()  # Armazena as apostas de 15 números escolhidas
    total_t_subsets_inicial = len(t_subsets_a_cobrir)
    start_time = time.time()

    # Loop principal: enquanto ainda houver sequências a cobrir
    while t_subsets_a_cobrir:
        # 1. Seleciona uma sequência t ainda não coberta para servir de "semente"
        t_semente = t_subsets_a_cobrir.pop()
        t_subsets_a_cobrir.add(t_semente)  # Adiciona de volta para a contagem de cobertura
        melhor_k_candidato = None
        max_cobertos = -1
        subsets_cobertos_pelo_melhor = set()
        # 2. Gera todos os candidatos de 15 números que cobrem a semente
        numeros_restantes = list(set(UNIVERSO_NUMEROS) - set(t_semente))
        for sub_combinacao in itertools.combinations(numeros_restantes, k - t):
            k_candidato = tuple(sorted(t_semente + sub_combinacao))
            # 3. Conta quantos novos t-subsets este candidato cobre
            novos_cobertos_pelo_candidato = set(itertools.combinations(k_candidato, t)).intersection(t_subsets_a_cobrir)
            if len(novos_cobertos_pelo_candidato) > max_cobertos:
                max_cobertos = len(novos_cobertos_pelo_candidato)
                melhor_k_candidato = k_candidato
                subsets_cobertos_pelo_melhor = novos_cobertos_pelo_candidato
        # 4. Adiciona o melhor candidato ao conjunto de cobertura e remove os t-subsets cobertos
        if melhor_k_candidato:
            conjunto_cobertura_final.add(melhor_k_candidato)
            t_subsets_a_cobrir.difference_update(subsets_cobertos_pelo_melhor)
        # 5. Relatório de progresso a cada 100 apostas
        if len(conjunto_cobertura_final) % 100 == 0:
            percentual_concluido = (1 - len(t_subsets_a_cobrir) / total_t_subsets_inicial) * 100
            print(f"Progresso: {len(conjunto_cobertura_final)} apostas no conjunto. "
                  f"{len(t_subsets_a_cobrir):,} sequências restantes. "
                  f"({percentual_concluido:.4f}% concluído)")
    end_time = time.time()

    # Salva o conjunto de cobertura encontrado no arquivo de saída
    try:
        with open(arquivo_saida_sb, 'w') as f:
            for aposta in sorted(conjunto_cobertura_final):
                f.write(" ".join(map(str, aposta)) + "\n")
        print(f"\nConjunto de cobertura encontrado com sucesso!")
        print(f"Aposta(s) salva(s) em '{arquivo_saida_sb}'")
        print(f"Tempo total: {end_time - start_time:.2f} segundos.")
        print(f"Total de apostas no subconjunto: {len(conjunto_cobertura_final)}")
        # Exibe as 10 primeiras apostas como amostra
        amostra_apostas = list(conjunto_cobertura_final)[:10]
        print("Amostra das 10 primeiras apostas encontradas:")
        for aposta in amostra_apostas:
            print(aposta)
    except Exception as e:
        print(f"\nERRO ao salvar o arquivo de saída: {e}")
