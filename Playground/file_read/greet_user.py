import json

if __name__ == '__main__':
    filename = 'username.json'
    with open(filename) as file_object:
        username = json.load(file_object)
        print("Welcome back, " + username + "!")