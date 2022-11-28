class Parent:
    parent_attr = 10

    def __init__(self):
        print("Вызов родительского класса")

    def parent_age(self):
        print("Вызов возраста родителя")

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print("Атрибут родителя: {}" .format(Parent.parent_attr))


class Child(Parent):
    def __init__(self):
        print('Вызов класса наследника')

    def child_age(self):
        print('Вызов возраста наследника')

c = Child()
c.child_age()
c.parent_age()
c.set_attr(20)
c.get_attr()