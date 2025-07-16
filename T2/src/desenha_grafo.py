import matplotlib.pyplot as plt


def desenhar_grafo(G):
    """Desenha e salva o grafo como uma imagem."""
    plt.figure(figsize=(14, 10))
    pos = nx.spring_layout(G, seed=42, k=0.9)  # Layout para melhor visualização

    # Desenha nós
    nx.draw_networkx_nodes(G, pos, node_size=2500, node_color='skyblue')

    # Desenha rótulos dos nós
    nx.draw_networkx_labels(G, pos, font_size=10)

    # Desenha arestas e seus rótulos
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title("Rede Semântica de Animais")
    plt.savefig("rede_semantica_animais.png")
    print("\n[INFO] Grafo salvo como 'rede_semantica_animais.png'")