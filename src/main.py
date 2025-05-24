import dfs
from time import perf_counter

if __name__ == '__main__':
    origins = ["Londrina", "Primeiro de Maio", "Londrina", "Londrina", "Primeiro de Maio"]
    destinies = ["Maringá", "Apucarana", "Paranavaí", "Foz do Iguaçu", "Curitiba"]

    i = 1
    while i <= 5:
        bfs_start = perf_counter()
        bfs_result = None
        bfs_end = perf_counter()

        dfs_start = perf_counter()
        dfs_result = dfs.dfs(origins[i-1], destinies[i-1])
        dfs_end = perf_counter()

        ucs_start = perf_counter()
        ucs_result = None
        ucs_end = perf_counter()

        print(f"""
                            -
        ================ TESTE {i} ===================
                {origins[i-1]}   -->   {destinies[i-1]} 
        =================== BFS =====================
        {bfs_result}

        Começo do teste: {bfs_start}
        Fim do teste: {bfs_end}
        Tempo total de execução: {bfs_end - bfs_start}
        =================== DFS =====================
        {dfs_result}
        
        Começo do teste: {dfs_start}
        Fim do teste: {dfs_end}
        Tempo total de execução: {dfs_end - dfs_start}
        =================== UCS =====================
        {ucs_result}
        
        Começo do teste: {ucs_start}
        Fim do teste: {ucs_end}
        Tempo total de execução: {ucs_end - ucs_start}
        =============================================""")
        
        i += 1