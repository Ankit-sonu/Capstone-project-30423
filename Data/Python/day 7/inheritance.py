class Person:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"Name={self.name}, dept={self.dept}"

    def __eq__(self,x):
        if self.dept == x.dept and self.name == x.name:
            return True
        else:
            return False

    def __hash__(self):
        return 1001


if __name__ == "__main__":
    person1 = Person("John", "Department")
    print(hash(person1))
    person2 = Person("John", "Department")
    print(hash(person2))

    if person1 == person2:
        print("Both are equal")
    else:
        print("Both are not equal")