#!/usr/bin/python3

class AnimalActions:
    def quack(self): return self.strings['quack']
    def feathers(self): return self.strings['feathers']
    def bark(self): return self.strings['bark']
    def fur(self): return self.strings['fur']

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        feathers = "The duck has gray and white feathers.",
        bark = "The duck cannot bark.",
        fur = "The duck has no fur."
    )
 
class Person(AnimalActions):
    strings = dict(
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    strings = dict(
        quack = "The dog cannot quack.",
        feathers = "The dog has no feathers.",
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )



def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

# 这段代码展示了 **多态（polymorphism）** 的概念：

# 多态实现**：虽然传入的是不同类型的对象，但只要这些类都实现了相同名称的方法
# 函数就能根据实际对象类型自动调用对应的方法。

# 这种设计允许用统一的接口处理不同类型的对象，是面向对象编程中多态性的典型应用。

def main():
    donald = Duck()
    john = Person()
    fido = Dog()


    print("- In the forest:")
    for o in ( donald, john, fido ):   # 列表推导式， o: object
        in_the_forest(o)               # object as parameter to the function

    print("- In the doghouse:")
    for o in ( donald, john, fido ):
        in_the_doghouse(o)
 
if __name__ == "__main__": 
    main()  # noqa: E701


# def in_the_doghouse(AnimalActions):
#     print(AnimalActions.bark())
#     print(AnimalActions.fur())

# def in_the_forest(AnimalActions):
#     print(AnimalActions.quack())
#     print(AnimalActions.feathers())
