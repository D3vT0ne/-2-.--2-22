class Classifier:
    def __init__(self, data):
        self.data = data

    def predict_class(self, predict_point, radius):
        min_distance = float('inf')
        predicted_class = None
        for class_name, points in self.data.items():
            for point in points:
                distance = ((predict_point[0] - point[0])**2 + (predict_point[1] - point[1])**2)**0.5
                if distance < min_distance:
                    min_distance = distance
                    predicted_class = class_name
        return predicted_class


def main():
    data = {}
    while True:
        x = float(input("Введите координаты точки по значению x: "))
        y = float(input("Введите координаты точки по значению y: "))
        class_name = input("Введите класс объекта: ")
        point = (x, y)
        if class_name not in data:
            data[class_name] = [point]
        else:
            data[class_name].append(point)

        choice = input("Хотите ли вы еще добавить точку? (Введите 'y' для продолжения): ")
        if choice.lower() != 'y':
            break

    predict_point = tuple(float(coord) for coord in input("Введите координаты точки неизвестного класса через пробел: ").split())
    radius = float(input("Задайте величину радиуса ближайших соседей: "))

    classifier = Classifier(data)
    predicted_class = classifier.predict_class(predict_point, radius)
    print(f"Точка с координатами {predict_point} предположительно принадлежит классу: {predicted_class}")


if __name__ == "__main__":
    main()
