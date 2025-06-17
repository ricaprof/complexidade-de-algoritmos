import sys
from combinacoes import gerar_combinacoes, encontrar_cobertura
from arquivos import salvar_em_arquivo
from utils import logger, medir_tempo, calcular_custo

# Programa 1: Gerar todas as combinações S15 e salvar em S15.txt
@medir_tempo
def programa1():
    print("\n[Programa 1] Gerando combinações S15...")
    S15 = list(gerar_combinacoes(25, 15))
    salvar_em_arquivo(S15, "S15.txt")
    print(f"S15 gerado com sucesso. Total de combinações: {len(S15)}")


# Programa 2 a 5: Usam o mesmo algoritmo de cobertura, variando o valor t
@medir_tempo
def programa_cobertura(tamanho_subconjunto):
    print(f"\n[Programa Cobertura] Encontrando SB15_{tamanho_subconjunto}...")
    # Gera S15: todas as apostas de 15 números do universo [1,25]
    S15 = list(gerar_combinacoes(25, 15))
    logger.info(f"S15 gerado com {len(S15)} apostas.")
    
    # Executa o algoritmo de cobertura para o valor t informado
    cobertura = encontrar_cobertura(S15, tamanho_subconjunto)
    logger.info(f"Cobertura encontrada com {len(cobertura)} apostas.")
    
    # Salva resultado num arquivo com nome baseado em t, ex: SB15_14.txt
    nome_arquivo = f"SB15_{tamanho_subconjunto}.txt"
    salvar_em_arquivo(cobertura, nome_arquivo)
    
    # Calcula custo financeiro
    calcular_custo(len(cobertura))
    print(f"Processo de cobertura para t = {tamanho_subconjunto} concluído.\n")


def menu():
    while True:
        print("\n=== LOTOFÁCIL - COMPLEXIDADE DE ALGORITMOS ===")
        print("1 - Gerar todas as combinações (Programa 1)")
        print("2 - Encontrar SB15_14 (Programa 2)")
        print("3 - Encontrar SB15_13 (Programa 3)")
        print("4 - Encontrar SB15_12 (Programa 4)")
        print("5 - Encontrar SB15_11 (Programa 5)")
        print("0 - Sair")
    
        opcao = input("Escolha uma opção: ").strip()
    
        if opcao == '1':
            programa1()
        elif opcao == '2':
            programa_cobertura(14)
        elif opcao == '3':
            programa_cobertura(13)
        elif opcao == '4':
            programa_cobertura(12)
        elif opcao == '5':
            programa_cobertura(11)
        elif opcao == '0':
            print("Encerrando o programa...")
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
