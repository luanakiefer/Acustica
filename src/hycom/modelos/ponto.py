class Ponto():
    """
    Classe que abstrai um valor de um ponto vindo do Hycom
    """

    def __init__(self, profundidade: int, latitude: float, longitude: float, salinidade: float, temperatura: float) -> None:
        self.profundidade = profundidade
        self.latitude = latitude
        self.longitude = longitude
        self.salinidade = salinidade
        self.temperatura = temperatura
    
    def csv(self) -> str:
        return ''.join([
            f'{self.profundidade};',
            f'{self.latitude};',
            f'{self.longitude};',
            f'{self.salinidade};',
            f'{self.temperatura}\n'
        ])