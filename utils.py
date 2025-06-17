import time
import functools
import logging

# Configura um logger customizado para evitar conflitos com o logger global
logger = logging.getLogger("complexidade")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

def medir_tempo(func):
    """Decorador para medir e logar o tempo de execução de uma função."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception as exc:
            logger.exception(f"Erro na função '{func.__name__}': {exc}")
            raise
        end = time.perf_counter()
        logger.info(f"Função '{func.__name__}' executada em {end - start:.4f} segundos")
        return result
    return wrapper

def calcular_custo(qtd_apostas, valor_por_cartao=3.00):
    """Calcula o custo total com base na quantidade de apostas e no valor por cartão."""
    custo = qtd_apostas * valor_por_cartao
    logger.info(f"Custo para {qtd_apostas} apostas: R$ {custo:.2f}")
    return custo
