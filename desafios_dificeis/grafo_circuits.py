import networkx as nx
import matplotlib.pyplot as plt


# Função para detectar ciclos usando o algoritmo de Tarjan (circuits)
def detectar_ciclos(grafo):
    print("\nDetectando ciclos no grafo...")
    ciclos = list(nx.simple_cycles(grafo))
    if ciclos:
        print("Ciclos detectados:")
        for i, ciclo in enumerate(ciclos, start=1):
            print(f"Ciclo {i}: {ciclo}")
    else:
        print("Nenhum ciclo encontrado no grafo.")
    return ciclos


# Função para visualizar o grafo e destacar os ciclos
def visualizar_grafo(grafo, ciclos):
    pos = nx.spring_layout(grafo)
    plt.figure(figsize=(10, 8))

    # Desenhar todos os nós e arestas
    nx.draw(grafo, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

    # Destacar os ciclos
    if ciclos:
        for ciclo in ciclos:
            edges = [(ciclo[i], ciclo[(i + 1) % len(ciclo)]) for i in range(len(ciclo))]
            nx.draw_networkx_edges(grafo, pos, edgelist=edges, edge_color='red', width=2)

    plt.title("Grafo de Comunicação e Ciclos Detectados")
    plt.show()


# Função para salvar o grafo em um arquivo
def salvar_grafo_em_arquivo(grafo, nome_arquivo="grafo_comunicacao.gml"):
    try:
        nx.write_gml(grafo, nome_arquivo)
        print(f"Grafo salvo com sucesso no arquivo: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o grafo: {e}")


# Função para carregar um grafo de um arquivo
def carregar_grafo_de_arquivo(nome_arquivo):
    try:
        grafo = nx.read_gml(nome_arquivo)
        print(f"Grafo carregado com sucesso do arquivo: {nome_arquivo}")
        return grafo
    except Exception as e:
        print(f"Erro ao carregar o grafo: {e}")
        return None


# Exemplo de uso
if __name__ == "__main__":
    # Criando o grafo dirigido
    grafo = nx.DiGraph()

    # Adicionando arestas (simulação de tráfego entre dispositivos)
    grafo.add_edges_from([
        ("Dispositivo A", "Dispositivo B"),
        ("Dispositivo B", "Dispositivo C"),
        ("Dispositivo C", "Dispositivo A"),  # Ciclo
        ("Dispositivo C", "Dispositivo D"),
        ("Dispositivo D", "Servidor E"),
        ("Servidor E", "Dispositivo C"),  # Ciclo
        ("Dispositivo F", "Dispositivo G"),
    ])

    # Detectar ciclos
    ciclos_detectados = detectar_ciclos(grafo)

    # Visualizar o grafo com ciclos destacados
    visualizar_grafo(grafo, ciclos_detectados)

    # Salvar o grafo em um arquivo
    salvar_grafo_em_arquivo(grafo)

    # Carregar o grafo de um arquivo (opcional, para testes)
    grafo_carregado = carregar_grafo_de_arquivo("grafo_comunicacao.gml")
    if grafo_carregado:
        ciclos_detectados_carregado = detectar_ciclos(grafo_carregado)
        visualizar_grafo(grafo_carregado, ciclos_detectados_carregado)