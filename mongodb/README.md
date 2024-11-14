Launch the database
````
docker compose up
````


Client login in the db
````
docker exec -it mongo bash
docker exec -it mongo mongosh -u admin -p admin --authenticationDatabase admin
````



Outros comandos

`````
docker exec -it mongo mongoimport  --db nobel --collection premios --drop --file /data/nobel.json --jsonArray --username admin -p admin --authenticationDatabase admin
````