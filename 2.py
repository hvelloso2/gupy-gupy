def contar(frase):

  return frase.lower().count('a')

texto = input("Digite uma frase: ")
resultado = contar(texto)

print(f"A letra 'a' aparece {resultado} vezes na frase.")