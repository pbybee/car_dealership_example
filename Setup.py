import psycopg2


def create_schema(conn):
    cur = conn.cursor()
    cur.execute("""                
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
        """)

    conn.commit()


def insert_mock_data(conn):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO customers(customer_name, customer_phone) VALUES ('Jon','123');
        INSERT INTO customers(customer_name, customer_phone) VALUES ('Jane','987');
        INSERT INTO cars(car_make, car_model, car_year, car_description) VALUES ('Toyota', 'Tacoma', 2011, 'Its a truck');
        INSERT INTO cars(car_make, car_model, car_year, car_description) VALUES ('Subaru', 'Forester', 2001, 'Super Sports Edition');
        INSERT INTO sales(customer_id, car_id, sale_price, sale_rep) VALUES (1,1,40000.00, 'Juan');
        INSERT INTO sales(customer_id, car_id, sale_price, sale_rep) VALUES (1,2,21000.20, 'Maria');
        """)
    conn.commit()


def delete_db():
    conn = psycopg2.connect(
        host='localhost',
        database='dealership',
        user='postgres',
        password='adminpass'
    )
    conn.cursor().execute("DROP DATABASE dealership;")


if __name__ == "__main__":

    try:
        conn = psycopg2.connect(
            host='localhost',
            database='dealership',
            user='postgres',
            password='adminpass'
        )
        create_schema(conn)
        insert_mock_data(conn)

    finally:
        conn.close()
