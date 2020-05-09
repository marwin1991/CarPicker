historical_data = [{"engine" : 50, "car_body":80, "costs":48, "car_details" : 72, "equipment":80, "driving_features": 68, "chosen_models" :{"VW Passat" : 4, "Skoda Superb":3, "VW Tiguan":3}}]


def are_similar_values(value1, value2):
    return abs(value1 - value2) <= 5


def get_all_similar_predictions(car_elements_list):
    result = {}
    car_elements_as_string = ["engine", "car_body", "costs", "car_details", "equipment", "driving_features"]
    for historical_row in historical_data:
        similarity = 0
        for index, element in enumerate(car_elements_list):
            if are_similar_values(element, historical_row.get(car_elements_as_string[index])):
                similarity += 1
        if similarity > 3:
            result.update(historical_row.get("chosen_models"))
    return result
