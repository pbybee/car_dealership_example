#!/usr/bin/python3.6
import psycopg2
import sys, os, traceback


def input_data(filename):
    try:
        #check if file exists and is extension csv
        if not os.path.isfile(filename) and \
                os.path.splitext(filename)[1] is not ".csv":
            print("Please input valid filename of type .csv")

        #get a list of cars and check some basivs
        cars = list()
        with open(filename, 'r') as fp:
            header = fp.readline().strip().split(',')
            if header != ['car_make', 'car_model', 'car_year', 'car_description']:
                print('csv file not formatted correctly')
                print(header)
                raise Exception
            for n,line in enumerate(fp.readlines()):
                vals = line.split(',')
                if len(vals) != 4 and len(vals) > 0:
                    print(f'csv has wrong number of values on line {n+2}')
                    print(vals)
                    raise Exception
                if not vals[2].isdigit():
                    print(f'year is invalid on line {n+2}')
                    print(vals[2])
                    raise Exception
                vals[3] = vals[3].strip()
                vals[2] = int(vals[2])
                print(vals)
                cars.append(vals)

        conn = psycopg2.connect(
            host="localhost",
            database="dealership",
            user="postgres",
            password="adminpass"
        )

        print('Inserting cars into DB')
        cur = conn.cursor()
        for car in cars:
            print(car)
            cmd = f"INSERT INTO cars (car_make, car_model, car_year, car_description) VALUES ('{car[0]}', '{car[1]}', {car[2]}, '{car[3]}');"
            print(cmd)
            cur.execute(cmd)
            conn.commit()
    except:
        traceback.print_exc()
    finally:
        conn.close()


def print_help():
    print("""Input can be as follows:
    -i [FILENAME] : Where FILENAME is a csv filewith car information as formatted
    car_make, car_model, car_year, car_description
    Toyota, Forerunner, 2008, rad SUV
    e.g.
    dealership -i cars.csv
    """)


if __name__ == "__main__":

    try:
        args = sys.argv
        print(args)
        if args[1] == '-i':
            input_data(args[2])
        elif args[1] == '--topsales':
            top_sales()
        else:
            print_help()
    except Exception:
        print_help()


