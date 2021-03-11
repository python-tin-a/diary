
"""
void foo(int a) {
}
"""

animal_name = "Mistigri"


def speak(animal_name):
    print("Miaouuuu %s" % animal_name)


class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.sleep_counter = 0

    def speak(self):
        print("Wafff (%s)" % self.name)

    def sleep(self, hours):
        print("ZZffjjZZZfjjjZZZ for %dh (%s)" % (hours, self.name))
        self.sleep_counter += hours

# Définition d'une classe "Cat"
class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.sleep_counter = 0

    def speak(self):
        print("Miaouuu (%s)" % self.name)

    def sleep(self, hours):
        """Fait dormir le chat pendant `hours` heures."""
        print("Zzzzzz for %dh (%s)" % (hours, self.name))
        self.sleep_counter += hours

    def __add__(self, other):
        dog = Dog(self.name + other.name)
        dog.age = self.age + other.age
        dog.sleep_counter = self.sleep_counter + other.sleep_counter
        return dog


class SuperListe(list): # Je crée une extension à une liste par héritage
    def super_sum(self):
        out = 0
        for element in self:
            out += element ** 2
        return out

