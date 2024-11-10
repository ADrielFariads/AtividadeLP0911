class Instrument:
    def __init__(self, marca:str, modelo:str, valor:int|float, n_cordas:int):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.n_cordas = n_cordas

class Guitarra(Instrument):
    def __init__(self, marca, modelo, valor, n_cordas, captador:str):
        super().__init__(marca, modelo, valor, n_cordas)
        self.captador = captador
    
class Baixo(Instrument):
    def __init__(self, marca, modelo, valor, n_cordas, escala, amplificacao:str):
        super().__init__(marca, modelo, valor, n_cordas)
        self.amplificacao = amplificacao
        self.escala = escala

class Violao(Instrument):
    def __init__(self, marca, modelo, valor, n_cordas, afinador:bool):
        super().__init__(marca, modelo, valor, n_cordas)
        self.afinador = afinador











