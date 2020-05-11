from sklearn import preprocessing
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from python.generator import generate_engine, generate_car_body, generate_costs, generate_car_details, \
    generate_equipment, generate_driving_features, get_cars
from python.historical_data import get_all_similar_predictions

from sklearn.linear_model import LogisticRegression

MAIN_CAR_FEATURES_AMMOUNT = 6
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
    model1 = LogisticRegression(random_state=1)
    model2 = DecisionTreeClassifier(random_state=1)
    model = VotingClassifier(estimators=[('lr', model1), ('dt', model2)], voting='hard')
    print(X_train)
    print(y_train)
    X_train = preprocessing.normalize(X_train)
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

def get_cars_predicted_by_classifier(classifier, observation):
    predicted_cars = {}
    for i in range(MAIN_CAR_FEATURES_AMMOUNT):
        for j in range(-10, 10, 5):
            observation_copy = observation.copy()
            observation_copy[i] = observation_copy[i] + j
            car = predict_car(classifier, observation_copy, training_data[6])[0]
            if car in predicted_cars.keys():
                predicted_cars[car] +=1
            else:
                predicted_cars[car] = 1
    return predicted_cars


def merge_dicts(car_dicts):
    result_car_dict = {}
    for car_dict in car_dicts:
        result_car_dict.update(car_dict)
    return result_car_dict




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
    car_elements_list = [predicted_engine, predicted_car_body, predicted_costs, predicted_car_details,
                         predicted_equipment, predicted_driving_features]

    classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="linear", C=0.025),
        SVC(gamma=2, C=1),
        DecisionTreeClassifier(max_depth=5),
        GaussianNB()
    ]

    observation = [50, 80, 48, 72, 70, 45]
    #observation = car_elements_list

    predicted_cars_dicts = []
    for classifier in classifiers:
        predicted_cars_dicts.append(get_cars_predicted_by_classifier(classifier, observation))

    predicted_cars = dict(merge_dicts(predicted_cars_dicts))
    recommended_cars_by_historical_data = dict(get_all_similar_predictions(observation))
    print(predicted_cars)
    print(recommended_cars_by_historical_data)
    predicted_cars.update(recommended_cars_by_historical_data)
    print(dict(sorted(predicted_cars.items(), key=lambda item : item[1], reverse=True)))
