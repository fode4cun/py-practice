"""
Continue callback next object method.
"""


class Person:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def do_action(self):
        print(self.name, self.action.name, end=" ")
        return self.action


class Action:
    def __init__(self, name):
        self.name = name

    def amount(self, val):
        print(val, end=" ")
        return self

    def stop(self):
        print("then stop")


if __name__ == '__main__':
    move = Action('move')
    person = Person('Jack', move)
    person.do_action().amount('5m').stop()
