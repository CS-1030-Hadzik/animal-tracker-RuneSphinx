from animal import Animal
from dog import Dog


def main():
    # TODO: Create an instance of the Animal class
    animal = Animal("Generic", "Unknown")
    # TODO: Print the Animal instance
    print(animal)
    # TODO: Call the method to make a generic animal sound
    animal.make_sound()

    # TODO: Create an instance of the Dog class
    doggy = Dog("Fred","Canine","Golden Retriver")
    # TODO: Print the Dog instance
    print(doggy)
    # TODO: Call the method to make the dog-specific sound
    doggy.make_sound()
    # TODO print out all the animals
    print("All animals:")
    for animal in Animal.all_animals:
        print(animal)


if __name__ == "__main__":
    main()