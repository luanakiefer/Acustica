from ler_csv import buscar_por_latitude_longitude

class Perfil():
    """
    Classe que guarda valores de um perfil vertical (temperatura, salinidade, velocidade)
    em uma latitude e longitude
    """

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.pontos = []
    
    def carregar_pontos(self, arquivo: str) -> None:
        """
        Carrega os pontos da lat/lon do arquivo dado
        """

        self.pontos = buscar_por_latitude_longitude(arquivo, self.latitude, self.longitude)