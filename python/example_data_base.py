import sqlite3


def get_query(with_timestamp=False):
    if with_timestamp:
        return 'SELECT dt, engine, car_body, costs, car_details, equipment, driving_features, car, grade  FROM car_rates'
    else:
        return 'SELECT engine, car_body, costs, car_details, equipment, driving_features, car, grade  FROM car_rates'


def get_connection(direct_from_python_call=False):
    if direct_from_python_call:
        return sqlite3.connect('../car_rates.db')
    else:
        return sqlite3.connect('car_rates.db')


def get_historical_data(python_call=False):
    conn = get_connection(python_call)
    c = conn.cursor()
    rows = []
    query = get_query()
    for row in c.execute(query):
        row = list(row)
        rows.append(row)

    conn.close()

    return rows


def save_historical_data(data, python_call=False):
    conn = get_connection(python_call)
    c = conn.cursor()

    for d in data:
        d_tuple = (float(d[0]), float(d[1]), float(d[2]), float(d[3]), float(d[4]), float(d[5]), d[6], d[7])
        c.execute('INSERT INTO car_rates VALUES (current_timestamp,?,?,?,?,?,?,?,?)', d_tuple)

    conn.commit()
    conn.close()
