class Person:
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
    def set_name(self, name) -> None:
        self.name = name
    def set_age(self, age) -> None:
        self.age = age
    def set_gender(self, gender) -> None:
        self.gender = gender
    def __str__(self):
        return f'Person(name="{self.name}", age={self.age}, gender="{self.gender}")'

john = Person("John", 23, "male")
print(john)
john.set_name("Julia")
john.set_gender("female")
print(john)
