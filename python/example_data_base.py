import sqlite3

def get_historical_data():
    conn = sqlite3.connect('car_rates.db')

    c = conn.cursor()
    rows = []
    for row in c.execute('SELECT engine, car_body, costs, car_details, equipment, driving_features, car, grade  FROM car_rates'):
        row = list(row)
        rows.append(row)
    return rows
