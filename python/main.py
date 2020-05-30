import argparse

from generator import generate_engine, generate_car_body, generate_costs, generate_car_details, \
    generate_equipment, generate_driving_features, get_cars
from historical_data import get_recommendation
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

MAIN_CAR_FEATURES_AMOUNT = 6
TRAINING_SET_SIZE = 100


def generate_training_datasets():
    engine = generate_engine(TRAINING_SET_SIZE, 5)
    car_body = generate_car_body(TRAINING_SET_SIZE, 4)
    costs = generate_costs(TRAINING_SET_SIZE, 3)
    car_details = generate_car_details(TRAINING_SET_SIZE, 3)
    equipment = generate_equipment(TRAINING_SET_SIZE, 3)
    driving_features = generate_driving_features(TRAINING_SET_SIZE, 4)
    cars = get_cars()
    return engine, car_body, costs, car_details, equipment, driving_features, cars


def predict(arguments, training_data):
    X_train = []
    y_train = []
    for data in training_data:
        X_train.append(data[:-1])
        y_train.append(data[-1])
    model = KNeighborsClassifier(5)
    # print(X_train)
    # print(y_train)
    # X_train = preprocessing.normalize(X_train)
    model.fit(X_train, y_train)
    return model.predict([arguments])


def predict_car(classifier, arguments, training_data):
    X_train = []
    y_train = []
    for data in training_data:
        X_train.append(data[:-1])
        y_train.append(data[-1])
    classifier.fit(X_train, y_train)
    return classifier.predict([arguments])


def get_cars_predicted_by_classifier(classifier, observation, training_data):
    predicted_cars = {}
    for i in range(MAIN_CAR_FEATURES_AMOUNT):
        for j in range(-10, 10, 5):
            observation_copy = observation.copy()
            observation_copy[i] = observation_copy[i] + j
            car = predict_car(classifier, observation_copy, training_data[6])[0]
            if car in predicted_cars.keys():
                predicted_cars[car] += 1
            else:
                predicted_cars[car] = 1
    return predicted_cars


def merge_dicts(car_dicts):
    result_car_dict = {}
    for car_dict in car_dicts:
        result_car_dict.update(car_dict)
    return result_car_dict


def create_result_list(cars_sorted_dict):
    cars_ammount = 0
    for k, v in cars_sorted_dict.items():
        cars_ammount += v
    # print(cars_ammount)
    result_list = []
    for k, v in cars_sorted_dict.items():
        if v / cars_ammount > 0.05:
            percent_rate = int(100 * v / cars_ammount)
            double_rate = percent_rate / 100
            result_list.append({"name": k, "rate": str(percent_rate) + "%", "doubleRate": double_rate})
        else:
            return result_list
    return result_list


training_data = generate_training_datasets()


def get_prediction(arguments):
    predicted_engine = predict(arguments.get("engine"), training_data[0])
    predicted_car_body = predict(arguments.get("car_body"), training_data[1])
    predicted_costs = predict(arguments.get("costs"), training_data[2])
    predicted_car_details = predict(arguments.get("car_details"), training_data[3])
    predicted_equipment = predict(arguments.get("equipment"), training_data[4])
    predicted_driving_features = predict(arguments.get("driving_features"), training_data[5])
    car_elements_list = [predicted_engine[0], predicted_car_body[0], predicted_costs[0], predicted_car_details[0],
                         predicted_equipment[0], predicted_driving_features[0]]
    # print(car_elements_list)

    classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        DecisionTreeClassifier(max_depth=5),
        GaussianNB()
    ]

    observation = car_elements_list

    predicted_cars_dicts = []
    for classifier in classifiers:
        predicted_cars_dicts.append(get_cars_predicted_by_classifier(classifier, observation, training_data))

    predicted_cars = dict(merge_dicts(predicted_cars_dicts))

    cars_with_recommendation = get_recommendation(predicted_cars, observation)

    # recommended_cars = get_recommendation(predicted_cars)
    # print("rc", recommended_cars)

    # recommended_cars_by_historical_data = dict(get_all_similar_predictions(observation))
    # print(predicted_cars)
    # print("rh", recommended_cars_by_historical_data)
    # predicted_cars.update(recommended_cars_by_historical_data)

    cars_sorted_dict = dict(sorted(cars_with_recommendation.items(), key=lambda item: item[1], reverse=True))
    result_list = create_result_list(cars_sorted_dict)
    return {"cars": result_list, "features": observation}


def main():
    parser = argparse.ArgumentParser(description='Elements of car')
    parser.add_argument('engine_power', type=int)
    parser.add_argument('fuel_consumption', type=int)
    parser.add_argument('acceleration', type=int)
    parser.add_argument('max_speed', type=int)
    parser.add_argument('durability', type=int)
    parser.add_argument('space_front', type=int)
    parser.add_argument('space_back', type=int)
    parser.add_argument('trunk', type=int)
    parser.add_argument('comfort', type=int)
    parser.add_argument('quality_finish', type=int)
    parser.add_argument('quality_mute', type=int)
    parser.add_argument('ease_of_use', type=int)
    parser.add_argument('comfort_equipment', type=int)
    parser.add_argument('security_equipment', type=int)
    parser.add_argument('extra_equipment', type=int)
    parser.add_argument('price', type=int)
    parser.add_argument('price_loss', type=int)
    parser.add_argument('extra_costs', type=int)
    parser.add_argument('driving', type=int)
    parser.add_argument('breaking', type=int)
    parser.add_argument('driving_modes', type=int)
    parser.add_argument('gearbox', type=int)

    args = parser.parse_args()

    arguments = {
        "engine": [args.engine_power, args.fuel_consumption, args.acceleration, args.max_speed, args.durability],
        "car_body": [args.space_front, args.space_back, args.trunk, args.comfort],
        "costs": [args.price, args.price_loss, args.extra_costs],
        "car_details": [args.quality_finish, args.quality_mute, args.ease_of_use],
        "equipment": [args.comfort_equipment, args.security_equipment, args.extra_equipment],
        "driving_features": [args.driving, args.breaking, args.driving_modes, args.gearbox]}

    return get_prediction(arguments)


if __name__ == '__main__':
    print(main())
