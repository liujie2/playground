from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['milk', 'strawberry', 'blueberry']

    def icecream_describe(self):
        print(self.flavors)


if __name__ == '__main__':
    my_icecream_stand = IceCreamStand('hagendas', 'icecream')
    my_icecream_stand.icecream_describe()
