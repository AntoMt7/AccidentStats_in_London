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

for year in years:
    print(f"Récupération des données pour l'année {year}")
    
    data = fetch_accident_stats(year)
    
    if data:
        # Extraire les champs souhaités pour chaque accident
        extracted_data = []
        for accident in data:
            casualties = accident.get("casualties", [])
            vehicles = accident.get("vehicles", [])

            # Récupérer la première victime si elle existe
            first_casualty = casualties[0] if casualties else {}

            # Récupérer le premier véhicule si il existe
            first_vehicle = vehicles[0] if vehicles else {}

            extracted_data.append({
                "id": accident.get("id"),
                "lat": accident.get("lat"),
                "lon": accident.get("lon"),
                "location": accident.get("location"),
                "date": accident.get("date"),
                "severity": accident.get("severity"),
                "borough": accident.get("borough"),
                "casualty_age": first_casualty.get("age"),
                "casualty_class": first_casualty.get("class"),
                "casualty_severity": first_casualty.get("severity"),
                "casualty_mode": first_casualty.get("mode"),
                "casualty_ageBand": first_casualty.get("ageBand"),
                "vehicle_type": first_vehicle.get("type")
            })
        
        # Ajouter les données extraites à la structure globale
        all_data[year] = extracted_data
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


