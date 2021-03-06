import pandas as pd
from example_data_base import get_historical_data, get_connection, get_query
from sklearn.metrics.pairwise import cosine_similarity

STRONG_SIMILARITY_DIFFERENCE = 5
SMALL_SIMILARITY_DIFFERENCE = 10
FEATURES_AMOUNT = 6

# (strong similar features count, small similar features count)
records_similarities = [(6, 0), (5, 1), (5, 0), (4, 2), (4, 1), (4, 0), (3, 3), (3, 2), (3, 1), (2, 4), (2, 3), (2, 2),
                        (1, 5), (1, 4), (1, 3), (0, 6), (0, 5), (0, 4)]
# (strong similar features count, small similar features count, similarity wage)
records_similarities_with_wages = []

STRONG_SIM_MULTIPLIER = 3
MEDIUM_SIM_MULTIPLIER = 2
SMALL_SIM_MULTIPLIER = 1

# grade: prediction_modifier
grade_modifiers = {5: 0.5, 4: 0.25, 3: 0.0, 2: -0.25, 1: -0.5}


def are_strong_similar_values(value1, value2):
    return abs(value1 - value2) <= STRONG_SIMILARITY_DIFFERENCE


def are_small_similar_values(value1, value2):
    return abs(value1 - value2) <= SMALL_SIMILARITY_DIFFERENCE


def prepare_record_similarities():
    s = len(records_similarities)
    for index, e in enumerate(records_similarities):
        w = 1.0 - index / s
        records_similarities_with_wages.append((e[0], e[1], w))


def prepare_record(car_name, grade, strong_s_count, small_s_count):
    index = records_similarities.index((strong_s_count, small_s_count))
    return car_name, grade, records_similarities_with_wages[index][2]


def get_all_similar_records(predicted_features):
    historical_data = get_historical_data()
    prepare_record_similarities()
    result = []
    for historical_row in historical_data:
        strong_similarity = 0
        small_similarity = 0
        for index, element in enumerate(predicted_features):
            if are_strong_similar_values(element, historical_row[index]):
                strong_similarity += 1
            elif are_small_similar_values(element, historical_row[index]):
                small_similarity += 1
        if strong_similarity + small_similarity >= 4:
            result.append(prepare_record(historical_row[-2], historical_row[-1], strong_similarity, small_similarity))

    return result, len(historical_data)


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


def get_best_match(data, car):
    processing_result = process(data, car)

    best_cars = {}
    for _, v in processing_result.items():
        cars = v['car'].to_list()
        values = v[car].to_list()
        for index, car_name in enumerate(cars):
            tmp = 0
            if car_name in best_cars:
                tmp = best_cars[car_name]
            tmp += values[index]
            best_cars[car_name] = tmp

    result = sorted(best_cars.items(), key=lambda item: item[1], reverse=True)[:3]
    return result


def calculate_grade_with_mul(grade, wage):
    multiplier = SMALL_SIM_MULTIPLIER

    if wage > 0.67:
        multiplier = STRONG_SIM_MULTIPLIER
    elif wage > 0.34:
        multiplier = MEDIUM_SIM_MULTIPLIER

    base_grade = grade_modifiers[grade]
    return multiplier * base_grade


def calculate_grades(similar_records):
    result = {}
    for r in similar_records:
        car_name, grade, wage = r
        current_sum = 0

        if car_name in result:
            current_sum = result[car_name]

        current_sum += calculate_grade_with_mul(grade, wage)

        result[car_name] = current_sum

    return result


def get_recommendation(predicted_cars, predicted_features):
    similar_records, history_size = get_all_similar_records(predicted_features)
    print("pred_car:", predicted_cars)
    print("pred_feat:", predicted_features)
    modifiers_per_car = calculate_grades(similar_records)

    # recommendation_modifiers = calculate_car_modifiers(modifiers_per_car)
    recommendation_modifiers = modifiers_per_car
    print(recommendation_modifiers)

    result = {}

    if len(recommendation_modifiers) == 0:
        return predicted_cars

    history_size_param = history_size / 100
    history_size_param = history_size_param if history_size_param <= 0.7 else 0.7

    for k, v in recommendation_modifiers.items():
        if k in predicted_cars.keys():
            s = predicted_cars[k] + v * history_size_param
            result[k] = s if s > 0.0 else 0.0
        elif v > 0:
            result[k] = v

    for k, v in predicted_cars.items():
        if k not in result.keys():
            result[k] = v

    print("after_recommendation:", result)
    return result

    # data = get_data_frames()
    # user_column = prepare_user_column(data['dt'])
    # data = data.assign(userId=pd.Series(user_column).values)
    #
    # result = {}
    # car_names = predicted_cars.keys()
    # for c in car_names:
    #
    #     if c not in data['car'].drop_duplicates().tolist():
    #         continue
    #
    #     distinct_cars = [a for (a, b) in get_best_match(data, c)]
    #
    #     filtered_cars = []
    #     for e in distinct_cars:
    #         if e not in car_names:
    #             filtered_cars.append(e)
    #
    #     result[c] = filtered_cars
    #
    # return result
