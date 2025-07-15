import networkx as nx
import matplotlib.pyplot as plt


def criar_base_conhecimento():
    """Cria e retorna a rede semântica (grafo) dos animais."""
    G = nx.DiGraph()  # Grafo Direcionado

    # Nós principais (categorias e animais)
    nodes = [
        "Animal", "Mamífero", "Pássaro", "Peixe",
        "Cachorro", "Gato", "Baleia", "Canário", "Pinguim", "Tubarão"
    ]
    G.add_nodes_from(nodes)

    # Nós de propriedades e ações
    prop_nodes = [
        "Pelos", "Leite", "Penas", "Ovos", "Asas",
        "Voar", "Nadar", "Escamas", "Vive na Água"
    ]
    G.add_nodes_from(prop_nodes)

    # Arestas de Relações (é_um, tem, pode, vive_em)
    # Relações de herança (é_um)
    G.add_edge("Mamífero", "Animal", label="é_um")
    G.add_edge("Pássaro", "Animal", label="é_um")
    G.add_edge("Peixe", "Animal", label="é_um")

    G.add_edge("Cachorro", "Mamífero", label="é_um")
    G.add_edge("Gato", "Mamífero", label="é_um")
    G.add_edge("Baleia", "Mamífero", label="é_um")  # Exemplo interessante
    G.add_edge("Canário", "Pássaro", label="é_um")
    G.add_edge("Pinguim", "Pássaro", label="é_um")  # Exceção interessante
    G.add_edge("Tubarão", "Peixe", label="é_um")

    # Relações de propriedades (tem)
    G.add_edge("Mamífero", "Pelos", label="tem")
    G.add_edge("Mamífero", "Leite", label="produz")
    G.add_edge("Pássaro", "Penas", label="tem")
    G.add_edge("Pássaro", "Ovos", label="bota")
    G.add_edge("Pássaro", "Asas", label="tem")
    G.add_edge("Peixe", "Escamas", label="tem")

    # Relações de capacidade (pode)
    G.add_edge("Canário", "Voar", label="pode")
    G.add_edge("Pinguim", "Nadar", label="pode")
    G.add_edge("Baleia", "Nadar", label="pode")
    G.add_edge("Tubarão", "Nadar", label="pode")

    # Relações de habitat
    G.add_edge("Peixe", "Vive na Água", label="vive_em")
    G.add_edge("Baleia", "Vive na Água", label="vive_em")

    return G


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


def obter_propriedades_heranca(G, no):
    """Obtém todas as propriedades de um nó, incluindo as herdadas."""
    propriedades = set()
    # Fila para busca em largura (ou profundidade) para cima na hierarquia
    fila = [no]
    visitados = set()

    while fila:
        no_atual = fila.pop(0)
        if no_atual not in visitados:
            visitados.add(no_atual)
            # Adiciona propriedades diretas do nó atual
            for vizinho, attrs in G[no_atual].items():
                if attrs['label'] in ["tem", "pode", "bota", "produz", "vive_em"]:
                    propriedades.add(vizinho)
            # Adiciona pais à fila para herdar suas propriedades
            for predecessor, attrs in G.in_edges(no_atual, data=True):
                if attrs['label'] == 'é_um':
                    fila.append(predecessor)
    return propriedades


def motor_inferencia(G):
    """Conduz o jogo de adivinhação com o usuário."""
    animais = [n for n, attr in G.nodes(data=True)
               if G.in_degree(n) > 0 and G.out_degree(n) > 0
               and not any(G[n][v]['label'] == 'é_um' for v in G[n])]
    animais.extend(["Baleia", "Pinguim", "Tubarão"])  # Adiciona folhas
    candidatos = set(animais)

    # Perguntas mapeadas a partir das propriedades
    perguntas = {
        "Voar": "O animal pode voar?",
        "Vive na Água": "O animal vive na água?",
        "Penas": "O animal tem penas?",
        "Pelos": "O animal tem pelos?",
        "Leite": "O animal produz leite?",
        "Ovos": "O animal bota ovos?",
        "Escamas": "O animal tem escamas?",
    }

    print("--- Jogo de Adivinhação de Animais ---")
    print("Responda com 's' para sim ou 'n' para não.")

    # Dicionário para guardar as propriedades de cada animal (cache)
    propriedades_animais = {animal: obter_propriedades_heranca(G, animal) for animal in animais}

    for prop, pergunta in perguntas.items():
        if len(candidatos) <= 1:
            break

        resposta = input(f"\n> {pergunta} ").lower()
        while resposta not in ['s', 'n']:
            resposta = input("Por favor, responda 's' ou 'n': ").lower()

        if resposta == 's':
            # Mantém apenas os candidatos que TÊM a propriedade
            candidatos.intersection_update({animal for animal in candidatos if prop in propriedades_animais[animal]})
        else:  # resposta == 'n'
            # Remove os candidatos que TÊM a propriedade
            candidatos.difference_update({animal for animal in candidatos if prop in propriedades_animais[animal]})

        print(f"Candidatos restantes: {list(candidatos)}")

    print("\n--- Resultado ---")
    if len(candidatos) == 1:
        print(f"O animal que você pensou é: {list(candidatos)[0]}!")
    else:
        print("Não consegui adivinhar o animal com base nas respostas.")
        print(f"Animais possíveis restantes: {list(candidatos)}")


if __name__ == "__main__":
    base_de_conhecimento = criar_base_conhecimento()

    # Passo 1: Gerar a imagem do grafo para o seminário
    desenhar_grafo(base_de_conhecimento)

    # Passo 2: Iniciar o sistema de perguntas e respostas
    motor_inferencia(base_de_conhecimento)