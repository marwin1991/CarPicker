historical_data = []


def is_similar(value1, value2):
    return abs(value1 - value2) <= 5


def get_all_similar_prediction(car_elements):
    result = []
    car_elements_as_string = ["engine", "car_body", "costs", "car_details", "equipment", "driving_feature"]
    for historical_row in historical_data:
        similarity = 0
        for element, index in enumerate(car_elements):
            if is_similar(element, historical_row.get(car_elements_as_string[index])):
                similarity += 1
        if similarity > 3:
            result.append(historical_row.get("chosen_model"))
    return result
