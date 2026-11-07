# MongoDB setup

This project runs MongoDB in Docker and exposes it on port `27017`.

## 1. Install Docker

Install and start Docker Desktop for your operating system:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

Wait until Docker Desktop reports that the Docker engine is running.

## 2. Start MongoDB

Open a terminal in this `mongodb` directory and start the service:

```sh
docker compose up -d
```

Check that the container is running:

```sh
docker compose ps
```

To follow its startup logs:

```sh
docker compose logs -f mongo
```

The database files are stored in the `db_data` directory. To stop MongoDB
without deleting the database, run:

```sh
docker compose down
```

## 3. Connect with MongoDB Compass

Install [MongoDB Compass](https://www.mongodb.com/products/tools/compass), open
it, and create a new connection using this connection string:

```text
mongodb://admin:admin@localhost:27017/?authSource=admin
```

Alternatively, enter these settings in Compass:

| Setting | Value |
| --- | --- |
| Hostname | `localhost` |
| Port | `27017` |
| Authentication | Username / Password |
| Username | `admin` |
| Password | `admin` |
| Authentication database | `admin` |

Select **Save & Connect** (or **Connect**). The MongoDB service must be running
before Compass can connect.

> These credentials are for local development only. MongoDB applies the
> `MONGO_INITDB_ROOT_USERNAME` and `MONGO_INITDB_ROOT_PASSWORD` settings when
> initializing an empty data directory. Changing them later does not change
> credentials in an already-initialized database.

## Shell access and data import

Open a shell in the running container:

```sh
docker exec -it mongo mongosh -u admin -p admin --authenticationDatabase admin
```

To import `nobel.json` when it is available under `db_data`:

```sh
docker exec -it mongo mongoimport \
  --username admin \
  --password admin \
  --authenticationDatabase admin \
  --db nobel \
  --collection premios \
  --drop \
  --file /data/nobel.json \
  --jsonArray
```
