You can get started by pulling the postgres docker image and making a directory
```
docker pull postgres
mkdir ~/postgres-testing
```

Then you can run it
```
docker run -d \
    --name dev-postgres \
    -e POSTGRES_PASSWORD=guest \
    -v ~/postgres-testing:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres
```

and create the databse we'll use
```
docker exec -it dev-postgres psql -h localhost -U postgres -c "CREATE DATABASE dealership;"
```

