from enum import Enum
class Cargo(Enum):
    DIRETOR = "Diretor"
    SUPERVISOR = "Supervisor"
    GERENTE = "Gerente"
    VENDEDOR = "Vendedor"
    ATENDENTE = "Atendente"

class Acao(Enum):
    REMOVER = "remover"
    ADICIONAR = "adicionar"


class Loja:
    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
        self.trabalhadores = []
        self.estoque = {
            "guitarra": [],
            "baixo": [],
            "violao":[]}

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
    
    def alterar_estoque(self, instrumento, acao):
        tipo_instrumento = instrumento.__class__.__name__.lower()
        if tipo_instrumento not in self.estoque.keys():
            print("tipo de instrumento inválido!")
            return None

        if acao == Acao.ADICIONAR:
            self.estoque[tipo_instrumento].append(instrumento)

        elif acao == Acao.REMOVER:
            if instrumento in self.estoque[instrumento]:
                self.estoque[tipo_instrumento].remove(instrumento)
            else:
                print(f"{instrumento} não está no estoque da loja")
        
    def consultar_instrumentos(self):
        print(f"Guitarras na loja: {len(self.estoque['guitarra1'])}", 
              f"Violões na loja: {len(self.estoque['violão'])}",
              f"Baixos na loja: {len(self.estoque['baixo'])}")
        
    def consultar_funcionarios_por_cargo(self):
        cargos_contagem = {cargo: 0 for cargo in Cargo}  
        for trabalhador in self.trabalhadores:
            cargos_contagem[trabalhador.cargo] += 1
        for cargo, contagem in cargos_contagem.items():
            print(f"{cargo.value}: {contagem} funcionário(s)")
    
    def __del__(self):
        print(f"A loja {self.nome} foi apagada.")
        for tipo, instrumentos in self.estoque.items():
            for instrumento in instrumentos:
                del instrumento
###############################################################################################
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

##### INSTRUMENTOS ###############################################################################################

class Instrumento:
    def __init__(self, marca:str, modelo:str, valor:int|float, n_cordas:int, loja:Loja):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.n_cordas = n_cordas
        loja.alterar_estoque(self, Acao.ADICIONAR)

    def __str__(self):
         return f"{self.modelo} ({self.marca}), {self.n_cordas} cordas, R${self.valor:.2f}"
    
class Guitarra(Instrumento):
    def __init__(self, marca:str, modelo:str, valor:int|float, n_cordas:int, loja:Loja, captador:str):
        super().__init__(marca, modelo, valor, n_cordas, loja)
        self.captador = captador
    
    def __str__(self):
        return f"{super().__str__()}, captador: {self.captador}"
    
class Baixo(Instrumento):
    def __init__(self, marca, modelo, valor, n_cordas, escala, amplificacao:str, loja):
        super().__init__(marca, modelo, valor, n_cordas, loja)
        self.amplificacao = amplificacao
        self.escala = escala

    def __str__(self):
        return f"{super().__str__()}, escala:{self.escala}, amplificação: {self.amplificacao}"

class Violao(Instrumento):
    def __init__(self, marca, modelo, valor, n_cordas, afinador:bool, loja):
        super().__init__(marca, modelo, valor, n_cordas, loja)
        self.afinador = afinador

    def __str__(self):
        afinador_info = "com afinador embutido" if self.afinador else "sem afinador embutido"
        return f"{super().__str__()} - {afinador_info}"
    
#violao = Violao("XYZ", "abc", 3000, 6, True)
#print(violao.__str__())

loja1 = Loja("abc", "São Paulo")
joao = Trabalhador("João", "12378945612", 2500, Cargo.VENDEDOR, loja1)
nelson = Guitarra("XZZ", "zzx", 3000, 6, loja1, "malagoli")
loja1.alterar_estoque(nelson, Acao.ADICIONAR)

print(loja1)
print(joao)
print(nelson)

del(loja1)

