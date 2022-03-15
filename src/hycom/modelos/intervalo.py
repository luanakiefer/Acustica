class Intervalo():
    """
    Classe que abstrai o intervalo de busca do Hycom
    """

    def __init__(self, data_inicio: str, data_fim: str) -> None:
        [self.dia_inicio, self.mes_inicio, self.ano_inicio] = [int(valor) for valor in data_inicio.split('-')]
        [self.dia_fim, self.mes_fim, self.ano_fim] = [int(valor) for valor in data_fim.split('-')]
    
    def mes(self, inicio: bool) -> str:
        """
        Formato mm
        """

        mes: int = self.mes_inicio if inicio else self.mes_fim

        if mes > 0 and mes <= 12:
            if mes >= 10:
                return str(mes)
            else:
                return '0' + str(mes)
        
        return ''
    
    def dia(self, inicio: bool) -> str:
        """
        Formato dd
        """

        dia: int = self.dia_inicio if inicio else self.dia_fim

        if dia > 0 and dia <= 31:
            if dia >= 10:
                return str(dia)
            else:
                return '0' + str(dia)
        
        return ''
    
    def ano(self, inicio: bool) -> str:
        """
        Formato yyyy
        """

        return str(self.ano_inicio) if inicio else str(self.ano_fim)
    
    def data(self, inicio: bool) -> list:
        """
        Retorna informações separadas de data já formatada (YYYY, mm, dd)
        """

        return [
            self.ano(inicio),
            self.mes(inicio),
            self.dia(inicio)
        ]
