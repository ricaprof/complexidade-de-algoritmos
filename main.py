"""
Arquivo principal do projeto. Centraliza a execução dos módulos e apresenta o menu interativo.
"""
from combinacoes import gerar_e_salvar_combinacoes
from cobertura import encontrar_conjunto_de_cobertura
from analise import analisar_complexidade
from custo import calcular_custo_financeiro

if __name__ == "__main__":
    # Apresentação inicial
    print("Trabalho de Complexidade de Algoritmos - Lotofácil")
    print("Professor: Edson Emílio Scalabrin")
    print("=" * 50)
    # Loop do menu interativo
    while True:
        print("\nEscolha a operação a ser realizada:")
        print("\n--- Bloco 1: Geração de Arquivos Base ---")
        print("1. Gerar TODAS as combinações (S11 a S15) (PROGRAMA 1)")  # combinacoes.py -> gerar_e_salvar_combinacoes
        print("\n--- Bloco 2: Encontrar Conjuntos de Cobertura (Processo Lento) ---")
        print("2. Encontrar SB15_14 (Cobre todas as S14) (PROGRAMA 2)")  # cobertura.py -> encontrar_conjunto_de_cobertura
        print("3. Encontrar SB15_13 (Cobre todas as S13) (PROGRAMA 3)")  # cobertura.py -> encontrar_conjunto_de_cobertura
        print("4. Encontrar SB15_12 (Cobre todas as S12) (PROGRAMA 4)")  # cobertura.py -> encontrar_conjunto_de_cobertura
        print("5. Encontrar SB15_11 (Cobre todas as S11) (PROGRAMA 5)")  # cobertura.py -> encontrar_conjunto_de_cobertura
        print("\n--- Bloco 3: Análise e Resultados ---")
        print("6. Apresentar Análise de Complexidade (Item 6)")  # analise.py -> analisar_complexidade
        print("7. Calcular Custo Financeiro dos subconjuntos (Item 7)")  # custo.py -> calcular_custo_financeiro
        print("0. Sair")
        escolha = input("\nDigite sua escolha: ")
        # Chama a função correspondente de acordo com a escolha do usuário
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
