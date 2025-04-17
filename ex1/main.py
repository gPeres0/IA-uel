import pandas as pd

def main():
    worldcities = pd.read_csv("./worldcities.csv")
    df = pd.DataFrame(data=worldcities, columns=["city","city_ascii","lat","lng","country","iso2","iso3","admin_name","capital","population","id"])
    mask_pr = df.admin_name == 'Paraná'    
    print(df[mask_pr])
    


main()