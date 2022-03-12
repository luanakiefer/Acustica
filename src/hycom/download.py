import requests
from sys import argv

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


def construir_url(secao: Secao, dia: int, mes: int, ano: int) -> str:
    """
    Constroi a URL de busca para o hycom
    """

    return f'http://ncss.hycom.org/thredds/ncss/GLBu0.08/expt_19.1/{ano}?var=salinity&var=water_temp&north={secao.norte}&west={secao.oeste}&east={secao.leste}&south={secao.sul}&disableLLSubset=on&disableProjSubset=on&horizStride=1&time_start={ano}-{formatar_mes(mes)}-{formatar_dia(dia)}T00%3A00%3A00Z&time_end={ano}-{formatar_mes(mes)}-{formatar_dia(dia)}T00%3A00%3A00Z&timeStride=1&vertCoord=&accept=netcdf'

def construir_arquivo(base: str, dia: int, mes: int, ano: int) -> str:
    """
    Constroi o nome do arquivo .nc
    """

    return f'{base}_{ano}{formatar_mes(mes)}{formatar_dia(dia)}.nc'

if __name__ == '__main__':
    dados: list = argv[1:]

    secao: Secao = Secao(norte=float(dados[0]), sul=float(dados[1]), leste=float(dados[2]), oeste=float(dados[3]))
    dia: int = int(dados[4])
    mes: int = int(dados[5])
    ano: int = int(dados[6])

    url: str = construir_url(secao, dia, mes, ano)
    arquivo: str = construir_arquivo(dados[7], dia, mes, ano)

    resposta = requests.get(url)

    with open(arquivo, 'wb') as fd:
        for pacote in resposta.iter_content(100):
            fd.write(pacote)