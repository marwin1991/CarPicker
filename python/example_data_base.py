import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE car_picker
             (engine real, car_body real, costs real, car_details real, equipment real, driving_features real,
             car text, grade real)''')
c.execute("INSERT INTO car_picker VALUES (51,71,61,81,41,31,'Audi A4', 5)")

for row in c.execute('SELECT * FROM car_picker'):
    row = list(row)
    print(row)

conn.commit()


def get_historical_data():
    conn = sqlite3.connect('example.db')

    c = conn.cursor()
    rows = []
    for row in c.execute('SELECT * FROM car_picker'):
        row = list(row)
        rows.append(row)
    return rows
