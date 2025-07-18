import streamlit as st
import matplotlib.pyplot as plt

# Título principal com a identidade AFZF
st.title("Calculadora de Gestão de Banca - **AFZF**")

# Subtítulo explicativo
st.subheader("Gerencia a tua banca de apostas de forma inteligente e estratégica!")

# Seção de Explicações Gerais
st.markdown("""
    **Como funciona:**
    - **Valor total da tua banca (€):** Este é o valor que tens disponível para apostas.
    - **Valor para a COR (€):** Este valor é calculado automaticamente como **3% da tua banca**.
    - **Valor para Empate (€):** Este valor é calculado como **10% do valor apostado na COR**.
    - **Meta de Lucro:** Defina a sua meta de lucro e veja quantos **greens** são necessários para atingi-la.
""")

# Seção para Inputs do Usuário
st.markdown("### 1. Defina o valor da sua banca")
total_banca = st.number_input("Valor total da tua banca (€):", min_value=0.0, value=200.0, step=0.01, format="%.2f")

# Verificação para garantir que o valor da banca seja positivo
if total_banca <= 0:
    st.warning("O valor da banca deve ser maior que 0. Por favor, insira um valor válido.")

# Definindo a Meta de Lucro
meta_lucro = st.number_input("Meta de Lucro (€):", min_value=0.0, value=50.0, step=0.01)

# Verificação para garantir que a meta de lucro seja positiva
if meta_lucro <= 0:
    st.warning("A meta de lucro deve ser maior que 0. Por favor, insira uma meta válida.")

# Cálculos automáticos para COR e Empate
valor_cor = total_banca * 0.03  # 3% da banca para COR
valor_empate = valor_cor * 0.10  # 10% do valor da COR para Empate

# Exibição dos resultados de COR e Empate
st.markdown("### 2. Valor Calculado para a COR e Empate")
st.markdown(f"**Valor para a COR (€):** €{valor_cor:.2f}")
st.markdown(f"**Valor para Empate (€):** €{valor_empate:.2f}")

# Seção de Stop Win e Stop Loss
st.markdown("### 3. Cálculo de Stop Win e Stop Loss")
# O Stop Win será igual à meta de lucro
stop_win = meta_lucro  # O Stop Win deve ser o valor que o usuário define como objetivo de lucro
stop_loss = total_banca * 0.18  # O Stop Loss permanece como 18% da banca

st.markdown(f"**Stop WIN (Meta de Lucro):** + €{stop_win:.2f}")
st.markdown(f"**Stop LOSS:** - €{stop_loss:.2f}")

# Cálculo dos greens necessários para atingir a meta de lucro
lucro_por_green = valor_cor  # O lucro por green é igual ao valor apostado na COR
greens_necessarios = meta_lucro / lucro_por_green  # Dividir a meta pelo lucro por green

st.markdown(f"**Quantos greens são necessários para atingir a meta de lucro de €{meta_lucro:.2f}:**")
st.markdown(f"Você precisa de **{greens_necessarios:.1f}** greens para atingir a meta de lucro.")

# **Segredo Extra**: Feedback visual dinâmico para meta de lucro
if greens_necessarios <= 1:
    st.markdown("<p style='color:green; font-size: 18px;'>Parabéns! Você já está bem perto de atingir a sua meta com poucos greens. Mantenha o foco!</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:red; font-size: 18px;'>Ainda faltam alguns greens para atingir a meta. Vamos lá!</p>", unsafe_allow_html=True)

# Gráfico de Evolução da Banca (Simulação)
st.markdown("### 4. Gráfico de Evolução da Banca")
with st.expander("Mostrar Gráfico de Evolução da Banca"):  # Usar o novo método st.expander
    # Criando um gráfico simples para ilustrar a evolução da banca
    fig, ax = plt.subplots(figsize=(6, 4))  # Reduzir o tamanho do gráfico
    x = [0, 1, 2, 3, 4]
    y = [total_banca, total_banca + valor_cor, total_banca + valor_cor * 2, total_banca + valor_cor * 3, total_banca + valor_cor * 4]
    ax.plot(x, y, label="Evolução da Banca", color='dodgerblue')
    ax.set_title("Evolução da Banca após Greens")
    ax.set_xlabel("Número de Greens")
    ax.set_ylabel("Valor da Banca (€)")
    ax.legend()
    st.pyplot(fig)

# Botão para Resetar os valores
st.markdown("### 5. Ações de Interação")
reset = st.button("Resetar Valores")
if reset:
    # Ao pressionar o botão, limpa os valores e pede ao usuário para recarregar a página
    st.write("Os valores foram resetados. Por favor, recarregue a página para começar novamente.")

# Regras de gestão de banca
st.markdown("### 6. Regras do AFZF")
st.markdown("""
- **3%** da banca para a COR.
- **10%** da entrada na COR é reservada para o Empate.
- **Banca mínima:** € 50.
- **Banca recomendada:** € 600.
""")

# Mensagem final de motivação
st.markdown("### 7. Mensagem de Motivação")
st.write("Com AFZF, as tuas apostas têm mais **estratégia** e **controlo**. Aposta com inteligência!")

# Adicionando a marca AI™ e AFZF®
st.markdown("<h5 style='color:#9c27b0;'>Config com AI™ by AFZF®</h5>", unsafe_allow_html=True)

# Links úteis para o usuário
st.markdown("""
    ### Links úteis:
    - [Gestão de Banca Responsável](https://www.somesite.com)
    - [Apostas Responsáveis](https://www.anotherlink.com)
""")

# Personalização do Layout: Mudando a cor de fundo e fontes
st.markdown("""
    <style>
        .reportview-container {
            background-color: #f5f5f5; /* Cor de fundo clara e profissional */
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
        }
        h1 {
            font-family: 'Arial', sans-serif;
            color: #333333; /* Título com cor escura para melhor leitura */
        }
        h3 {
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
        .stButton button {
            background-color: #4CAF50; /* Cor do botão em verde */
            color: white;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)
