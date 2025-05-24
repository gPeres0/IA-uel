import json

with open("../data/conexoes.json", "r", encoding="utf-8") as f:
    conexoes = json.load(f)

def dfs(origem, destino):
    if origem not in conexoes or destino not in conexoes:
        return "Cidade de origem ou destino incompatível"

    pilha = [origem]
    visitadas = {origem}
    pai = {origem: None}

    while pilha:
        atual = pilha.pop()
        if atual == destino:
            caminho = []
            node = atual
            while node is not None:
                caminho.append(node)
                node = pai[node]
            return list(reversed(caminho))

        for vizinho in conexoes[atual]:
            nome = vizinho if isinstance(vizinho, str) else vizinho[0]
            if nome not in visitadas:
                visitadas.add(nome)
                pai[nome] = atual
                pilha.append(nome)

    return "Nenhum caminho encontrado"
