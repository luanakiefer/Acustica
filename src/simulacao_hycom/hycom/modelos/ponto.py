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

        self._calcular_velocidade()
    
    def _calcular_velocidade(self) -> None:
        t: float = self.temperatura
        s: float = self.salinidade
        p: float = self.profundidade

        if (t == None or s == None or p == None):
            self.velocidade = None
        else:
            self.velocidade: float = 0
            self.velocidade = (
                1448.96 + 4.591 * t - 0.05304 * t**2
                + 2.374 * 10**(-4) * t**3 + 1.340 * (s - 35)
                + 0.0163 * p + 1.675 * 10**(-7) * p**2
                - 0.01025 * t * (s - 35)
                - 7.139 * 10**(-13) * t * p**3
            )
    
    def csv(self) -> str:
        return ''.join([
            f'{self.profundidade};',
            f'{self.latitude};',
            f'{self.longitude};',
            f'{self.salinidade};',
            f'{self.temperatura};',
            f'{self.velocidade}\n'
        ])