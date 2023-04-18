import os

if __name__ == '__main__':
    with open('pi_digits.txt', 'r') as file_object:
        content = file_object.read()
        print(content.rstrip())

