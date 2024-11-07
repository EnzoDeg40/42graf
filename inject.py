from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime, timedelta
import random

# Configuration d'InfluxDB
url = "http://localhost:8086"
token = "my-super-secret-token"
org = "myorg"
bucket = "mybucket"

# Initialiser le client InfluxDB
client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Date/heure de début
start_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

# Génération des données
for i in range(20):  # Insère 20 valeurs
    # Générer l'heure actuelle en ajoutant un intervalle de temps
    current_time = start_time + timedelta(minutes=i * 15)
    
    # Créer un point avec les données
    person_count = random.randint(1, 100)
    point = (
        Point("people_count")
        .tag("cluster", "made")
        .field("person_count", person_count)
        .time(current_time, WritePrecision.NS)
    )
    
    # Écrire le point dans InfluxDB
    write_api.write(bucket=bucket, org=org, record=point)
    print(f"Inséré : {current_time}, cluster=made, person_count={person_count}")

# Fermer la connexion
client.close()
