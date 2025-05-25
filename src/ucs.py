import json
import heapq
import time


def busca_custo_uniforme(grafo, cidade_inicio, cidade_destino):
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
        return None, float("inf")

    caminho = []
    atual = cidade_destino
    while atual != cidade_inicio:
        caminho.append(atual)
        atual = anterior[atual]
    caminho.append(cidade_inicio)
    caminho.reverse()

    return caminho, distancias[cidade_destino]


if __name__ == "__main__":
    # Carrega o grafo
    with open("../data/conexoes.json", encoding="utf-8") as arquivo:
        grafo = json.load(arquivo)

    # Lista de testes (origem, destino)
    testes = [
        ("Londrina", "Maringá"),
        ("Primeiro de Maio", "Apucarana"),
        ("Londrina", "Paranavaí"),
        ("Londrina", "Foz do Iguaçu"),
        ("Primeiro de Maio", "Curitiba"),
    ]

    # Executa cada teste
    for cidade_inicio, cidade_destino in testes:
        print(f"\nTeste: {[cidade_inicio, cidade_destino]}")
        tempo_inicio = time.perf_counter()
        caminho, custo_total = busca_custo_uniforme(
            grafo, cidade_inicio, cidade_destino
        )
        tempo_fim = time.perf_counter()
        tempo_total_ms = (tempo_fim - tempo_inicio) * 1000

        if caminho is None:
            print(f"Não há caminho de {cidade_inicio} até {cidade_destino}.")
        else:
            rota = " -> ".join(caminho)
            print(f"Caminho mínimo: {rota}")
            print(f"Custo total: {custo_total}")
        print(f"Tempo de execução: {tempo_total_ms:.6f} ms")
