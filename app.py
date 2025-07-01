import streamlit as st
from sentiment import analisar_sentimento

st.set_page_config(page_title="Analisador de Sentimentos", page_icon="💬")

st.title("💬 Classificador de Sentimentos de Comentários")
st.markdown("Digite um comentário abaixo para analisar o sentimento com **TextBlob** (IA de linguagem natural).")

comentario = st.text_area("✏️ Comentário")

if st.button("🔍 Analisar Sentimento"):
    if comentario.strip() == "":
        st.warning("Por favor, digite um comentário.")
    else:
        resultado = analisar_sentimento(comentario)
        st.success(f"Sentimento detectado: **{resultado}**")
