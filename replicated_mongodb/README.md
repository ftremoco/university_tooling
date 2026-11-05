Launch the database
````
docker compose up
````

In order to create a cluster:

1) Client Login - 1 terminal window for each
docker exec -it mongo1 mongosh
docker exec -it mongo2 mongosh
docker exec -it mongo3 mongosh

2) initiate the replicaset and add the nodes
Within the mongo1 terminal run:
    rs.initiate()
    rs.add('mongo2')
    rs.add('mongo3')

----


Client login in the db (if the authentication method was setup)
````
docker exec -it mongo1 mongosh -u admin -p admin --authenticationDatabase admin
docker exec -it mongo2 mongosh -u admin -p admin --authenticationDatabase admin
docker exec -it mongo3 mongosh -u admin -p admin --authenticationDatabase admin
````
