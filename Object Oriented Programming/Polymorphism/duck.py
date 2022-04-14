# Polymorphism : One name, multiple implementation

class Duck:
    def talk(self):
        print("Quak Quak!")


class Human:
    def talk(self):
        print("HI!")


class Dog:
    def bark(self):
        print("Bow Wow!")


def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()

    elif hasattr(obj, 'bark'):
        obj.bark()

    else:
        print("Something worng!")


d = Duck()
call_talk(d)

d = Human()
call_talk(d)

d = Dog()
call_talk(d)
