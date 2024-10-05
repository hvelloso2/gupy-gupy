def pertence_fibonacci(numero):

  a, b = 0, 1
  while b <= numero:
    if b == numero:
      return True
    a, b = b, a + b
  return False

print("digite um numero:")
numero = int(input())
if pertence_fibonacci(numero):
  print(f"O numero {numero} pertence a sequencia de fibonacci.")
else:
  print(f"O numero {numero} não pertence a sequencia de fibonacci.")