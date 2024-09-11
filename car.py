class Car:

    def __init__(self , car_brand , car_model , car_price , car_color , manifacture_year):
        self.car_brand = car_brand
        self.car_modal = car_model
        self.car_price = car_price
        self.car_color = car_color
        self.manifacture_year = manifacture_year


    def display_info(self):
        print("Car brand : " , self.car_brand , "Car model : " , self.car_modal , "Car price : " , self.car_price ,
              "Car color : " , self.car_color , "Manifacture year : " , self.manifacture_year)


cars = [
    Car("Toyota", "Corolla", 20000, "Red", 2022),
    Car("BMW", "X5", 60000, "Black", 2021),
    Car("Audi", "A4", 35000, "White", 2022),
    Car("Mercedes", "C-Class", 55000, "Blue", 2020),
    Car("Honda", "Civic", 18000, "Gray", 2022),
    Car("Tesla", "Model S", 75000, "Black", 2021),
    Car("Ford", "Mustang", 45000, "Red", 2019)
]

def sort_price(cars):
    sorted_cars = sorted(cars, key=lambda  car: car.car_price , reverse=True)
    for car in sorted_cars:
        car.display_info()

def list_by_brand(cars , brand):
    cars_by_brand = [car for car in cars if car.car_brand.lower() == brand.lower()]
    if cars_by_brand:
        for car in cars_by_brand:
            car.display_info()
    else:
        print(f"No cars found for brand : {brand}")

def search_color(cars , color):
    cars_by_color = [car for car in cars if car.car_color.lower() == color.lower()]
    if(cars_by_color):
        most_expensive = max(cars_by_color , key=lambda car: car.car_price)
        return most_expensive
    else:
        return None


def newest_car(cars):

    new_Cars = [car for car in cars if car.manifacture_year >= 2022]
    return new_Cars



print("Cars sorted by price (descending):")
sort_price(cars)

print("\n")

# 2. List all cars by a specific brand
print("Cars of brand 'BMW':")
list_by_brand(cars, "BMW")

print("\n")

# 3. Search for the most expensive car with a specific color
color = "Black"
expensive_car = search_color(cars, color)
if expensive_car:
    print(f"The most expensive car with color {color}:")
    expensive_car.display_info()
else:
    print(f"No car found with color {color}")

print("\n")

# 4. List cars manufactured in 2022
print("Cars manufactured in 2022:")
newest_cars = newest_car(cars)
if newest_cars:
    for car in newest_cars:
        car.display_info()
else:
    print("No cars manufactured in 2022")
