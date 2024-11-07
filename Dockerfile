# Utiliser une image InfluxDB
FROM influxdb:2.0 AS influxdb

# Utiliser une image Grafana
FROM grafana/grafana:latest

# Configuration de la base de données InfluxDB
# Note : InfluxDB 2.0 nécessite une configuration via un script d'initialisation ou via une configuration manuelle

# Copier les scripts de configuration pour initialiser InfluxDB
COPY --from=influxdb /etc/influxdb2 /etc/influxdb2
COPY --from=influxdb /var/lib/influxdb2 /var/lib/influxdb2

# Exposer les ports pour InfluxDB et Grafana
EXPOSE 8086 3000

# Démarrer Grafana et InfluxDB
CMD ["sh", "-c", "/entrypoint.sh & /usr/bin/influxd & /run.sh"]
