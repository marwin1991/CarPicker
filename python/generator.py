import random

from sklearn.linear_model import LogisticRegression


def normalize(value):
    if value > 10:
        return 10
    if value < 0:
        return 0
    return value


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

    predict(engine)
