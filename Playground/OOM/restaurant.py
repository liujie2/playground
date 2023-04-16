class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name.title())
        print("Cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is opening")


if __name__ == '__main__':
    chinese_restaurant = Restaurant('Chinese', 'Chinese Food')
    chinese_restaurant.describe_restaurant()
    japanese_restaurant = Restaurant('Japan', 'Susi')
    japanese_restaurant.describe_restaurant()
    italy_restaurant = Restaurant('Italy', 'Pizza')
    italy_restaurant.describe_restaurant()