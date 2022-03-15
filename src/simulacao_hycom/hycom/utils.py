from modelos.intervalo import Intervalo
from modelos.secao import Secao


def construir_url(secao: Secao, intervalo: Intervalo) -> str:
    """
    Constroi a URL de busca para o hycom
    """

    [ano_1, mes_1, dia_1] = intervalo.data(inicio = True)
    [ano_2, mes_2, dia_2] = intervalo.data(inicio = False)

    print([ano_1, mes_1, dia_1])
    print([ano_2, mes_2, dia_2])

    return f'http://ncss.hycom.org/thredds/ncss/GLBu0.08/expt_19.1/{ano_1}?var=salinity&var=water_temp&north={secao.norte}&west={secao.oeste}&east={secao.leste}&south={secao.sul}&disableLLSubset=on&disableProjSubset=on&horizStride=1&time_start={ano_1}-{mes_1}-{dia_1}T00%3A00%3A00Z&time_end={ano_2}-{mes_2}-{dia_2}T00%3A00%3A00Z&timeStride=1&vertCoord=&accept=netcdf'

def construir_arquivo_nc(base: str, intervalo: Intervalo) -> str:
    """
    Constroi o nome do arquivo .nc
    """

    [ano_1, mes_1, dia_1] = intervalo.data(inicio = True)
    [ano_2, mes_2, dia_2] = intervalo.data(inicio = False)

    return f'{base}_{ano_1}{mes_1}{dia_1}_{ano_2}{mes_2}{dia_2}.nc'

def construir_arquivo_csv(base: str, intervalo: Intervalo) -> str:
    """
    Constroi o nome do arquivo .csv
    """

    [ano_1, mes_1, dia_1] = intervalo.data(inicio = True)
    [ano_2, mes_2, dia_2] = intervalo.data(inicio = False)

    return f'{base}_{ano_1}{mes_1}{dia_1}_{ano_2}{mes_2}{dia_2}.csv'