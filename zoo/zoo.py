class Animal:
    def __init__(self, name, species, age, height, width, preferred_habitat):
        self.name = name
        self.species = species
        self.age = age
        self.height = height
        self.width = width
        self.preferred_habitat = preferred_habitat
        self.health = round(100 * (1 / age), 3)

class Fence:
    def __init__(self, area, temperature, habitat):
        self.area = area
        self.temperature = temperature
        self.habitat = habitat
        self.animals = []
        self.occupied = 0

    def accomodare(self, animal):
        return self.habitat == animal.preferred_habitat and (self.area - self.occupied) >= (animal.height * animal.width)

    def add_animal(self, animal):
        if self.accomodare(animal):
            self.animals.append(animal)
            self.occupied += animal.height * animal.width
            return True
        return False

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            self.occupied -= animal.height * animal.width
            return True
        return False

class ZooKeeper:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.id = id

    def add_animal(self, animal, fence):
        return fence.add_animal(animal)

    def remove_animal(self, animal, fence):
        return fence.remove_animal(animal)

    def feed(self, animal, fence):
        new_height = animal.height * 1.02
        new_width = animal.width * 1.02
        new_area = new_height * new_width
        current_area = animal.height * animal.width

        if (fence.area - fence.occupied + current_area) >= new_area:
            fence.occupied -= current_area
            animal.height = new_height
            animal.width = new_width
            animal.health *= 1.01
            fence.occupied += new_area
            return True
        return False

    def clean(self, fence):
        if fence.area - fence.occupied == 0:
            return fence.occupied
        return fence.occupied / (fence.area - fence.occupied)

class Zoo:
    def __init__(self):
        self.fences = []
        self.zoo_keepers = []

    def add_fence(self, fence):
        self.fences.append(fence)
    def add_zoo_keeper(self, zoo_keeper):
        self.zoo_keepers.append(zoo_keeper)

    def describe_zoo(self):
        descrizione ="Guardians:\n"
        for keeper in self.zoo_keepers:
            descrizione +=f"ZooKeeper(name={keeper.name}, surname={keeper.surname}, id={keeper.id})\n"

        descrizione +="Fences:\n"
        for fence in self.fences:
            descrizione +=f"Fence(area={fence.area},temperature={fence.temperature}, habitat={fence.habitat})\nwith animals:\n"
            for animal in fence.animals:
                descrizione +=f"Animal(name={animal.name}, species={animal.species}, age={animal.age})\n"
            descrizione +="#" * 30 + "\n"

        return descrizione


















    
    
    
    

