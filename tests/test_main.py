import os
import pandas as pd
from herois import Guerreiro, Tank, machado, Mago, cajado
from main import salvar_historico

def test_vida_inicial():
    gandalf = Mago('gandalf', cajado)
    
    assert gandalf.vida == 100



def test_dano_guerreiro():
    marcos_guerreiro = Guerreiro ('marcos', machado)
    
    assert marcos_guerreiro.atacar() == 60 or 40


def test_defesa_tank():
    marcos_guerreiro = Guerreiro ('marcos', machado)
    sergio_1 = Tank('sergio', machado)
    sergio_2 = Tank('sergio', cajado)
    

    assert marcos_guerreiro.defesa(sergio_1.atacar()) == 36 or 24
    assert marcos_guerreiro.defesa(sergio_2.atacar()) != 36 or 24
    

def test_save_historico():
    arquivo_teste = 'historico_batalhas.csv'
    vencedor = 'mario'
    perdedor = 'marco'
    turnos = 5

    if os.path.exists(arquivo_teste):
        os.remove(arquivo_teste)
    
    salvar_historico(vencedor, perdedor, turnos)
    
    assert os.path.exists(arquivo_teste), 'Arquivo CSV nao foi criado'

    df = pd.read_csv(arquivo_teste)

    assert len(df) == 1, 'CSV deveria ter 1 linha'

    assert df.iloc[0]['Vencedor'] == vencedor
    assert df.iloc[0]['Perdedor'] == perdedor
    assert df.iloc[0]['Turnos'] == turnos

    os.remove(arquivo_teste)