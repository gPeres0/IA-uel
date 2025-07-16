import networkx as nx


def criar_base_conhecimento():
    G = nx.DiGraph()
    # Nós principais
    nodes = [
        "Animal", "Mamífero", "Pássaro", "Peixe",
        "Cachorro", "Gato", "Baleia", "Canário", "Pinguim", "Tubarão"
    ]
    G.add_nodes_from(nodes)
    # Propriedades
    prop_nodes = [
        "Pelos", "Leite", "Penas", "Ovos", "Asas",
        "Voar", "Nadar", "Escamas", "Vive na Água", "Latir"
    ]
    G.add_nodes_from(prop_nodes)

    # Relações é_um
    rel = [("Mamífero","Animal"),("Pássaro","Animal"),("Peixe","Animal"),
           ("Cachorro","Mamífero"),("Gato","Mamífero"),("Baleia","Mamífero"),
           ("Canário","Pássaro"),("Pinguim","Pássaro"),("Tubarão","Peixe")]
    for u,v in rel:
        G.add_edge(u, v, label="é_um")

    # Relações de propriedades e etc.
    props = [
        ("Mamífero","Pelos","tem"),
        ("Mamífero","Leite","produz"),
        ("Pássaro","Penas","tem"),
        ("Pássaro","Ovos","bota"),
        ("Pássaro","Asas","tem"),
        ("Peixe","Escamas","tem"),
        ("Canário","Voar","pode"),
        ("Pinguim","Nadar","pode"),
        ("Baleia","Nadar","pode"),
        ("Tubarão","Nadar","pode"),
        ("Cachorro", "Latir", "pode"),
        ("Peixe","Vive na Água","vive_em"),
        ("Baleia","Vive na Água","vive_em"),
    ]
    for u,v,lab in props:
        G.add_edge(u, v, label=lab)

    return G