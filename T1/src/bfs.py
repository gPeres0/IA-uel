import json
from collections import deque

with open("../data/conexoes.json", "r", encoding="utf-8") as f:
    conexoes = json.load(f)


def bfs(cidade_origem, cidade_destino):
    if cidade_origem not in conexoes or cidade_destino not in conexoes:
        return None

    fila = deque([cidade_origem])
    visitados = {cidade_origem}
    predecessores = {cidade_origem: None}

    while fila:
        cidade_atual = fila.popleft()

        if cidade_atual == cidade_destino:
            caminho = []
            cidade = cidade_atual
            while cidade is not None:
                caminho.append(cidade)
                cidade = predecessores[cidade]
            caminho.reverse()
            return caminho

        for vizinho_info in conexoes[cidade_atual]:
            vizinho = vizinho_info[0]  # Extrai apenas o nome
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                predecessores[vizinho] = cidade_atual

    return "Nenhum caminho encontrado"


