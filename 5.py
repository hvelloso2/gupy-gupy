def descobrir_interruptor():
  

  print("Primeira visita: Ligue o primeiro interruptor e espere.")
  print("Segunda visita:")

  estado_lampada = input("Digite o estado da lâmpada (A, B ou C): ")

  if estado_lampada == 'A':
    print("O primeiro interruptor controla a lâmpada.")
  elif estado_lampada == 'B':
    print("O segundo interruptor controla a lâmpada.")
  else:
    print("O terceiro interruptor controla a lâmpada.")


descobrir_interruptor()