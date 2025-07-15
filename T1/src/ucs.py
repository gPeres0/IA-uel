import json
import heapq

with open("../data/conexoes.json", encoding="utf-8") as arquivo:
        grafo = json.load(arquivo)

def busca_custo_uniforme(cidade_inicio, cidade_destino):
    """
    Encontra o caminho de menor custo entre cidade_inicio e cidade_destino
    usando Uniform Cost Search.
    Retorna (caminho, custo_total).
    """
    # Inicialização
    distancias = {cidade: float("inf") for cidade in grafo}
    distancias[cidade_inicio] = 0
    anterior = {}
    fila_prioridade = [(0, cidade_inicio)]

    while fila_prioridade:
        custo_atual, cidade_atual = heapq.heappop(fila_prioridade)

        # Encerra quando chega no destino
        if cidade_atual == cidade_destino:
            break

        # Ignora entradas desnecessarias
        if custo_atual > distancias[cidade_atual]:
            continue

        # Expande vizinhos
        for vizinho, peso in grafo[cidade_atual]:
            novo_custo = custo_atual + peso
            if novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                anterior[vizinho] = cidade_atual
                heapq.heappush(fila_prioridade, (novo_custo, vizinho))

    # Reconstroi o caminho
    if cidade_destino not in anterior and cidade_inicio != cidade_destino:
        return "Cidade de origem e/ou destino inválida", float("inf")

    caminho = []
    atual = cidade_destino
    while atual != cidade_inicio:
        caminho.append(atual)
        atual = anterior[atual]
    caminho.append(cidade_inicio)
    caminho.reverse()

    if caminho == None:
        return "Não há caminho entre as cidades", None

    return caminho, distancias[cidade_destino]
