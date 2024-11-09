Launch the database
````
docker compose up
````


Client login in the db
````
docker exec -it mongo1 mongosh -u admin -p admin --authenticationDatabase admin
docker exec -it mongo2 mongosh -u admin -p admin --authenticationDatabase admin
docker exec -it mongo3 mongosh -u admin -p admin --authenticationDatabase admin
````
