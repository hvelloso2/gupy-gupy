def encontrar_proximo(sequencia):
    
    if all(x % 2 != 0 for x in sequencia):
        return sequencia[-1] + 2

    if all(x == sequencia[0] * 2**i for i, x in enumerate(sequencia)):
        return sequencia[-1] * 2
    
    if all(x == i**2 for i, x in enumerate(sequencia)):
        return (len(sequencia))**2
 
    if all(x == (2*i)**2 for i, x in enumerate(sequencia)):
        return (2 * len(sequencia))**2

    if len(sequencia) >= 3 and all(sequencia[i] == sequencia[i-1] + sequencia[i-2] for i in range(2, len(sequencia))):
        return sequencia[-1] + sequencia[-2]

sequencias = [[1, 3, 5, 7],
             [2, 4, 8, 16, 32, 64],
             [0, 1, 4, 9, 16, 25, 36],
             [4, 16, 36, 64],
             [1, 1, 2, 3, 5, 8],
             [2, 10, 12, 16, 17, 18, 19]]

for sequencia in sequencias:
    proximo = encontrar_proximo(sequencia)
    if proximo:
        print(f"O próximo elemento da sequência {sequencia} é: {proximo}")