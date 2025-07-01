# 💬 Classificador de Sentimentos de Comentários

Este projeto utiliza **IA com NLP (TextBlob)** para analisar o sentimento de comentários/textos. Classifica a entrada como **Positivo**, **Negativo** ou **Neutro**, com interface interativa feita em **Streamlit**.

## 🔧 Tecnologias
- Python
- NLP com TextBlob
- Streamlit

## 🚀 Como executar

1. Clone este repositório:
```bash
git clone https://github.com/seuusuario/sentiment-analyzer.git
cd sentiment-analyzer
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

3. Execute o app:
```bash
streamlit run app.py
```

## 📌 Exemplo de uso

Digite um texto como:
> "O atendimento foi excelente!"

E o app retorna:
> Sentimento detectado: **Positivo**

---

## 📄 Licença
MIT
