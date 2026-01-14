import random
from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome):
        self.nome = nome
        

    @abstractmethod
    def atacar(self, arma):
        pass

    @abstractmethod
    def defesa(self, dano_inimigo):
        pass


#armas -------------


class Arma(ABC):
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

        @abstractmethod
        def gerar_dano(self):
            pass

class ArmaEnvenenada(Arma):
    def __init__(self):
        super().__init__(nome = 'adaga envenenada', dano = 30)

    def gerar_dano(self):
        if random.randint(2, 3) == 3:
            return self.dano * 2.5
        else: 
            return self.dano

class Machado(Arma):
    def __init__(self):
        super().__init__(nome = 'machado', dano = 40)
        

    def gerar_dano(self):
        if random.randint(3, 5) == 5:
            return 60
        else:
            return self.dano 
        
class CajadoMago(Arma):
    def __init__(self):
        super().__init__(nome = 'cajado', dano = 0)

    def gerar_dano(self):
        chance = random.randint(1, 3) 
        if chance == 3:
            return 60
        elif chance == 2:
            return 40
        else:
            return 20

class Arco(Arma):
    def __init__(self):
        super().__init__(nome = 'Arco', dano = 70)

    def gerar_dano(self):
        if random.randint(1, 3) == 3:
            return 70
        else:
            return 0



# instanciando armas -------
cajado = CajadoMago()
adaga_envenenada = ArmaEnvenenada()
machado = Machado()
arco = Arco()
#print(machado.gerar_dano())

# bonecos ----------------


class Tank(Personagem):
    def __init__(self, nome, arma):
        super().__init__(nome)
        self.vida = 120
        self.arma = arma
        self.nome_classe = 'Tank'

    def atacar(self):
        dano_base = self.arma.gerar_dano()
        if isinstance(self.arma, CajadoMago) or isinstance(self.arma, Arco):
            print(f'{self.nome} nao tem muita aptidão com {self.arma.nome} e deu pouco dano')
            return dano_base * 0.1
        return dano_base
    
    def defesa(self, ataque_inimigo):
        dano_inimigo = ataque_inimigo
        self.vida -= dano_inimigo * 0.6
        return self.vida 



class Mago(Personagem):
    def __init__(self, nome, arma):
        super().__init__(nome)
        self.vida = 100
        self.arma = arma
        self.nome_classe = 'Mago'
    
    def atacar(self):
        dano_base = self.arma.gerar_dano()
        if not isinstance(self.arma, CajadoMago):
            print(f'o {self.nome} nao sabe usar {self.arma.nome} e causou pouco dano')
            return dano_base * 0.5
        return dano_base
    
    def defesa(self, ataque_inimigo):
        dano_inimigo = ataque_inimigo
        self.vida -= dano_inimigo
        return self.vida

class Guerreiro(Personagem):
    def __init__(self, nome, arma):
        super().__init__(nome)
        self.vida = 120
        self.arma = arma
        self.nome_classe = 'Guerreiro'
    
    def atacar(self):
        dano_base = self.arma.gerar_dano()
        if isinstance(self.arma, CajadoMago):
            return dano_base * 0.1
        return dano_base
    


    def defesa(self, ataque_inimigo):
        dano_inimigo = ataque_inimigo
        self.vida -= dano_inimigo
        return self.vida




