class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())
        print(str(self.number_served) + " people served")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opening")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served


if __name__ == '__main__':
    chinese_restaurant = Restaurant('Chinese', 'Chinese Food')
    chinese_restaurant.describe_restaurant()
    chinese_restaurant.set_number_served(50)
    chinese_restaurant.describe_restaurant()
    chinese_restaurant.increment_number_served(10)
    chinese_restaurant.describe_restaurant()
    japanese_restaurant = Restaurant('Japan', 'Susi')
    japanese_restaurant.describe_restaurant()
    italy_restaurant = Restaurant('Italy', 'Pizza')
    italy_restaurant.describe_restaurant()