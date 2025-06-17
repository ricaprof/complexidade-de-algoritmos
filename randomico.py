import itertools
import random
from math import comb

UNIVERSO_NUMEROS = range(1, 26)

# Função para gerar subconjuntos aleatórios de S15 que cobrem S_t

def cobertura_randomica(t, max_iter=10000, seed=None):
    """
    Tenta encontrar um subconjunto de S15 que cubra todas as combinações de S_t usando uma abordagem randômica.
    max_iter: número máximo de tentativas
    seed: semente para reprodutibilidade
    """
    if seed is not None:
        random.seed(seed)

    total_t_subsets = set(itertools.combinations(UNIVERSO_NUMEROS, t))
    cobertura = set()
    cobertos = set()
    iteracao = 0

    while cobertos != total_t_subsets and iteracao < max_iter:
        aposta = tuple(sorted(random.sample(UNIVERSO_NUMEROS, 15)))
        cobertura.add(aposta)
        novos = set(itertools.combinations(aposta, t))
        cobertos.update(novos)
        iteracao += 1
        if iteracao % 100 == 0:
            print(f"Iteração {iteracao}: {len(cobertos)}/{len(total_t_subsets)} sequências cobertas, {len(cobertura)} apostas geradas.")

    if cobertos == total_t_subsets:
        print(f"Cobertura completa encontrada com {len(cobertura)} apostas em {iteracao} iterações.")
    else:
        print(f"Cobertura incompleta após {iteracao} iterações. {len(cobertos)}/{len(total_t_subsets)} sequências cobertas.")
    return cobertura

if __name__ == "__main__":
    print("Exemplo de abordagem randômica para cobertura de S11")
    cobertura_randomica(t=11, max_iter=1000, seed=42)
