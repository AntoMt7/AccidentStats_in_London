import requests
import pandas as pd

def fetch_accident_stats(year):
    api_url = f"https://api.tfl.gov.uk/AccidentStats/{year}"
    response= requests.get(api_url)
    if response.status_code==200:
        return response.json()
    else: 
        print(f"Erreur pour l'année {year} : {response.status_code}")
        return None
years= range(2014,2020)
all_data = {}

for year in years : 
    print(f"Récupération des données pour l'année {year}")
    data = fetch_accident_stats(year)
    if data:
        all_data[year]= data
        print(f"Données pour {year} récupérées avec succès")
    else: 
        print(f"Aucune donnée n'a été récupérée pour {year}")

#Exemple de données
for year, data in all_data.items():
    print(f"\nExemple de données pour {year}: ")
    print(data[0])

#Stockage des données pour les différentes années

for year, data in all_data.items():
    df = pd.DataFrame(data)

    filename = f"london_accidents_{year}.csv"
    df.to_csv(filename, index=False)
    print(f"Données pour {year} sauvegardées dans {filename}.")

    
