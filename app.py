import streamlit as st

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
""", unsafe_allow_html=True)

# Seção para Inputs do Usuário
st.markdown("<h3 style='color:#00bcd4;'>1. Defina o valor da sua banca</h3>", unsafe_allow_html=True)
total_banca = st.number_input("Valor total da tua banca (€):", min_value=0.0, value=200.0, step=0.01, format="%.2f")

# Cálculos automáticos para COR e Empate
valor_cor = total_banca * 0.03  # 3% da banca para COR
valor_empate = valor_cor * 0.10  # 10% do valor da COR para Empate

# Exibição dos resultados de COR e Empate
st.markdown("<h3 style='color:#4caf50;'>2. Valor Calculado para a COR e Empate</h3>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #4caf50; font-size: 18px;'>**Valor para a COR (€):** €{valor_cor:.2f}</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #4caf50; font-size: 18px;'>**Valor para Empate (€):** €{valor_empate:.2f}</span>", unsafe_allow_html=True)

# Seção de Stop Win e Stop Loss
st.markdown("<h3 style='color:#ff9800;'>3. Cálculo de Stop Win e Stop Loss</h3>", unsafe_allow_html=True)
stop_win = total_banca * 0.09  # 9% da banca para Stop WIN
stop_loss = total_banca * 0.18  # 18% da banca para Stop LOSS

st.markdown(f"<span style='color: #ff9800; font-size: 18px;'>**Stop WIN:** + €{stop_win:.2f}</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #ff9800; font-size: 18px;'>**Stop LOSS:** - €{stop_loss:.2f}</span>", unsafe_allow_html=True)

# Seção da Meta de Lucro
st.markdown("<h3 style='color:#f44336;'>4. Defina a Meta de Lucro</h3>", unsafe_allow_html=True)
meta_lucro = st.number_input("Meta de Lucro (€):", min_value=0.0, value=50.0, step=0.01)

# Cálculo dos greens necessários para atingir a meta de lucro
lucro_por_green = valor_cor  # O lucro por green é igual ao valor apostado na COR
greens_necessarios = meta_lucro / lucro_por_green  # Dividir a meta pelo lucro por green

st.markdown(f"<span style='color: #2196f3; font-size: 18px;'>**Quantos greens são necessários para atingir a meta de lucro de €{meta_lucro:.2f}:**</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #2196f3; font-size: 20px; font-weight: bold;'>Você precisa de **{greens_necessarios:.1f}** greens para atingir a meta de lucro.</span>", unsafe_allow_html=True)

# **Segredo Extra**: Feedback visual dinâmico para meta de lucro
if greens_necessarios <= 1:
    st.markdown("<p style='color:green; font-size: 18px;'>✨ Parabéns! Você já está bem perto de atingir a sua meta com poucos greens. Mantenha o foco!</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:red; font-size: 18px;'>⏳ Ainda faltam alguns greens para atingir a meta. Vamos lá! 👊</p>", unsafe_allow_html=True)

# Regras de gestão de banca
st.markdown("<h3 style='color:#2196f3;'>5. Regras do AFZF</h3>", unsafe_allow_html=True)
st.markdown("""
- **3%** da banca para a COR.
- **10%** da entrada na COR é reservada para o Empate.
- **Banca mínima:** € 50.
- **Banca recomendada:** € 600.
""", unsafe_allow_html=True)

# Mensagem final de motivação
st.markdown("<h3 style='color:#9c27b0;'>6. Mensagem de Motivação</h3>", unsafe_allow_html=True)
st.write("Com AFZF, as tuas apostas têm mais **estratégia** e **controlo**. Aposta com inteligência!")

# Personalização do Layout: Mudando a cor de fundo e fontes
st.markdown("""
    <style>
        .reportview-container {
            background-color: #121212; /* Cor de fundo escura */
        }
        .sidebar .sidebar-content {
            background-color: #1f1f1f;
        }
        h1 {
            font-family: 'Arial', sans-serif;
            color: #ffffff;
        }
        h3 {
            font-family: 'Arial', sans-serif;
            color: #ffffff;
        }
        .stButton button {
            background-color: #ff5722;
            color: white;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)
