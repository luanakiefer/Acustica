import requests
from netCDF4 import Dataset
from sys import argv
from modelos.ponto import Ponto
from modelos.intervalo import Intervalo
from modelos.secao import Secao
import utils

PROFUNDIDADES = [
    0, 2, 4, 6, 8,
    10, 12, 15, 20, 25,
    30, 35, 40, 45, 50,
    60, 70, 80, 90, 100,
    125, 150, 200, 250, 300,
    350, 400, 500, 600, 700,
    800, 900, 1000, 1250, 1500,
    2000, 2500, 3000, 4000, 5000
]

if __name__ == '__main__':
    dados: list = argv[1:]

    secao: Secao = Secao(norte=float(dados[0]), sul=float(dados[1]), leste=float(dados[2]), oeste=float(dados[3]))
    intervalo: Intervalo = Intervalo(data_inicio=dados[4], data_fim=dados[5])
    base_arquivo: str = dados[6]

    url: str = utils.construir_url(secao, intervalo)
    print(url)
    arquivo_nc: str = utils.construir_arquivo_nc(base_arquivo, intervalo)
    arquivo_csv: str = utils.construir_arquivo_csv(base_arquivo, intervalo)

    resposta = requests.get(url)

    with open(arquivo_nc, 'wb') as fd:
        for pacote in resposta.iter_content(100):
            fd.write(pacote)
    
    dataset = Dataset(arquivo_nc)

    LATITUDE: list = dataset['lat'][:].tolist()
    LONGITUDE: list = dataset['lon'][:].tolist()

    matriz: list = []
    
    # Tratar salinidade
    salinidades: list = dataset['salinity'][:].tolist()[0]
    temperaturas: list = dataset['water_temp'][:].tolist()[0]

    pontos: list = []

    for indice_prof in range(40):
        prof: int = PROFUNDIDADES[indice_prof]

        for indice_lat in range(len(salinidades[0])):
            lat: float = LATITUDE[indice_lat]

            for indice_lon in range(len(salinidades[0][0])):
                lon: float = LONGITUDE[indice_lon]
                salinidade: float = salinidades[indice_prof][indice_lat][indice_lon]
                temperatura: float = temperaturas[indice_prof][indice_lat][indice_lon]

                pontos.append(Ponto(prof, lat, lon, salinidade, temperatura))
    
    with open(arquivo_csv, 'w') as fd:
        fd.write('PROFUNDIDADE;LATITUDE;LONGITUDE;SALINIDADE;TEMPERATURA;VELOCIDADE\n')

        for ponto in pontos:
            fd.write(ponto.csv())