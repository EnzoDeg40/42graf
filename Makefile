compose:
	docker compose up -d --build

re:
	docker compose down
	-docker volume prune -f
	-docker volume rm 42graf_influxdb-data
	docker compose up -d --build