import pandas as pd

years = range(2014,2020)

for year in years: 
    data = pd.read_csv(f"london_accidents_{year}.csv")

    print(f"Information sur le fichier de l'année {year}")
    #Compter le nombre de NA 

    print(f"Nombre de NA: {data.isnull().sum().sum()}")

    #Suppression des données manquantes
    data_net = data.dropna()
    print(f"Nombre de NA après suppression : {data_net.isnull().sum().sum()}")

    #Nombre de lignes totales
    num_rows = data_net.shape[0]
    print(f"Nombre de lignes du fichier : {num_rows}")

    #Nombre de colonnes

    num_col = data_net.shape[1]
    print(f"Nombre de colonnes : {num_col}")

    print(data_net.head())
    
    data_net.to_csv(f"nettoyé/london_accidents_{year}.csv", index=False)

    print(f"✅ Fichier london_accidents_{year}_nettoye.csv sauvegardé avec succès !\n")






