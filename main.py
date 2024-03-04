def knapsack(peso_max, pesos, valores, n, K):

    """
    Função para resolver o problema da mochila usando programação dinâmica.

    Argumentos:
        peso_max: Capacidade máxima da mochila.
        pesos: Lista com os pesos dos itens.
        valores: Lista com os valores (pontos de sobrevivência) dos itens.
        n: Número de itens.
        K: Matriz para armazenar os resultados intermediários.

    Retorna:
        O valor máximo de pontos de sobrevivência que podem ser alcançados sem exceder o limite de peso da mochila.
    """

    # Construindo a tabela K[][] de baixo para cima
    for i in range(n + 1):
        for j in range(peso_max + 1):
            if i == 0 or j == 0:
                K[i][j] = 0
            elif pesos[i - 1] <= j:
                K[i][j] = max(K[i - 1][j], valores[i - 1] + K[i - 1][j - pesos[i - 1]])
            else:
                K[i][j] = K[i - 1][j]

    # Retornando o valor máximo na última célula da matriz K[][]
    return K[n][peso_max]

# Exemplo de uso
itens = [
    {"peso": 15, "valor": 15},
    {"peso": 3, "valor": 7},
    {"peso": 2, "valor": 10},
    {"peso": 5, "valor": 5},
    {"peso": 9, "valor": 8},
    {"peso": 20, "valor": 17},
]

peso_max = 30
n = len(itens)

# Extraindo os pesos e valores dos itens
pesos = [item["peso"] for item in itens]
valores = [item["valor"] for item in itens]

# Criando a matriz K[][]
K = [[0 for x in range(peso_max + 1)] for x in range(n + 1)]

# Resolvendo o problema da mochila
valor_maximo = knapsack(peso_max, pesos, valores, n, K)

print(f"Valor máximo de pontos de sobrevivência: {valor_maximo}")

# Rastreando a solução ótima
i = n
j = peso_max
solucao = []

while i > 0 and j > 0:
    # Verificando K[i][j] ao invés de K[i - 1][j]
    if K[i][j] != K[i - 1][j]:
        solucao.append(i - 1)
        j -= pesos[i - 1]
    i -= 1

# Imprimindo a lista de itens na solução ótima
print("Itens na solução ótima:")
for i in solucao:
    print(f" - {itens[i]}")

# Imprimindo o peso total da mochila na solução ótima
peso_total = sum(pesos[i] for i in solucao)
print(f"Peso total da mochila: {peso_total} kg")
