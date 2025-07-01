from pysentimiento import create_analyzer

analisador = create_analyzer(task="sentiment", lang="pt")

def analisar_sentimento(texto: str) -> str:
    resultado = analisador.predict(texto)
    label = resultado.output

    if label == "POS":
        return "Positivo"
    elif label == "NEG":
        return "Negativo"
    else:
        return "Neutro"
