import matplotlib.pyplot as plt

# Dados fornecidos
problemas = [
    "Azulejo prestes a cair (infiltração)",
    "Água contaminada",
    "Risco de desabamento do teto",
    "Área da parada de ônibus (insegurança)",
    "Falta de ambulatório na universidade"
]
grau_risco = [4, 4, 5, 3, 2]
custo_medio = [6500, 12500, 60000, 30000, 125000]
pontuacao = [26_000, 50_000, 300_000, 90_000, 500_000]

# Criar o gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(custo_medio, grau_risco, s=pontuacao, c=pontuacao, cmap='viridis', alpha=0.7)

# Adicionar título e rótulos
plt.title('Prioridade de Resolução dos Problemas: Custo vs. Risco')
plt.xlabel('Custo Médio (R$)')
plt.ylabel('Grau de Risco (Escala 1-5)')

# Adicionar rótulos aos pontos
for i, problema in enumerate(problemas):
    plt.text(custo_medio[i] + 1000, grau_risco[i], problema, fontsize=9)

# Adicionar barra de cores para indicar a pontuação
plt.colorbar(label='Pontuação (Risco x Custo Médio)')

# Exibir o gráfico
plt.grid(True)
plt.tight_layout()
plt.show()