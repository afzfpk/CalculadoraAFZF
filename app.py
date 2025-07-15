import streamlit as st

# Título do aplicativo com a identidade AFZF
st.title("Calculadora de Gestão de Banca - AFZF")

# Subtítulo explicativo
st.subheader("Gerencia a tua banca de apostas de forma inteligente!")

# Inputs para o valor da banca, valor para COR e valor para Empate
total_banca = st.number_input("Valor total da tua banca (€):", min_value=0, value=200)
valor_cor = st.number_input("Valor para a COR (€):", min_value=0, value=6.00)
valor_empate = st.number_input("Valor para Empate (€):", min_value=0, value=0.60)

# Cálculos para Stop Win e Stop Loss, adaptando a tua lógica
stop_win = total_banca * 0.09  # Exemplo: 9% da banca para Stop WIN
stop_loss = total_banca * 0.18  # Exemplo: 18% da banca para Stop LOSS

# Exibir os resultados calculados
st.write(f"**Stop WIN**: + €{stop_win:.2f}")
st.write(f"**Stop LOSS**: - €{stop_loss:.2f}")

# Regras adaptadas para o estilo AFZF
st.subheader("Regras do AFZF:")
st.markdown("""
- 3% da banca para a COR
- Protege o empate com 10% da tua entrada
- Banca mínima: € 50
- Banca recomendada: € 600
""")

# Imagem personalizada do AFZF (certifica-te de que o logo está no mesmo diretório que o código)
st.image("afzf_logo.png", caption="AFZF - Aposta com inteligência!", use_column_width=True)

# Mensagem final de motivação :)
st.write("Com AFZF, as tuas apostas têm mais estratégia e controlo!")
