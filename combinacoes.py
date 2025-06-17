from itertools import combinations
from math import comb


def tuple_to_bitmask(tup):
    """Converte uma tupla de números em um bitmask inteiro."""
    mask = 0
    for number in tup:
        mask |= (1 << (number - 1))
    return mask


def gerar_combinacoes(n, p):
    """Gera todas as combinações de p elementos do conjunto [1, n]."""
    return list(combinations(range(1, n + 1), p))


def t_subsets_bitmask(tamanho):
    """Gera o conjunto (como bitmasks) de todos os t‑subconjuntos do conjunto [1, 25]."""
    return {tuple_to_bitmask(c) for c in combinations(range(1, 26), tamanho)}


def calcular_t_subsets_de_candidato(candidato, tamanho_subconjunto):
    """Calcula os bitmasks de todos os t‑subconjuntos de um candidato."""
    return {tuple_to_bitmask(c) for c in combinations(candidato, tamanho_subconjunto)}


def encontrar_cobertura(S_maior, tamanho_subconjunto):
    """
    Encontra um subconjunto de S_maior que cubra todos os subconjuntos de tamanho_subconjunto.
    Otimização:
      - Utiliza representação em bitmask para operações rápidas.
      - Pré-cálculo dos t‑subconjuntos do universo.
      - Para cada candidato, calcula quantos t‑subconjuntos faltantes ele cobre.
    """
    # Gera os t‑subconjuntos do universo (ficam representados como bitmasks)
    S_sub = t_subsets_bitmask(tamanho_subconjunto)
    cobertura = []

    # Converte cada candidato para (tupla, bitmask)
    S_maior_bit = [(s, tuple_to_bitmask(s)) for s in S_maior]

    while S_sub:
        melhor = None
        max_cobertos = 0
        melhor_subs = None

        # Para cada candidato, compute quantos dos t‑subconjuntos restantes ele cobre
        for s, s_mask in S_maior_bit:
            subs_candidato = calcular_t_subsets_de_candidato(s, tamanho_subconjunto)
            num_cobertos = len(subs_candidato & S_sub)
            if num_cobertos > max_cobertos:
                melhor = s
                max_cobertos = num_cobertos
                melhor_subs = subs_candidato
                # Se o candidato cobre todos os seus t‑subconjuntos possíveis, interrompe a busca
                if max_cobertos == comb(len(s), tamanho_subconjunto):
                    break

        if melhor is None:
            break

        cobertura.append(melhor)
        S_sub -= melhor_subs
        print(f"Restam {len(S_sub)} subconjuntos a serem cobertos...")

    return cobertura
