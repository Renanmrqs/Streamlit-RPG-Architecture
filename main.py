import herois
import streamlit as st
from faker import Faker
import random
import pandas as pd
import os

st.markdown("""
    <style>
        audio { display: none; }    
    </style>  """, unsafe_allow_html=True)

def salvar_historico(vencedor, perdedor, turnos):
    arquivo = 'historico_batalhas.csv'
    novo_dado = {'Vencedor': [vencedor], 'Perdedor': [perdedor], 'Turnos': [turnos]}
    df_novo = pd.DataFrame(novo_dado)

    if os.path.exists(arquivo):
        df_novo.to_csv(arquivo, mode='a', header=False, index=False)
    else:
        df_novo.to_csv(arquivo, index=False)



fake = Faker('pt_BR')

armas = {'Machado': herois.machado, 
    'Arco': herois.arco,
    'Cajado': herois.cajado,
    'Adaga Envenenada': herois.adaga_envenenada
}
classes = {'Guerreiro':herois.Guerreiro, 'Tank': herois.Tank, 'Mago': herois.Mago}

armas_list = list(armas.values())
classes_list = list(classes.values())


st.title('--- Coliseu de Batalha Dinamico---')

st.subheader('⚔️ Arsenal Disponível')
col_a, col_b, col_c, col_d = st.columns(4)

with col_a:
    st.metric(label='Adaga Envenenada', value='30 Dano', delta='Critico 2.5x')
with col_b:
    st.metric(label='Machado', value='40 Dano', delta='Dano pesado 60')
with col_c:
    st.metric(label='Arco', value='70 Dano', delta='Chance de errar')
with col_d:
    st.metric(label='Cajado', value='20 a 60 Dano', delta='Dano escalonado')

with st.expander('Conheça as Classes'):
    st.write("""
    * **Guerreiro:** 120HP. Equilibrado. Sofre debuff ao usar cajado.
    * **Tank:** 120HP. O Forte. Tem 40% de vida extra ao se defender. Sofre debuff ao usar cajado.
    * **Mago:** 100HP. O Maestro. Tem aptidao com cajado. Sofre debuff ao usar qualquer outra arma.
    
""")

st.title('---Configuração do seu Boneco---')

with st.container():
    st.subheader('Configure seu boneco')
    col1, col2, col3 = st.columns(3)

    with col1:
        nome_usuario = st.text_input('Nome do seu Boneco', )
    with col2:
        classe_usuario = st.selectbox('Classe do seu Boneco', list(classes.keys()))
    with col3:
        arma_usuario = st.selectbox('Arma do seu Boneco', list(armas.keys()))

if st.button("🔥 COMEÇAR A BATALHA"):
    nome_aleatorio = fake.name()

    classe_npc = random.choice(classes_list)
    arma_npc = random.choice(armas_list)
    st.session_state.player = classes[classe_usuario](nome_usuario, armas[arma_usuario])
    st.session_state.npc = classe_npc(nome_aleatorio, arma_npc)
    
    st.session_state.log = []

    st.success(f'Batalha iniciada: {st.session_state.player.nome} VS {st.session_state.npc.nome}')

if 'player' in st.session_state:
    p = st.session_state.player
    n = st.session_state.npc
    
    if p.vida > 0 and n.vida > 0:
        if st.button('💥 DAR UM GOLPE'):
            st.audio('som_dano.mp4', format='audio/mp4', autoplay=True)
            n.defesa(p.atacar())
            st.session_state.log.append(f'{p.nome} atacou! {n.nome} ficou com {n.vida:.1f} HP.')

            if n.vida > 0:
                p.defesa(n.atacar())
                st.session_state.log.append(f'{n.nome} contra-atacou! {p.nome} ficou com {p.vida:.1f} HP.')
            if n.vida <= 0:
                st.session_state.log.append(f'🏆{p.nome} venceu a batalha!')
                st.warning('A batalha acabou! Caso queira brincar denovo clique em ''Começar a Batalha'' ')
                st.balloons()
                salvar_historico(p.nome, n.nome, len(st.session_state.log))
            elif p.vida <= 0:
                st.session_state.log.append(f'🏆{n.nome} venceu a batalha! Sobra nada pro beta!')
                st.warning('A batalha acabou! Caso queira brincar denovo clique em ''Começar a Batalha'' ')
                st.balloons()
                salvar_historico(n.nome, p.nome, len(st.session_state.log))

        st.divider()
        c1, c2 = st.columns(2)
        c1.metric(f'Hp {p.nome}', f'{p.vida:.1f}')
        c2.metric(f'Hp {n.nome}', f'{n.vida:.1f}')

        for registro in reversed(st.session_state.log):
            st.write(registro)

        st.divider()
        st.subheader("📊 Histórico do Coliseu")
        if os.path.exists('historico_batalhas.csv'):
            df = pd.read_csv('historico_batalhas.csv')
            st.dataframe(df)

            st.bar_chart(df['Vencedor'].value_counts())






