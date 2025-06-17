import itertools
import os
import time
from math import comb

# --- Configurações Iniciais ---

# Números base para a Lotofácil 
UNIVERSO_NUMEROS = range(1, 26)
CUSTO_POR_APOSTA = 3.00  # 

# Nomes dos arquivos de saída
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

# --- PROGRAMA 1: Geração de Todas as Combinações ---

def gerar_e_salvar_combinacoes(n, p):
    """
    Gera combinações C(n, p) e salva em um arquivo de texto.
    Verifica se a contagem corresponde ao esperado no documento.
    """
    nome_arquivo = ARQUIVOS_COMBINACOES.get(p)
    if not nome_arquivo:
        print(f"Tamanho de combinação {p} não é necessário.")
        return

    print(f"Iniciando a geração de sequências de {p} números (S{p})...")
    
    # Valores esperados do documento PDF
    contagens_esperadas = {
        15: 3268760, # 
        14: 4457400, # 
        13: 5200300, # 
        12: 5200300, # 
        11: 4457400  # 
    }

    try:
        with open(nome_arquivo, "w") as f:
            count = 0
            combinacoes = itertools.combinations(UNIVERSO_NUMEROS, p)
            for combo in combinacoes:
                f.write(" ".join(map(str, combo)) + "\n")
                count += 1
        
        print(f"Arquivo '{nome_arquivo}' gerado com sucesso.")
        print(f"Total de combinações geradas: {count}")

        # Verificação
        if count == contagens_esperadas.get(p):
            print(f"Contagem VERIFICADA com sucesso com o valor do documento: {contagens_esperadas[p]}.")
        else:
            print(f"AVISO: Contagem {count} difere do valor esperado {contagens_esperadas.get(p)}.")

    except Exception as e:
        print(f"Ocorreu um erro ao gerar o arquivo {nome_arquivo}: {e}")
    print("-" * 30)

# --- PROGRAMAS 2-5: Algoritmo de Cobertura (Heurística Gulosa) ---

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

    # --- AVISO DE PERFORMANCE ---
    print("\nAVISO: Este processo é EXTREMAMENTE demorado e pode levar horas ou dias.")
    print("O algoritmo carregará todas as combinações a serem cobertas na memória.")
    
    try:
        # Carregar todas as sequências-alvo (t-subsets) na memória para acesso rápido
        print(f"Carregando sequências do arquivo '{arquivo_t}' para a memória...")
        with open(arquivo_t, 'r') as f:
            # Usar um set de tuplas para busca O(1) e remoção eficiente
            t_subsets_a_cobrir = {tuple(map(int, line.strip().split())) for line in f}
        print(f"{len(t_subsets_a_cobrir):,} sequências de tamanho {t} carregadas.")

    except FileNotFoundError:
        print(f"\nERRO: O arquivo de combinações '{arquivo_t}' não foi encontrado.")
        print("Por favor, execute a geração de combinações primeiro.")
        return

    conjunto_cobertura_final = set()
    total_t_subsets_inicial = len(t_subsets_a_cobrir)
    start_time = time.time()

    while t_subsets_a_cobrir:
        # --- Lógica do Algoritmo Guloso ---
        
        # 1. Pega uma sequência `t` ainda não coberta para usar como "semente"
        t_semente = t_subsets_a_cobrir.pop()
        t_subsets_a_cobrir.add(t_semente) # Adiciona de volta para a contagem de cobertura

        melhor_k_candidato = None
        max_cobertos = -1
        subsets_cobertos_pelo_melhor = set()

        # 2. Gera k-sets candidatos que garantidamente cobrem a `t_semente`
        numeros_restantes = list(set(UNIVERSO_NUMEROS) - set(t_semente))
        
        for sub_combinacao in itertools.combinations(numeros_restantes, k - t):
            k_candidato = tuple(sorted(t_semente + sub_combinacao))

            # 3. Conta quantos novos t-subsets este k-candidato cobre
            novos_cobertos_pelo_candidato = set(itertools.combinations(k_candidato, t)).intersection(t_subsets_a_cobrir)
            
            if len(novos_cobertos_pelo_candidato) > max_cobertos:
                max_cobertos = len(novos_cobertos_pelo_candidato)
                melhor_k_candidato = k_candidato
                subsets_cobertos_pelo_melhor = novos_cobertos_pelo_candidato

        # 4. Adiciona o melhor candidato ao conjunto de cobertura e atualiza o set de t-subsets
        if melhor_k_candidato:
            conjunto_cobertura_final.add(melhor_k_candidato)
            t_subsets_a_cobrir.difference_update(subsets_cobertos_pelo_melhor)

        # 5. Relatório de progresso
        if len(conjunto_cobertura_final) % 100 == 0:
            percentual_concluido = (1 - len(t_subsets_a_cobrir) / total_t_subsets_inicial) * 100
            print(f"Progresso: {len(conjunto_cobertura_final)} apostas no conjunto. "
                  f"{len(t_subsets_a_cobrir):,} sequências restantes. "
                  f"({percentual_concluido:.4f}% concluído)")

    end_time = time.time()
    
    # Salvando o resultado
    print("Cobertura completa! Salvando o subconjunto resultante...")
    with open(arquivo_saida_sb, "w") as f:
        for aposta in sorted(list(conjunto_cobertura_final)):
            f.write(" ".join(map(str, aposta)) + "\n")

    print(f"\n--- RESULTADO PARA O CENÁRIO C(v={v}, k={k}, t={t}) ---")
    print(f"O arquivo '{arquivo_saida_sb}' foi gerado com sucesso.")
    print(f"Número de apostas no subconjunto: {len(conjunto_cobertura_final)}")
    print(f"Tempo total de execução: { (end_time - start_time) / 3600:.2f} horas")


