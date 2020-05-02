from sklearn import preprocessing
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier

from python.generator import generate_engine, generate_car_body, generate_costs, generate_car_details, \
    generate_equipment, generate_driving_features, get_cars
import numpy as np

from sklearn.linear_model import LogisticRegression


def generate_training_datasets():
    engine = generate_engine(100, 5)
    car_body = generate_car_body(100, 4)
    costs = generate_costs(100, 3)
    car_details = generate_car_details(100, 3)
    equipment = generate_equipment(100, 3)
    driving_features = generate_driving_features(100, 4)
    cars = get_cars()
    return engine, car_body, costs, car_details, equipment, driving_features, cars


def predict(arguments, training_data):
    X_train = []
    y_train = []
    for data in training_data:
        X_train.append(data[:-1])
        y_train.append(data[-1])
    model1 = LogisticRegression(random_state=1)
    model2 = DecisionTreeClassifier(random_state=1)
    model = VotingClassifier(estimators=[('lr', model1), ('dt', model2)], voting='hard')
    print(X_train)
    print(y_train)
    X_train = preprocessing.normalize(X_train)
    print("Tutaj")
    model.fit(X_train, y_train)
    return model.predict([arguments])


def predict_car(arguments, training_data):
    X_train = []
    y_train = []
    for data in training_data:
        X_train.append(data[:-1])
        y_train.append(data[-1])
    from sklearn.neighbors import KNeighborsClassifier
    neigh = KNeighborsClassifier(n_neighbors=5)
    neigh.fit(X_train, y_train)
    return neigh.predict([arguments])


def parse_arguments(arguments):
    return arguments


if __name__ == '__main__':
    arguments = {"engine": [10, 8, 5, 4, 3], "car_body": [5, 7, 8, 4], "costs": [5, 5, 2],
                 "car_details": [7, 8, 5], "equipment": [5, 8, 2], "driving_features": [5, 7, 4, 7]}
    training_data = generate_training_datasets()
    predicted_engine = predict(arguments.get("engine"), training_data[0])
    predicted_car_body = predict(arguments.get("car_body"), training_data[1])
    predicted_costs = predict(arguments.get("costs"), training_data[2])
    predicted_car_details = predict(arguments.get("car_details"), training_data[3])
    predicted_equipment = predict(arguments.get("equipment"), training_data[4])
    predicted_driving_features = predict(arguments.get("driving_features"), training_data[5])
    # print(predicted_engine)
    # print(predicted_car_body)
    # print(predicted_costs)
    # print(predicted_car_details)
    # print(predicted_equipment)
    # print(predicted_driving_features)

    observation = [40, 50, 35, 70, 70, 45]
    for i in range(6):
        for j in range(-10,10):
            observation_copy = observation.copy()
            observation_copy[i] = observation_copy[i] + j
            print(predict_car(observation_copy, training_data[6]))
