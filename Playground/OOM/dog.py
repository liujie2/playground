"""
创建dog类 每个实例都将存储名字和年龄, 赋予蹲下（sit）和打滚（rollover）的能力
__init__() 是一个特殊的函数，每当创建新的实例时，Python会自动运行他

"""


class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性名字和年龄"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下时"""
        print(self.name.title() + " now is sitting.")

    def roll_over(self):
        """模拟小狗被命令打滚时"""
        print(self.name.title() + " rolled over.")


if __name__ == '__main__':
    my_dog = Dog('willie', 6)
    your_dog = Dog('lucy', 3)
    print("My Dog's name is " + my_dog.name.title())
    print("My Dog is " + str(my_dog.age) + " year old.")
    my_dog.sit()
    print("\nYour Dog's name is " + your_dog.name.title())
    print("Your Dog is " + str(your_dog.age) + " year old.")
    your_dog.sit()

