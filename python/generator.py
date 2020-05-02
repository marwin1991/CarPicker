import random

from sklearn.linear_model import LogisticRegression


def normalize(value):
    if value > 10:
        return 10
    if value < 0:
        return 0
    return value


def get_cars():
    training_rows = []
    # ["engine", "car_body", "costs", "car_details", "equipment", "driving_feature"]
    training_rows.append([50, 80, 30, 72, 80, 68, "VW Passat"])
    training_rows.append([40, 60, 40, 65, 58, "VW Polo"])
    training_rows.append([45, 70, 35, 72, 70, 75, "VW Golf"])
    training_rows.append([55, 85, 25, 85, 80, 50, "VW Touareg"])
    training_rows.append([45, 65, 30, 77, 75, 45, "VW Tiguan"])
    training_rows.append([40, 50, 35, 70, 70, 45, "VW T-ROC"])

    training_rows.append([47, 84, 45, 70, 80, 67, "Skoda Superb"])
    training_rows.append([45, 78, 50, 70, 72, 71, "Skoda Octavia"])
    training_rows.append([40, 70, 60, 60, 58, 64, "Skoda Scala"])
    training_rows.append([50, 87, 32, 75, 77, 47, "Skoda Kodiaq"])
    training_rows.append([48, 75, 38, 70, 70, 42, "Skoda Karoq"])

    training_rows.append([57, 70, 25, 83, 74, 72, "Audi A4"])
    training_rows.append([58, 60, 22, 87, 74, 73, "Audi A5"])
    training_rows.append([60, 81, 22, 89, 80, 75, "Audi A6"])
    training_rows.append([61, 72, 21, 90, 80, 77, "Audi A7"])
    training_rows.append([61, 90, 15, 92, 91, 68, "Audi A8"])
    training_rows.append([60, 85, 17, 90, 90, 58, "Audi Q7"])
    training_rows.append([57, 75, 21, 81, 83, 60, "Audi Q5"])
    training_rows.append([53, 65, 27, 79, 80, 65, "Audi Q3"])

    #training_rows.append([, "Opel Corsa"])
    #training_rows.append([, "Opel Astra"])
    #training_rows.append([, "Opel Corsa"])
    #training_rows.append([, "Opel Corsa"])
    #training_rows.append([, "Opel Corsa"])


    return training_rows


def generate_engine(N, attributes_count):
    training_rows = []
    for _ in range(N):
        engine_power = random.randint(1, 10)
        fuel_consumption = random.randint(0, 10)
        acceleration = random.randint(engine_power - 2, engine_power + 2)
        max_speed = random.randint(acceleration - 1, acceleration + 3)
        durability = random.randint(0, 10)
        score = (engine_power + fuel_consumption + max_speed + acceleration + durability) * 100 / (
                attributes_count * 10) + random.randint(-5, 5)
        if fuel_consumption > 8:
            score += 2
        if durability > 8:
            score += 1
        engine_power = normalize(engine_power)
        fuel_consumption = normalize(fuel_consumption)
        acceleration = normalize(acceleration)
        max_speed = normalize(max_speed)
        durability = normalize(durability)
        training_rows.append([engine_power, fuel_consumption, max_speed, acceleration, durability, int(score)])
    return training_rows


def generate_car_body(N, attributes_count):
    training_rows = []
    for _ in range(N):
        space_front = random.randint(2, 10)
        space_back = random.randint(2, 10)
        trunk = random.randint(2, 10)
        comfort = random.randint(min(space_back, space_front) - 1, max(space_back, space_front) + 2)
        comfort = normalize(comfort)
        score = (space_front + space_back + trunk + comfort) * 100 / (attributes_count * 10) + random.randint(-3, 3)
        training_rows.append([space_front, space_back, trunk, comfort, int(score)])
    return training_rows


def generate_car_details(N, attributes_count):
    training_rows = []
    for _ in range(N):
        quality_finish = random.randint(2, 10)
        quality_mute = random.randint(2, 10)
        ease_of_use = random.randint(2, 10)
        score = (quality_finish + quality_mute + ease_of_use) * 100 / (attributes_count * 10) + random.randint(-2, 2)
        training_rows.append([quality_finish, quality_mute, ease_of_use, int(score)])
    return training_rows


def generate_equipment(N, attributes_count):
    training_rows = []
    for _ in range(N):
        comfort_equipment = random.randint(2, 10)
        security_equipment = random.randint(2, 10)
        extra_equipment = random.randint(0, 10)
        score = (comfort_equipment + security_equipment + extra_equipment) * 100 / (
                attributes_count * 10) + random.randint(-2, 2)
        training_rows.append([comfort_equipment, security_equipment, extra_equipment, int(score)])
    return training_rows


def generate_costs(N, attributes_count):
    training_rows = []
    for _ in range(N):
        price = random.randint(0, 10)
        price_loss = random.randint(0, 10)
        extra_costs = random.randint(price - 2, price + 2)
        extra_costs = normalize(extra_costs)
        score = (price + price_loss + extra_costs) * 100 / (attributes_count * 10) + random.randint(-2, 2)
        training_rows.append([price, price_loss, extra_costs, int(score)])
    return training_rows


def generate_driving_features(N, attributes_count):
    training_rows = []
    for _ in range(N):
        driving = random.randint(0, 10)
        breaking = random.randint(0, 10)
        driving_modes = random.randint(driving - 2, 10)
        driving_modes = normalize(driving_modes)
        score = (driving + breaking + driving_modes) * 100 / (attributes_count * 10) + random.randint(-1, 1)
        training_rows.append([driving, breaking, driving_modes, int(score)])
    return training_rows


def save_file(training_rows, file_name):
    file = open(file_name, "a")
    for row in training_rows:
        row_string = ",".join([str(value) for value in row])
        file.write(row_string + "\n")


def predict(training_data):
    X_train = []
    y_train = []
    for data in training_data:
        X_train.append(data[:-1])
        y_train.append(data[-1])
    print(X_train)
    print("////////////////")
    print(y_train)

    #   from sklearn.neighbors import KNeighborsClassifier
    #   neigh = KNeighborsClassifier(n_neighbors=3)
    #   neigh.fit(X_train, y_train)
    #   print(neigh.predict([[10, 10, 7, 8, 1]]))

    from sklearn.ensemble import VotingClassifier
    from sklearn.tree import DecisionTreeClassifier
    from sklearn import preprocessing

    model1 = LogisticRegression(random_state=1)
    model2 = DecisionTreeClassifier(random_state=1)
    model = VotingClassifier(estimators=[('lr', model1), ('dt', model2)], voting='hard')
    X_train = preprocessing.normalize(X_train)
    model.fit(X_train, y_train)
    print(model.predict([[1, 1, 10, 10, 5]]))


if __name__ == "__main__":
    engine = generate_engine(100, 5)
    car_body = generate_car_body(100, 4)
    costs = generate_costs(100, 3)
    car_details = generate_car_details(100, 3)
    equipment = generate_equipment(100, 3)
    driving_feature = generate_driving_features(100, 3)
    save_file(engine, "engine.txt")
    save_file(car_body, "car_body.txt")
    save_file(costs, "costs.txt")
    save_file(car_details, "car_details.txt")
    save_file(equipment, "equipment.txt")
    save_file(driving_feature, "driving_feature.txt")
    save_file(get_cars(), "cars.txt")

    predict(engine)
