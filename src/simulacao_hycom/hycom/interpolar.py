import numpy as np
from perfil import Perfil
from ponto import Ponto
from math import floor
def equacao_reta(delta_x: float, y0: float, m: float) -> float:
    return y0 + m * delta_x

def preencher_vertical(ponto_a: Ponto, ponto_b: Ponto, passo: int = 1) -> list:
    """
    Interpola para encontrar valores das profundidades faltantes
    """

    inicio: int = floor(ponto_a.profundidade)
    fim: int = floor(ponto_b.profundidade + 1)
    
    profundidades: list = [p for p in range(inicio, fim, passo)]
    pontos_interpolados: list = np.zeros(len(profundidades), dtype=Ponto)
    
    pontos_interpolados[0] = ponto_a
    pontos_interpolados[-1] = ponto_b

    delta_profundidade: float = (ponto_b.profundidade - ponto_a.profundidade)

    m_salinidade: float = (ponto_b.salinidade - ponto_a.salinidade) / delta_profundidade
    m_temperatura: float = (ponto_b.temperatura - ponto_a.temperatura) / delta_profundidade

    for indice, profundidade in enumerate(profundidades[1:-1]):
        salinidade: float = equacao_reta(1, pontos_interpolados[indice - 1].salinidade, m_salinidade)
        temperatura: float = equacao_reta(1, pontos_interpolados[indice - 1].temperatura, m_temperatura)

        pontos_interpolados[indice] = Ponto(profundidade, ponto_a.latitude, ponto_a.longitude, salinidade, temperatura)
    
    return pontos_interpolados

def preencher_horizontal(ponto_a: Ponto, ponto_b: Ponto, distancia: int, passo: int = 1, latitudinal: bool = True) -> list:
    """
    Interpola para encontrar valores faltantes entre pontos distantes
    """

    nPontos: int = round(distancia / passo)
    pontos_interpolados: list = np.zeros(nPontos, dtype=Ponto)

    pontos_interpolados[0] = ponto_a
    pontos_interpolados[-1] = ponto_b

    m_salinidade: float = (ponto_b.salinidade - ponto_a.salinidade) / distancia
    m_temperatura: float = (ponto_b.temperatura - ponto_a.temperatura) / distancia
    
    diferenca_pontos: float = distancia / 0.08

    for indice in range(0, nPontos)[1:-1]:
        salinidade: float = equacao_reta(1, pontos_interpolados[indice - 1].salinidade, m_salinidade)
        temperatura: float = equacao_reta(1, pontos_interpolados[indice - 1].temperatura, m_temperatura)

        latitude: float = ponto_a.latitude + (diferenca_pontos * indice if latitudinal else 0)
        longitude: float = ponto_a.latitude + (diferenca_pontos * indice if latitudinal else 0)

        pontos_interpolados[indice] = Ponto(ponto_a.profundidade, latitude, longitude, salinidade, temperatura)

    return pontos_interpolados

def preencher_secao(perfil_a: Perfil, perfil_b: Perfil, n_pontos: int, latitudinal: bool):
    """
    Interpola verticalmente e horizontalmente 2 perfis
    """

    perfil_interpolado_a = Perfil(perfil_a.latitude, perfil_a.longitude)
    perfil_interpolado_b = Perfil(perfil_b.latitude, perfil_b.longitude)

    perfil_interpolado_a.pontos = preencher_vertical(perfil_a.pontos[0], perfil_a.pontos[1])
    perfil_interpolado_b.pontos = preencher_vertical(perfil_b.pontos[0], perfil_b.pontos[1])

    for indice in range(1, len(perfil_a.pontos) - 1):
        interpolacao_a = preencher_vertical(perfil_a.pontos[indice], perfil_a.pontos[indice + 1])
        interpolacao_b = preencher_vertical(perfil_b.pontos[indice], perfil_b.pontos[indice + 1])

        perfil_interpolado_a.pontos = perfil_interpolado_a.pontos + interpolacao_a[1:]
        perfil_interpolado_b.pontos = perfil_interpolado_b.pontos + interpolacao_b[1:]
    
    perfis_interpolados: list = []
    
    for i in range(n_pontos):
        nova_latitude: float = perfil_interpolado_a.latitude + (i * (0.08 / n_pontos)) if latitudinal else perfil_a.latitude
        nova_longitude: float = perfil_a.longitude if latitudinal else perfil_interpolado_a.longitude + (i * (0.08 / n_pontos))

        novo_perfil = Perfil(nova_latitude, nova_longitude)
        perfis_interpolados.append(novo_perfil)

    for indice in range(len(perfil_interpolado_a.pontos)):
        interpolacao = preencher_horizontal(perfil_interpolado_a.pontos[indice], perfil_interpolado_b.pontos[indice], n_pontos, latitudinal=latitudinal)

        for indice_perfil, ponto in enumerate(interpolacao):
            perfis_interpolados[indice_perfil].pontos.append(ponto)
    
    return perfis_interpolados


