You can get started by pulling the postgres docker image and making a directory
```
docker-comose build
docker-compose up
```

you'll need to add data into the database by logging into the container
```
docker exec -it postgres bash
psql -h localhost -U postgres
\c postgres
CREATE TABLE IF NOT EXISTS customers (
  customer_id SERIAL PRIMARY KEY,
  customer_name TEXT NOT NULL,
  customer_phone TEXT NOT NULL
);
  
CREATE TABLE IF NOT EXISTS cars (
  car_id SERIAL PRIMARY KEY,
  car_make TEXT NOT NULL,
  car_model TEXT NOT NULL,
  car_year INTEGER NOT NULL,
  car_description TEXT
);
  
CREATE TABLE IF NOT EXISTS sales (
  sale_id SERIAL PRIMARY KEY,
  customer_id INTEGER REFERENCES customers,
  car_id INTEGER REFERENCES cars,
  sale_price NUMERIC(10,2),
  sale_rep TEXT
  );
  
CREATE TABLE IF NOT EXISTS top_sales (
  id SERIAL PRIMARY KEY,
  sale_rep TEXT,
  total_sales NUMERIC(10,2)
  );
INSERT INTO customers(customer_name, customer_phone) VALUES ('Jon','123');
INSERT INTO customers(customer_name, customer_phone) VALUES ('Jane','987');
INSERT INTO cars(car_make, car_model, car_year, car_description) VALUES ('Toyota', 'Tacoma', 2011, 'Its a truck');
INSERT INTO cars(car_make, car_model, car_year, car_description) VALUES ('Subaru', 'Forester', 2001, 'Super Sports Edition');
INSERT INTO sales(customer_id, car_id, sale_price, sale_rep) VALUES (1,1,40000.00, 'Juan');
INSERT INTO sales(customer_id, car_id, sale_price, sale_rep) VALUES (1,2,21000.20, 'Maria');

```

It's a little scrambled since I made the DB then worked on the django app

The file topsales/views.py contains the code to tabulate the top sellers and display a webpage with the table.html

The dealership file support command line argument with the -i flag and a csv file (e.g. cars.csv) which will upload the csv data into the database
