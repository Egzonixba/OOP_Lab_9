# 1
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km"


if __name__ == "__main__":
    new_car = Car("ABC-123", 142)
    print(new_car)

#2
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change >= 0:
            self.current_speed = min(self.current_speed + speed_change, self.maximum_speed)
        else:
            self.current_speed = max(self.current_speed + speed_change, 0)

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km"


if __name__ == "__main__":
    new_car = Car("ABC-123", 142)
    new_car.accelerate(30)
    new_car.accelerate(70)
    new_car.accelerate(50)
    print(f"Current Speed: {new_car.current_speed} km/h")
    new_car.accelerate(-200)
    print(f"Final Speed: {new_car.current_speed} km/h")

#3
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change >= 0:
            self.current_speed = min(self.current_speed + speed_change, self.maximum_speed)
        else:
            self.current_speed = max(self.current_speed + speed_change, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return f"Registration Number: {self.registration_number}, Maximum Speed: {self.maximum_speed} km/h, Current Speed: {self.current_speed} km/h, Travelled Distance: {self.travelled_distance} km"


if __name__ == "__main__":
    new_car = Car("ABC-123", 142)
    new_car.accelerate(30)
    new_car.drive(1.5)
    new_car.accelerate(70)
    new_car.drive(2)
    new_car.accelerate(50)
    new_car.drive(1)
    print(new_car)

#4
import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        if speed_change >= 0:
            self.current_speed = min(self.current_speed + speed_change, self.maximum_speed)
        else:
            self.current_speed = max(self.current_speed + speed_change, 0)

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return f"| {self.registration_number:8} | {self.maximum_speed:13} | {self.current_speed:12} | {self.travelled_distance:15} |"


if __name__ == "__main__":
    cars = []
    for i in range(1, 11):
        registration_number = f"ABC-{i}"
        maximum_speed = random.randint(100, 200)
        cars.append(Car(registration_number, maximum_speed))

    race_end_distance = 10000
    while all(car.travelled_distance < race_end_distance for car in cars):
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)

    # Print table header
    print("| Registration | Maximum Speed | Current Speed | Travelled Distance |")
    print("-" * 60)

    # Print properties of each car
    for car in cars:
        print(car)

