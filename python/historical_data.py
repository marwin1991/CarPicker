historical_data = [{"engine" : 50, "car_body":80, "costs":48, "car_details" : 72, "equipment":80, "driving-features": 68, "chosen_models" :{"VW Passat" : 4, "Skoda Superb":3, "VW Tiguan":3}}]


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
            result.append(historical_row.get("chosen_models"))
    return result
