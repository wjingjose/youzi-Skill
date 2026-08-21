def calculate_score(uzi_score, technical_score, quant_score):
    return round(
        uzi_score * 0.5 +
        technical_score * 0.3 +
        quant_score * 0.2,
        2
    )
