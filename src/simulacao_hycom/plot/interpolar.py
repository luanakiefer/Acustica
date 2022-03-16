import numpy as np
from modelos.ponto import Ponto

def equacao_reta(delta_x: float, y0: float, m: float) -> float:
    return y0 + m * delta_x

def preencher_vertical(ponto_a: Ponto, ponto_b: Ponto):
    """
    Interpola para encontrar valores das profundidades faltantes
    """

    profundidades: list = [p for p in range(ponto_a.profundidade, ponto_b.profundidade + 1)]
    pontos: list = np.zeros(len(profundidades), dtype=Ponto)
    
    pontos[0] = ponto_a
    pontos[-1] = ponto_b

    delta_profundidade: float = (ponto_b.profundidade - ponto_a.profundidade)

    m_salinidade: float = (ponto_b.salinidade - ponto_a.salinidade) / delta_profundidade
    m_temperatura: float = (ponto_b.temperatura - ponto_a.temperatura) / delta_profundidade

    for indice, profundidade in enumerate(profundidades)[1:-1]:
        salinidade: float = equacao_reta(1, pontos[indice - 1].salinidade, m_salinidade)
        temperatura: float = equacao_reta(1, pontos[indice - 1].temperatura, m_temperatura)

        pontos[indice] = Ponto(profundidade, ponto_a.latitude, ponto_a.longitude, salinidade, temperatura)       