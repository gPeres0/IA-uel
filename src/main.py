import bfs
import dfs
import ucs
import time

if __name__ == '__main__':
    origins = ["Londrina", "Primeiro de Maio", "Londrina", "Londrina", "Primeiro de Maio"]
    destinies = ["Maringá", "Apucarana", "Paranavaí", "Foz do Iguaçu", "Curitiba"]

    i = 1
    while i <= 5:
        bfs_start = time.perf_counter_ns()
        bfs_result = bfs.bfs(origins[i-1], destinies[i-1])
        bfs_end = time.perf_counter_ns()

        dfs_start = time.perf_counter_ns()
        dfs_result = dfs.dfs(origins[i-1], destinies[i-1])
        dfs_end = time.perf_counter_ns()

        ucs_start = time.perf_counter_ns()
        ucs_result, total_cost = ucs.busca_custo_uniforme(origins[i-1], destinies[i-1])
        ucs_end = time.perf_counter_ns()

        print(f"""
                            -
        ================ TESTE {i} ===================
                {origins[i-1]}   -->   {destinies[i-1]} 
        =================== BFS =====================
        {bfs_result}

        Começo do teste: {bfs_start}
        Fim do teste: {bfs_end}
        Tempo total de execução: {(bfs_end - bfs_start)/1000000} ms
        =================== DFS =====================
        {dfs_result}
        
        Começo do teste: {dfs_start}
        Fim do teste: {dfs_end}
        Tempo total de execução: {(dfs_end - dfs_start)/1000000} ms
        =================== UCS =====================
        Custo total: {total_cost}
        {ucs_result}
        
        Começo do teste: {ucs_start}
        Fim do teste: {ucs_end}
        Tempo total de execução: {(ucs_end - ucs_start)/1000000} ms
        =============================================""")
        
        i += 1