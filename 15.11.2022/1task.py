class Student:
    def __init__(self, name, group, city, age, job, sportssection):
        print('init', name)
        self.name = name
        self.group = group
        self.city = city
        self.age = age
        self.job = job
        self.sportssection = sportssection

    def years(self):
        print(f"{self.name} is {self.age}")

    def city(self):
        print(f"{self.name} from {self.city} city")

    def job(self):
        print(f"{self.name} is working on {self.job}")

    def sportssection(self):
        print(f"{self.name} goes to {self.sportssection}")

    def __new__(cls, *args, **kwargs):
        print('new')
        return super(Student, cls).__new__(cls)

    def __del__(self):
        print(self.name, 'is deleted')

    def introduce(self):
        print(f'Hi, I am {self.name} from group {self.group}')

    @staticmethod
    def say_hi(name):
        print('Hi,', name)

new_group = '11-250'
a = Student('Izida', new_group)
b = Student('Kate', '11-210')

class Collection:
    def __init__(self, list):
        self.list = list

    def __len__(self):
        return len(self.list)

list = ['Hi', 'Hello']
print(len(list))
collection = Collection(list)

print(len(collection))