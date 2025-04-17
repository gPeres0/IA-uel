import pandas as pd
from haversine import haversine


worldcities = pd.read_csv("./worldcities.csv")
df = pd.DataFrame(data=worldcities, columns=["city","city_ascii","lat","lng","country","iso2","iso3","admin_name","capital","population","id"])
mask_pr = df.admin_name == 'Paraná' # Cria uma máscara (boolean) dos valores q se aplicam à condição 

def main():
    pr_cities = df[mask_pr] # Usa a máscara para exibir os valores correspondentes
    #print(pr_cities)
    # Cria tuple com as coordenadas de teste (curitiba e londrina)
    curitiba = (pr_cities.at[453, "lat"], pr_cities.at[453, "lng"])
    londrina = (pr_cities.at[1328, "lat"], pr_cities.at[1328, "lng"])

    # Imprime o resultado do cálculo de Haversine entre os tuples de teste criados
    print(haversine(curitiba, londrina))

    


main()