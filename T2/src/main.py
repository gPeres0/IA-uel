import cria_base_conhecimento as cbc
import desenha_grafo as dg
import motor_inferencia as mi

def main():
    G = cbc.criar_base_conhecimento()
    dg.desenhar_grafo(G)
    mi.motor_inferencia(G)
