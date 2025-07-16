
def obter_propriedades_heranca(G, no):
    """Obtém todas as propriedades de um nó, incluindo as herdadas."""
    propriedades = set()
    fila = [no]
    visitados = set()

    while fila:
        atual = fila.pop(0)
        if atual in visitados:
            continue
        visitados.add(atual)

        # 1) coleta propriedades diretas (arestas saindo do nó com labels de propriedade)
        for vizinho, attrs in G[atual].items():
            if attrs['label'] in {"tem", "produz", "bota", "pode", "vive_em"}:
                propriedades.add(vizinho)

        # 2) sobe para o pai através das arestas 'é_um' (saindo do nó)
        for _, pai, attrs in G.out_edges(atual, data=True):
            if attrs['label'] == "é_um":
                fila.append(pai)

    return propriedades


def motor_inferencia(G):
    # 1) identifica corretamente as "folhas" (animais concretos)
    folhas = [
        n for n in G.nodes()
        if any(attrs['label'] == 'é_um' for _, _, attrs in G.out_edges(n, data=True))
        and not any(attrs['label'] == 'é_um' for _, _, attrs in G.in_edges(n, data=True))
        and n != "Animal"
    ]
    candidatos = set(folhas)

    # print("Debug: candidatos iniciais:", sorted(candidatos))

    perguntas = [
        ("Voar",         "O animal pode voar?"),
        ("Vive na Água", "O animal vive na água?"),
        ("Escamas",      "O animal tem escamas?"),
        ("Penas",        "O animal tem penas?"),
        ("Ovos",         "O animal bota ovos?"),
        ("Leite",        "O animal produz leite?"),
        ("Pelos",        "O animal tem pelos?"),
        ("Latir",        "O animal pode latir?")
    ]

    # 2) pré-computa, para cada animal, todas as propriedades herdadas
    propriedades_animais = {
        animal: obter_propriedades_heranca(G, animal)
        for animal in candidatos
    }

    print("\n--- Jogo de Adivinhação de Animais ---")
    print("Responda com 's' ou 'n'.")

    # 3) percorre SEMPRE cada pergunta, até sobrar <=1 candidato
    for prop, texto in perguntas:
        if len(candidatos) <= 1:
            break

        # solicita resposta
        resp = input(f"\n> {texto} ").strip().lower()
        while resp not in ('s', 'n'):
            resp = input("Por favor, responda 's' ou 'n': ").strip().lower()

        # filtra candidatos de acordo com a resposta
        if resp == 's':
            candidatos = {a for a in candidatos if prop in propriedades_animais[a]}
        else:  # 'n'
            candidatos = {a for a in candidatos if prop not in propriedades_animais[a]}

        if not candidatos:
            print("\nNão há animais que satisfaçam todas as respostas dadas.")
            return

        print("Candidatos restantes:", sorted(candidatos))

    # 4) resultado final
    print("\n--- Resultado ---")
    if len(candidatos) == 1:
        print(f"O animal que você pensou é: {next(iter(candidatos))}!")
    else:
        print("Não consegui adivinhar o animal com base nas respostas.")
        print("Possíveis:", sorted(candidatos))
