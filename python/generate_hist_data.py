import numpy as np
import warnings
from time import sleep
from main import get_prediction
from example_data_base import save_historical_data, get_historical_data

prediction_rates = {}


def get_random_array(n):
    return np.random.randint(0, 10, n).tolist()


def convert_to_db_format(predictions):
    cars = predictions.get('cars')
    features = predictions.get('features')

    hist_array = []
    for c in cars:
        car_rate = c['rate']

        if car_rate in prediction_rates:
            prediction_rates[car_rate] += 1
        else:
            prediction_rates[car_rate] = 1

        car_record = []
        car_record.extend(features)
        car_record.append(c['name'])
        car_record.append(get_rate(c['doubleRate']))
        hist_array.append(car_record)

    return hist_array


def get_rate(predict_rate):
    if predict_rate > 0.3:
        return 5.0
    elif predict_rate > 0.25:
        return 4.0
    elif predict_rate > 0.17:
        return 3.0
    elif predict_rate > 0.1:
        return 2.0
    else:
        return 1.0


def generate_data(n):
    for i in range(n):
        engine = get_random_array(5)
        car_body = get_random_array(4)
        costs = get_random_array(3)
        car_details = get_random_array(3)
        equipment = get_random_array(3)
        driving_features = get_random_array(4)
        arguments = {"engine": engine,
                     "car_body": car_body,
                     "costs": costs,
                     "car_details": car_details,
                     "equipment": equipment,
                     "driving_features": driving_features}
        predictions = get_prediction(arguments)
        db_records = convert_to_db_format(predictions)
        save_historical_data(db_records, python_call=True)
        print("Finished for [%d/%d]" % (i + 1, n))
        sleep(1)


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    generate_data(150)
    history = get_historical_data(python_call=True)
    print(len(history))

    for p in prediction_rates:
        print(p, prediction_rates[p])
