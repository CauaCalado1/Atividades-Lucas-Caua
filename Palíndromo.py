def remover_acentos(texto):
    acentuadas = 'áàãâäéèêëíìîïóòõôöúùûüçÁÀÃÂÄÉÈÊËÍÌÎÏÓÒÕÔÖÚÙÛÜÇ'
    sem_acentos = 'aaaaaeeeeiiiiooooouuuucAAAAAEEEEIIIIOOOOOUUUUC'
    tabela = str.maketrans(acentuadas, sem_acentos)
    return texto.translate(tabela)

def e_palindromo(texto):

    texto = remover_acentos(texto)


    filtrado = "".join(
        ch.lower()
        for ch in texto
        if ch.isalpha()
    )

    print(f"\n🔍 Texto filtrado para verificação: '{filtrado}'")


    return filtrado == filtrado[::-1]


entrada = input("Digite uma palavra ou frase: ")

if e_palindromo(entrada):
    print(" É um palíndromo!")
else:
    print(" Não é um palíndromo.")