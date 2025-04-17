import csv
import pandas as pd

def main():
    with open('worldcities.csv') as csvfile:
        worldcities = csv.reader(csvfile, delimiter=',')
    
    df = pd.DataFrame(data=worldcities, index=["city","city_ascii","lat","lng","country","iso2","iso3","capital","admin_name","population","id"])
    for cidades in df:
        if cidades["capital"] == "Paraná":
            print(cidades)

main()