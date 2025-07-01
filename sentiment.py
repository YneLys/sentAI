from textblob import TextBlob

def analisar_sentimento(texto: str) -> str:
    blob = TextBlob(texto)
    polaridade = blob.sentiment.polarity

    if polaridade > 0:
        return "Positivo"
    elif polaridade < 0:
        return "Negativo"
    else:
        return "Neutro"
