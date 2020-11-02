import psycopg2
import sys, os


def main(args):
    filename = args[0]
    #check if file exists and is extension csv
    if not os.path.isfile(filename) and \
            os.path.splitext(filename)[1] is not ".csv":
        print("Please input valid filename of type .csv")

    conn = psycopg2.connect(
        host="localhost",
        database="dealership",
        user="postgres",
        password="adminpass"
    )

    cur = conn.cursor()
    cur.execute("""
    select cst.customer_id, cst.customer_name, cars.car_make, cars.car_model, sales.sale_price 
    from sales
    join customers as cst on cst.customer_id=sales.customer_id
    join cars on cars.car_id = sales.car_id
    where customer_name='TOM'
    """)

    print(cur.fetchall())


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
