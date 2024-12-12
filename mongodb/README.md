Launch the database
````
docker compose up
````


Client login in the db
````
docker exec -it mongo bash
docker exec -it mongo mongosh 
````



Outros comandos

`````
docker exec -it mongo mongoimport  --db nobel --collection premios --drop --file /data/nobel.json --jsonArray
````