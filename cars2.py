class Car:

    def __init__(self , car_brand , car_model , car_price
                 , car_color , manufacture_year):

        self.car_brand = car_brand
        self.car_model = car_model
        self.car_price = car_price
        self.car_color = car_color
        self.manufacture_year = manufacture_year



    def display_info(self):
        print(f"Brand: {self.car_brand} , Model: {self.car_model} , Price: {self.car_price} ,"
              f"Color: {self.car_color} , Manufacture year: {self.manufacture_year}")



cars = [
    Car("Tesla", "Model S", 75000, "Black", 2021),
    Car("Ford", "Mustang", 45000, "Red", 2019),
    Car("BMW", "X5", 60000, "Black", 2022),
    Car("BMW", "X3", 50000, "White", 2022),
    Car("Audi", "A4", 35000, "White", 2022),
    Car("Audi", "Q7", 80000, "Black", 2021),
    Car("Toyota", "Corolla", 20000, "Red", 2022),
    Car("Toyota", "Camry", 30000, "White", 2022),
]


def sort_price(cars):
    sorted_cars = sorted(cars , key=lambda car: car.car_price , reverse=True )
    for car in sorted_cars:
        car.display_info()


def list_by_brand(car_brand , cars):
    branded_cars = [car for car in cars if car.car_brand.lower() == car_brand.lower()]
    if branded_cars:
        for car in branded_cars:
            car.display_info()
    else:
        print("No cars with that brand")


def search_color(car_color , cars):
    color_Car = [car for car in cars if car.car_color.lower() == car_color.lower()]
    if(color_Car):
        most_expnsive = max(color_Car , key=lambda car: car.car_price)
        most_expnsive.display_info()
    else :
        print("No cars with that color")


def newest_car(cars):
    cars_2022_year = [car for car in cars if car.manufacture_year == 2022]
    if cars_2022_year:
        for car in cars_2022_year:
            car.display_info()
    else:
        print("No cars are from 2022")


print("Sorted by price:")
sort_price(cars)



print("\nCars by Brand 'BMW :")
list_by_brand("BMW" , cars)


print("\nMost expensive black car is")
search_color("Black" , cars)

print("\nNewest cars(2022):")
newest_car(cars)