# --- Item 6: Análise de Complexidade ---

def analisar_complexidade():
    """
    Imprime a análise de complexidade de tempo para os algoritmos de cobertura.
    """
    print("\n--- Item 6: Análise de Complexidade de Tempo ---")
    print("A análise a seguir aplica-se aos PROGRAMAS 2, 3, 4 e 5, que usam a mesma heurística gulosa.")
    print("Notação:")
    print("  v: Tamanho do universo de números (25)")
    print("  k: Tamanho das apostas no conjunto de cobertura (15)")
    print("  t: Tamanho das sequências a serem cobertas (11, 12, 13 ou 14)")
    print(r"  $N_t = \binom{v}{t}$: Número total de sequências a serem cobertas")
    print(r"  $|S_B|$: Tamanho final do conjunto de cobertura encontrado (ex: |SB15_14|)")
    
    print("\nComplexidade do Algoritmo Guloso Implementado:")
    print(r"O( $N_t \cdot t \log t$ + $|S_B| \cdot \binom{v-t}{k-t} \cdot \binom{k}{t} \cdot t$ )")
    
    print("\nDetalhamento:")
    print(f"1. Carregamento inicial: Carregar todas as $N_t$ sequências em um set. A complexidade de inserir $N_t$ itens, cada um de tamanho $t$, é aproximadamente $O(N_t \cdot t \log t)$ devido à necessidade de ordenar as tuplas para consistência.")
    print(f"2. Loop Principal: O loop executa $|S_B|$ vezes, uma para cada aposta adicionada ao conjunto de cobertura.")
    print(f"3. Dentro do Loop:")
    print(f"   a. Geração de Candidatos: Para uma 'semente' de tamanho $t$, geramos $\binom{v-t}{k-t}$ apostas candidatas de tamanho $k$.")
    print(f"   b. Avaliação de Candidatos: Para cada candidato, geramos seus $\binom{k}{t}$ sub-sets de tamanho $t$ e verificamos se estão no conjunto de sequências a cobrir. Esta verificação (interseção de sets) é a parte mais cara.")
    print("\nConclusão:")
    print("A complexidade é dominada pelo loop principal. Embora muito alta, é significativamente melhor do que uma abordagem de força bruta que testaria todas as $\binom{v}{k}$ apostas possíveis a cada passo.")


# --- Item 7: Cálculo de Custo Financeiro ---

def calcular_custo_financeiro():
    """
    Calcula o custo para jogar os subconjuntos de apostas encontrados.
    """
    print("\n--- Item 7: Cálculo de Custo Financeiro ---")
    print(f"Considerando que cada aposta custa R$ {CUSTO_POR_APOSTA:.2f}.\n")

    for t, nome_arquivo in ARQUIVOS_SUBSET.items():
        cenario = f"SB15_{t}"
        try:
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


# --- Função Principal ---

if __name__ == "__main__":
    print("Trabalho de Complexidade de Algoritmos - Lotofácil")
    print("Professor: Edson Emílio Scalabrin")
    print("=" * 50)

    # --- Menu de Execução ---
    while True:
        print("\nEscolha a operação a ser realizada:")
        print("\n--- Bloco 1: Geração de Arquivos Base ---")
        print("1. Gerar TODAS as combinações (S11 a S15) (PROGRAMA 1)")
        
        print("\n--- Bloco 2: Encontrar Conjuntos de Cobertura (Processo Lento) ---")
        print("2. Encontrar SB15_14 (Cobre todas as S14) (PROGRAMA 2)")
        print("3. Encontrar SB15_13 (Cobre todas as S13) (PROGRAMA 3)")
        print("4. Encontrar SB15_12 (Cobre todas as S12) (PROGRAMA 4)")
        print("5. Encontrar SB15_11 (Cobre todas as S11) (PROGRAMA 5)")
        
        print("\n--- Bloco 3: Análise e Resultados ---")
        print("6. Apresentar Análise de Complexidade (Item 6)")
        print("7. Calcular Custo Financeiro dos subconjuntos (Item 7)")
        print("0. Sair")

        escolha = input("\nDigite sua escolha: ")

        if escolha == '1':
            print("\n--- EXECUTANDO PROGRAMA 1 ---")
            for p in [15, 14, 13, 12, 11]:
                gerar_e_salvar_combinacoes(n=25, p=p)
        elif escolha == '2':
            encontrar_conjunto_de_cobertura(v=25, k=15, t=14)
        elif escolha == '3':
            encontrar_conjunto_de_cobertura(v=25, k=15, t=13)
        elif escolha == '4':
            encontrar_conjunto_de_cobertura(v=25, k=15, t=12)
        elif escolha == '5':
            encontrar_conjunto_de_cobertura(v=25, k=15, t=11)
        elif escolha == '6':
            analisar_complexidade()
        elif escolha == '7':
            calcular_custo_financeiro()
        elif escolha == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")
