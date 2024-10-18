Launch the database
````
docker compose up
````


Client login in the db
````
docker exec -it mongo mongosh -u admin -p admin --authenticationDatabase admin
````
