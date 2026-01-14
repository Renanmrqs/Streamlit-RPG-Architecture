# ⚔️ Coliseu de Batalha Dinâmico

Este é um simulador de batalhas RPG desenvolvido em **Python**, utilizando a biblioteca **Streamlit** para a interface gráfica. O projeto foca na aplicação de conceitos avançados de **Programação Orientada a Objetos (POO)** e gestão de estado em aplicações Web.

## 🚀 Funcionalidades

- **Criação de Personagem:** Escolha personalizada de nome, classe (Guerreiro, Tank, Mago) e arma.
- **NPC Aleatório:** Oponente gerado dinamicamente com nomes reais (via biblioteca `Faker`) e combinações aleatórias de classe/arma.
- **Sistema de Batalha:** Lógica de turnos com cálculos de dano baseados em proficiência e tipos de armas.
- **Interface Intuitiva:** Exibição de HP em tempo real, métricas de armas e log de combate detalhado.

## 🛠️ Tecnologias Utilizadas

- **Python 3.14.2**: Linguagem base.
- **Streamlit**: Framework para a criação da interface web.
- **Faker**: Geração de dados aleatórios para NPCs.
- **POO Avançada**: Uso de classes abstratas, herança e polimorfismo.

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

Desenvolvido por: Renan - Focado em evoluir e buscar novas oportunidades!