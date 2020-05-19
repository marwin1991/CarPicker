
from example_data_base import get_historical_data

historical_data = [
    {"engine": 50, "car_body": 80, "costs": 48, "car_details": 72, "equipment": 80, "driving_features": 68,
     "chosen_models": {"VW Passat": 4, "Skoda Superb": 3, "VW Tiguan": 3}}]

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
            if are_strong_similar_values(element, historical_row[index]):
                small_similarity += 1
        if strong_similarity > 3:
            result.update({historical_row[-2],historical_row[-1] })
        elif small_similarity > 5:
            result.update({historical_row[-2], historical_row[-1]})
    return result
