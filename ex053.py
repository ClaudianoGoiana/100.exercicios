frase = str(input("Digite uma frase: ")).strip().upper()  # o usuario digita uma frase, ela é convertida para string, os espaços em branco são removidos e as letras são convertidas para maiusculas
palindromo = frase.replace(" ", "")  # a variavel palindromo recebe a frase sem os espaços em branco
if palindromo == palindromo[::-1]:  # verifica se a variavel palindromo é igual a ela mesma invertida, ou seja, se a frase é um palindromo
    print("A frase é um palíndromo.")
else:  # se a frase não for um palindromo, ou seja, se a variavel palindromo for diferente da ela mesma invertida
    print("A frase não é um palíndromo.")