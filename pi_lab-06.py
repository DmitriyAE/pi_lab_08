# 7. Найти средний возраст пассажиров по каждому классу обслуживания (поле Pclass)
with open('data.csv') as file:
    class1_total_age = 0
    class1_passenger_count = 0
    class2_total_age = 0
    class2_passenger_count = 0
    class3_total_age = 0
    class3_passenger_count = 0

    for line in file:
        data = line.strip().split(',')
        if data[6] == 'Age' or data[6] == '' or data[6] == 'Pclass' or data[2] == '':
            continue
        if data[2] == '1':
            class1_total_age += float(data[6])
            class1_passenger_count += 1
        elif data[2] == '2':
            class2_total_age += float(data[6])
            class2_passenger_count += 1
        elif data[2] == '3':
            class3_total_age += float(data[6])
            class3_passenger_count += 1

class1_average_age = 0
if class1_passenger_count > 0:
    class1_average_age = class1_total_age / class1_passenger_count

class2_average_age = 0
if class2_passenger_count > 0:
    class2_average_age = class2_total_age / class2_passenger_count

class3_average_age = 0
if class3_passenger_count > 0:
    class3_average_age = class3_total_age / class3_passenger_count

print(f"Средний возраст пассажиров первого класса: {class1_average_age:.2f}")
print(f"Средний возраст пассажиров второго класса: {class2_average_age:.2f}")
print(f"Средний возраст пассажиров третьего класса: {class3_average_age:.2f}")
