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
""")

# Seção para Inputs do Usuário
st.markdown("<h3 style='color:#ff5722;'>1. Defina o valor da sua banca</h3>", unsafe_allow_html=True)
total_banca = st.number_input("Valor total da tua banca (€):", min_value=0.0, value=200.0, step=0.01, format="%.2f")

# Cálculos automáticos para COR e Empate
valor_cor = total_banca * 0.03  # 3% da banca para COR
valor_empate = valor_cor * 0.10  # 10% do valor da COR para Empate

# Exibição dos resultados de COR e Empate com cores e destaque
st.markdown("<h3 style='color:#4caf50;'>2. Valor Calculado para a COR e Empate</h3>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #00bcd4; font-size: 20px; font-weight: bold;'>**Valor para a COR (€):** €{valor_cor:.2f}</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #00bcd4; font-size: 20px; font-weight: bold;'>**Valor para Empate (€):** €{valor_empate:.2f}</span>", unsafe_allow_html=True)

# Seção de Stop Win e Stop Loss
st.markdown("<h3 style='color:#ff9800;'>3. Cálculo de Stop Win e Stop Loss</h3>", unsafe_allow_html=True)

# Ajustando os valores de Stop Win e Stop Loss com base na Meta de Lucro
meta_lucro = st.number_input("Meta de Lucro (€):", min_value=0.0, value=50.0, step=0.01)

# Agora, o Stop Win será igual à meta de lucro
stop_win = meta_lucro  # O Stop Win deve ser o valor que o usuário define como objetivo de lucro
stop_loss = total_banca * 0.18  # O Stop Loss permanece como 18% da banca, mas pode ser ajustado conforme necessário

st.markdown(f"<span style='color: #ff9800; font-size: 20px; font-weight: bold;'>**Stop WIN (Meta de Lucro):** + €{stop_win:.2f}</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #ff9800; font-size: 20px; font-weight: bold;'>**Stop LOSS:** - €{stop_loss:.2f}</span>", unsafe_allow_html=True)

# Cálculo dos greens necessários para atingir a meta de lucro
lucro_por_green = valor_cor  # O lucro por green é igual ao valor apostado na COR
greens_necessarios = meta_lucro / lucro_por_green  # Dividir a meta pelo lucro por green

st.markdown(f"<span style='color: #2196f3; font-size: 20px; font-weight: bold;'>**Quantos greens são necessários para atingir a meta de lucro de €{meta_lucro:.2f}:**</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: #2196f3; font-size: 24px; font-weight: bold;'>Você precisa de **{greens_necessarios:.1f}** greens para atingir a meta de lucro.</span>", unsafe_allow_html=True)

# **Segredo Extra**: Feedback visual dinâmico para meta de lucro
if greens_necessarios <= 1:
    st.markdown("<p style='color:green; font-size: 20px;'>Parabéns! Você já está bem perto de atingir a sua meta com poucos greens. Mantenha o foco!</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:red; font-size: 20px;'>Ainda faltam alguns greens para atingir a meta. Vamos lá!</p>", unsafe_allow_html=True)

# Regras de gestão de banca
st.markdown("<h3 style='color:#2196f3;'>4. Regras do AFZF</h3>", unsafe_allow_html=True)
st.markdown("""
- **3%** da banca para a COR.
- **10%** da entrada na COR é reservada para o Empate.
- **Banca mínima:** € 50.
- **Banca recomendada:** € 600.
""")

# Mensagem final de motivação
st.markdown("<h3 style='color:#9c27b0;'>5. Mensagem de Motivação</h3>", unsafe_allow_html=True)
st.write("Com AFZF, as tuas apostas têm mais **estratégia** e **controlo**. Aposta com inteligência!")

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
