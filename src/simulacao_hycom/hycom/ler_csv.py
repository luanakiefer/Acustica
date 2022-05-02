from ponto import ponto_de_lista
from plot import plotar_perfis, plotar_varios_perfis

def buscar_por_latitude_longitude(arquivo: str, latitude: float, longitude: float):
    pontos: list = []

    with open(arquivo, 'r') as fd:
        fd.readline() # Pula cabeçalho

        for linha in fd:
            valores: list = [None if valor == 'None' else float(valor) for valor in linha.strip().split(';')]

            if valores[1] == latitude and valores[2] == longitude:
                pontos.append(ponto_de_lista(valores))
        
    return pontos