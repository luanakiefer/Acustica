from perfil import Perfil
import interpolar

coordenada_a = {
    "lat": -20.239999771118164,
    "lon": -39.0400390625
}

coordenada_b = {
    "lat": -20.31999969482422,
    "lon": -39.0400390625
}

distancia_entre_coordenadas = 9000
corte_latitudinal = True
localizao_arquivo_dados = './data/teste_20121231_20121231.csv' #Colocar endereço da pasta onde esta o arquivo

perfil_a = Perfil(coordenada_a['lat'], coordenada_a['lon'])
perfil_b = Perfil(coordenada_b['lat'], coordenada_b['lon'])

perfil_a.carregar_pontos(localizao_arquivo_dados)
perfil_b.carregar_pontos(localizao_arquivo_dados)

secao = interpolar.preencher_secao(
    perfil_a,
    perfil_b,
    distancia_entre_coordenadas,
    corte_latitudinal
)