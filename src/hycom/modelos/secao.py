class Secao():
    """
    Classe que abstrai os limites geograficos da seção de busca no Hycom
    """

    def __init__(self, norte: float, sul: float, leste: float, oeste: float) -> None:
        self.norte = norte
        self.sul = sul
        self.leste = leste
        self.oeste = oeste