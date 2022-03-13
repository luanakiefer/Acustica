import requests
from netCDF4 import Dataset
from sys import argv
from json import dump

class Secao():
    """
    Classe que abstrai os limites geograficos da seção de busca no Hycom
    """

    def __init__(self, norte: float, sul: float, leste: float, oeste: float) -> None:
        self.norte = norte
        self.sul = sul
        self.leste = leste
        self.oeste = oeste

def formatar_dia(dia: int) -> str:
    """
    Formato dd
    """

    if dia > 0 and dia <= 31:
        if dia >= 10:
            return str(dia)
        else:
            return '0' + str(dia)
    
    return ''

def formatar_mes(mes: int) -> str:
    """
    Formato dd
    """

    if mes > 0 and mes <= 12:
        if mes >= 10:
            return str(mes)
        else:
            return '0' + str(mes)
    
    return ''


def construir_url(secao: Secao, dia_1: int, mes_1: int, ano_1: int, dia_2: int, mes_2: int, ano_2: int) -> str:
    """
    Constroi a URL de busca para o hycom
    """

    return f'http://ncss.hycom.org/thredds/ncss/GLBu0.08/expt_19.1/{ano_1}?var=salinity&var=water_temp&north={secao.norte}&west={secao.oeste}&east={secao.leste}&south={secao.sul}&disableLLSubset=on&disableProjSubset=on&horizStride=1&time_start={ano_1}-{formatar_mes(mes_1)}-{formatar_dia(dia_1)}T00%3A00%3A00Z&time_end={ano_2}-{formatar_mes(mes_2)}-{formatar_dia(dia_2)}T00%3A00%3A00Z&timeStride=1&vertCoord=&accept=netcdf'

def construir_arquivo_nc(base: str, dia_1: int, mes_1: int, ano_1: int, dia_2: int, mes_2: int, ano_2: int) -> str:
    """
    Constroi o nome do arquivo .nc
    """

    return f'{base}_{ano_1}{formatar_mes(mes_1)}{formatar_dia(dia_1)}_{ano_2}{formatar_mes(mes_2)}{formatar_dia(dia_2)}.nc'

def construir_arquivo_json(base: str, dia_1: int, mes_1: int, ano_1: int, dia_2: int, mes_2: int, ano_2: int) -> str:
    """
    Constroi o nome do arquivo .json
    """

    return f'{base}_{ano_1}{formatar_mes(mes_1)}{formatar_dia(dia_1)}_{ano_2}{formatar_mes(mes_2)}{formatar_dia(dia_2)}.json'


if __name__ == '__main__':
    dados: list = argv[1:]

    secao: Secao = Secao(norte=float(dados[0]), sul=float(dados[1]), leste=float(dados[2]), oeste=float(dados[3]))
    [dia_1, mes_1, ano_1] = [int(valor) for valor in dados[4].split('-')]
    [dia_2, mes_2, ano_2] = [int(valor) for valor in dados[5].split('-')]

    url: str = construir_url(secao, dia_1, mes_1, ano_1, dia_2, mes_2, ano_2)
    arquivo_nc: str = construir_arquivo_nc(dados[6], dia_1, mes_1, ano_1, dia_2, mes_2, ano_2)
    arquivo_json: str = construir_arquivo_json(dados[6], dia_1, mes_1, ano_1, dia_2, mes_2, ano_2)

    resposta = requests.get(url)

    with open(arquivo_nc, 'wb') as fd:
        for pacote in resposta.iter_content(100):
            fd.write(pacote)
    
    dataset = Dataset(arquivo_nc)
    
    with open(arquivo_json, 'w') as fd:
        conteudo = {
            'LATITUDE': dataset['lat'][:].tolist(),
            'LONGITUDE': dataset['lon'][:].tolist(),
            'SALINIDADE': dataset['salinity'][:].tolist(),
            'TEMPERATURA': dataset['water_temp'][:].tolist()
        }

        dump(conteudo, fd)