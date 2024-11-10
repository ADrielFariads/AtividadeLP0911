from enum import Enum

class Instrumento:
    def __init__(self, marca:str, modelo:str, valor:int|float, n_cordas:int):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.n_cordas = n_cordas

    def __str__(self):
         return f"{self.modelo} ({self.marca}), {self.n_cordas} cordas, R${self.valor:.2f}"
    
class Guitarra(Instrumento):
    def __init__(self, marca, modelo, valor, n_cordas, captador:str):
        super().__init__(marca, modelo, valor, n_cordas)
        self.captador = captador
    
    def __str__(self):
        return f"{super().__str__()}, captador: {self.captador}"
    
class Baixo(Instrumento):
    def __init__(self, marca, modelo, valor, n_cordas, escala, amplificacao:str):
        super().__init__(marca, modelo, valor, n_cordas)
        self.amplificacao = amplificacao
        self.escala = escala

    def __str__(self):
        return f"{super().__str__()}, escala:{self.escala}, amplificação: {self.amplificacao}"

class Violao(Instrumento):
    def __init__(self, marca, modelo, valor, n_cordas, afinador:bool):
        super().__init__(marca, modelo, valor, n_cordas)
        self.afinador = afinador

    def __str__(self):
        afinador_info = "com afinador embutido" if self.afinador else "sem afinador embutido"
        return f"{super().__str__()} - {afinador_info}"
    
#violao = Violao("XYZ", "abc", 3000, 6, True)
#print(violao.__str__())


class Cargo(Enum):
    DIRETOR = "Diretor"
    SUPERVISOR = "Supervisor"
    GERENTE = "Gerente"
    VENDEDOR = "Vendedor"
    ATENDENTE = "Atendente"



class Loja:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.trabalhadores = []

    def __str__(self):
        return f"{self.nome} localizada em {self.localizacao}"

    def adicionar_trabalhador(self, funcionario):
        if funcionario not in self.trabalhadores:
            self.trabalhadores.append(funcionario)
        else:
            print(f"{funcionario.nome} já está trabalhando nessa loja.")

    def remover_trabalhador(self, funcionario):
        if funcionario in self.trabalhadores:
            self.trabalhadores.remove(funcionario)
        else: 
            print(f"{funcionario.nome} não trabalha aqui.")
    

    
class Trabalhador:
    def __init__(self, nome:str, cpf:str, salario:float, cargo:Cargo, loja_atual:Loja):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
        self.loja_atual = loja_atual
        loja_atual.adicionar_trabalhador(self)

    def __str__(self):
        return f"{self.nome}, CPF: {self.cpf}, Cargo: {self.cargo.value}, Salário: R${self.salario:.2f}, trabalha em {self.loja_atual.nome}"


