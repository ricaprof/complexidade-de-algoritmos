import os


def salvar_em_arquivo(combinacoes, nome_arquivo):
    os.makedirs('resultados', exist_ok=True)
    caminho = os.path.join('resultados', nome_arquivo)

    with open(caminho, 'w') as f:
        for c in combinacoes:
            linha = ','.join(map(str, c))
            f.write(linha + '\n')

    print(f"Arquivo salvo em {caminho}")


def ler_arquivo(nome_arquivo):
    caminho = os.path.join('resultados', nome_arquivo)
    with open(caminho, 'r') as f:
        linhas = f.readlines()
    combinacoes = [tuple(map(int, linha.strip().split(','))) for linha in linhas]
    return combinacoes
