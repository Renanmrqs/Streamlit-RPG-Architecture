# ⚔️ Coliseu de Batalha Dinâmico
> 📢 **Update (Jan/2026): Módulo de Analytics Adicionado!**
> Agora o projeto conta com persistência de dados em CSV e Dashboards automáticos com Pandas.

Este é um simulador de batalhas RPG desenvolvido em **Python**, utilizando a biblioteca **Streamlit** para a interface gráfica. O projeto foca na aplicação de conceitos avançados de **Programação Orientada a Objetos (POO)** e gestão de estado em aplicações Web.

## 🚀 Funcionalidades

- **Criação de Personagem:** Escolha personalizada de nome, classe (Guerreiro, Tank, Mago) e arma.
- **NPC Aleatório:** Oponente gerado dinamicamente com nomes reais (via biblioteca `Faker`) e combinações aleatórias de classe/arma.
- **Sistema de Batalha:** Lógica de turnos com cálculos de dano baseados em proficiência e tipos de armas.
- **Interface Intuitiva:** Exibição de HP em tempo real, métricas de armas e log de combate detalhado.
- **Analytics e Persistência de Dados:** Além da lógica de combate, implementei um sistema de ETL simplificado usando Pandas:
1. *Extração:* A cada batalha finalizada, os dados (Vencedor, Perdedor, Turnos) são capturados.
2. *Carga (Persistence):* Os dados são salvos incrementalmente em um arquivo local (`.csv`), simulando um banco de dados.
3. *Visualização:* Uso do *Streamlit* para ler o CSV e gerar gráficos de performance em tempo real.
[Dashboard Preview](Dashboard_preview.png)

## 🛠️ Tecnologias Utilizadas

- **Python 3.14.2**: Linguagem base.
- **Streamlit**: Framework para a criação da interface web.
- **Faker**: Geração de dados aleatórios para NPCs.
- **POO Avançada**: Uso de classes abstratas, herança e polimorfismo.
- **Pandas**: Framework de manipulação e análise de dados.

## 📦 Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/Renanmrqs/rpg-classes-python.git](https://github.com/renanmrqs/rpg-classes-python.git)
   cd rpg-classes-python

2. **Criar e ativar o ambiente virtual (Recomendado):**
python -m venv venv
# No Windows:
.\venv\Scripts\activate

3. **Instalar as dependencias:**
pip install -r requirements.txt

4. **Executar a aplicação:**
streamlit run main.py

## 🧠 Conceitos Aplicados

**Este projeto foi construído para demonstrar maturidade técnica em:**

*Gestão de Estado (st.session_state): Persistência de objetos na memória RAM durante a interação do usuário.*

*Mapeamento Dinâmico: Uso de dicionários para instanciar classes de forma escalável, evitando excesso de estruturas condicionais (if/else).*

*Arquitetura de Software: Separação da lógica de combate (backend) da camada de visualização (frontend).*

*Analytics e Persistencia de Dados: Dashboard interrativo, com persistencia de dados.*


Desenvolvido por: Renan - Focado em evoluir e buscar novas oportunidades!