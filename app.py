import streamlit as st

# Título do aplicativo com a identidade AFZF
st.title("Calculadora de Gestão de Banca - AFZF")

# Subtítulo explicativo
st.subheader("Gerencia a tua banca de apostas de forma inteligente!")

# Explicações sobre os valores
st.markdown("""
**Como funciona:**
- **Valor total da tua banca (€):** Este é o valor que tens disponível para apostas.
- **Valor para a COR (€):** Este valor é calculado automaticamente como **3% da tua banca**.
- **Valor para Empate (€):** Este valor é calculado como **10% do valor apostado na COR**.
""")

# Input para o valor da banca
total_banca = st.number_input("Valor total da tua banca (€):", min_value=0.0, value=200.0, step=0.01)

# Cálculos automáticos dos valores da COR e do Empate
valor_cor = total_banca * 0.03  # 3% da banca para COR
valor_empate = valor_cor * 0.10  # 10% do valor da COR para Empate

# Exibir os valores calculados automaticamente
st.write(f"**Valor para a COR (€):** €{valor_cor:.2f}")
st.write(f"**Valor para Empate (€):** €{valor_empate:.2f}")

# Cálculos para Stop Win e Stop Loss
stop_win = total_banca * 0.09  # 9% da banca para Stop WIN
stop_loss = total_banca * 0.18  # 18% da banca para Stop LOSS

# Exibir os resultados calculados de Stop Win e Stop Loss
st.write(f"**Stop WIN**: + €{stop_win:.2f}")
st.write(f"**Stop LOSS**: - €{stop_loss:.2f}")

# Definir a meta de lucro
meta_lucro = st.number_input("Meta de Lucro (€):", min_value=0.0, value=50.0, step=0.01)

# Calcular quantos greens são necessários para atingir a meta de lucro
# Considerando que o lucro por green é o valor apostado na COR
lucro_por_green = valor_cor  # O lucro por green é igual ao valor apostado na COR
greens_necessarios = meta_lucro / lucro_por_green  # Dividir a meta pelo lucro por green

# Exibir quantos greens são necessários
st.write(f"**Quantos greens são necessários para atingir a meta de lucro de €{meta_lucro:.2f}:**")
st.write(f"Você precisa de **{greens_necessarios:.1f}** greens para atingir a meta de lucro.")

# Regras adaptadas para o estilo AFZF
st.subheader("Regras do AFZF:")
st.markdown("""
- 3% da banca para a COR
- Protege o empate com 10% da tua entrada
- Banca mínima: € 50
- Banca recomendada: € 600
""")

# Mensagem final de motivação :)
st.write("Com AFZF, as tuas apostas têm mais estratégia e controlo!")
