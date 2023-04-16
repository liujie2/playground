class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def greet_user(self):
        print("greetings " + self.first_name.title() + "." + self.last_name.title())


if __name__ == '__main__':
    jie_liu = User('jie', 'liu')
    jie_liu.greet_user()
