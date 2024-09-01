def invert(string):
    palavras_trocadas = [palavra[::-1] for palavra in string.split()]
    inversao = ' '.join(palavras_trocadas)
    return inversao

n = input("Digite uma frase: ")
inversao = invert(n)
print(inversao)