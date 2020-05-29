import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from example_data_base import get_historical_data, get_connection, get_query

STRONG_SIMILARITY_DIFFERENCE = 5
SMALL_SIMILARITY_DIFFERENCE = 10


def are_strong_similar_values(value1, value2):
    return abs(value1 - value2) <= STRONG_SIMILARITY_DIFFERENCE


def are_small_similar_values(value1, value2):
    return abs(value1 - value2) <= SMALL_SIMILARITY_DIFFERENCE


def get_all_similar_predictions(car_elements_list):
    historical_data = get_historical_data()
    result = {}
    car_elements_as_string = ["engine", "car_body", "costs", "car_details", "equipment", "driving_features"]
    for historical_row in historical_data:
        strong_similarity = 0
        small_similarity = 0
        for index, element in enumerate(car_elements_list):
            if are_strong_similar_values(element, historical_row[index]):
                strong_similarity += 1
            if are_small_similar_values(element, historical_row[index]):
                small_similarity += 1
        if strong_similarity > 3:
            result.update({historical_row[-2], historical_row[-1]})
        elif small_similarity > 5:
            result.update({historical_row[-2], historical_row[-1]})
    return result


def get_data_frames():
    conn = get_connection()
    sql = get_query(with_timestamp=True)
    data = pd.read_sql(sql, conn)
    conn.close()

    return data


def prepare_user_column(dt):
    dt_to_user = {}

    c = 1
    for d in dt.drop_duplicates():
        dt_to_user[d] = c
        c += 1

    user_column = []

    for e in dt:
        user_column.append(dt_to_user[e])

    return user_column


def get_similar_cars(car, similarity_df, n_neighbors=3):
    similar_ids = similarity_df.loc[car].sort_values(ascending=False)[1:n_neighbors + 1].reset_index()
    return similar_ids


def prepare_matrix(data, column_name):
    return data.pivot_table(index='car', columns='userId', values=column_name, fill_value=0)


def get_cosine_similarity(matrix):
    cosine_similarity_cf_mx = cosine_similarity(matrix)
    return pd.DataFrame(cosine_similarity_cf_mx, columns=matrix.index, index=matrix.index)


def process(data, car_name):
    column_names = ['engine', 'car_body', 'costs', 'car_details', 'equipment', 'driving_features', 'grade']
    results = {}

    for c in column_names:
        mx = prepare_matrix(data, c)
        sim_mx = get_cosine_similarity(mx)
        sim_cars = get_similar_cars(car_name, sim_mx)
        results[c] = sim_cars

    return results


def get_recommendation(predicted_cars):
    data = get_data_frames()
    print(data)
    user_column = prepare_user_column(data['dt'])
    data = data.assign(userId=pd.Series(user_column).values)

    result = {}
    for k, _ in predicted_cars.items():

        if k not in data['car'].drop_duplicates().tolist():
            continue

        processing_result = process(data, k)

        print(processing_result)

        distinct_cars = []
        for _, v in processing_result.items():
            for c in v['car']:
                if c not in distinct_cars:
                    distinct_cars.append(c)

        result[k] = distinct_cars

    return result
