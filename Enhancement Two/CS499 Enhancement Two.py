"""
    Created by Cydnie Fisher on November 17th, 2024.
    This program is able to store dogs and monkeys with the respective attributes.
    Users are able to enter animals into a dictionary,
    and print animals based on the animal type and reserved status.
    Reserved animals can be sent on missions to search for and rescue humans.

    Edited on November 21st, 2024 for my second enhancement category in CS499
    The lists to store animals have been switched to dictionaries. Unique IDs
    have also been implemented to help search for animals more efficiently.
    These changes have decreased the runtime complexity when iterating through
    the animals from O(n) to O(1). A helper function has also been added to
    ensure that the same animal is not entered twice. This works be comparing
    all attributes, except the unique IDs, for all animals. Lastly, a helper
    function was created to ensure that the appropriate animal is reserved
    if multiple animals of the same animal type also share the same name.
"""
import uuid
from collections import defaultdict

# dictionaries to store instances of Dog and Monkey classes
dog_dict = {}
monkey_dict = {}

# used to map names to unique IDs
dog_id = defaultdict(list)
monkey_id = defaultdict(list)


# base class for program, represents common attributes for rescue animals
class RescueAnimal:
    # method which initializes common attributes for rescue animals
    def __init__(self, name="", animal_type="", gender="", age=0, weight=0.0, acquisition_date="",
                 acquisition_country="", training_status="", reserved=False, in_service_country=""):
        self.unique_id = str(uuid.uuid4())  # generate a unique ID
        self.name = name
        self.animal_type = animal_type
        self.gender = gender
        self.age = age
        self.weight = weight
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country

    # method to return formatted string, used to output animal attributes to user
    def __str__(self):
        return (f"{self.animal_type} Name: {self.name}, Training Status: {self.training_status}, "
                f"Service Location: {self.in_service_country}, Reserved: {self.reserved}")


# subclass of RescueAnimal for dogs, ensuring inheritance
class Dog(RescueAnimal):
    # method to extend initialization of attributes from RescueAnimal
    # includes a breed attribute, which is specific to dogs
    def __init__(self, name, breed, gender, age, weight, acquisition_date, acquisition_country,
                 training_status, reserved, in_service_country):
        super().__init__(name, "Dog", gender, age, weight, acquisition_date, acquisition_country,
                         training_status, reserved, in_service_country)
        self.breed = breed

    # method to override the formatted string in RescueAnimal
    # to include attributes specific to dogs
    def __str__(self):
        return (f"Dog Name: {self.name}, Breed: {self.breed}, Training Status: {self.training_status}, "
                f"Service Location: {self.in_service_country}, Reserved: {self.reserved}")


# subclass of RescueAnimal for monkeys, ensuring inheritance
class Monkey(RescueAnimal):
    # only these species of monkey are valid
    valid_species = ["Capuchin", "Guenon", "Macaque", "Marmoset", "Squirrel Monkey", "Tamarin"]

    # method to extend initialization of attributes from RescueAnimal
    # includes tail and body length, height, and species attributes, which are specific to monkeys
    def __init__(self, name, gender, age, weight, acquisition_date, acquisition_country,
                 training_status, reserved, in_service_country, tail_length, height, body_length, species):
        super().__init__(name, "Monkey", gender, age, weight, acquisition_date, acquisition_country,
                         training_status, reserved, in_service_country)
        self.tail_length = tail_length
        self.height = height
        self.body_length = body_length
        self.species = species

    # method to override the formatted string in RescueAnimal
    # to include attributes specific to monkeys
    def __str__(self):
        return (f"Monkey Name: {self.name}, Species: {self.species}, Training Status: {self.training_status}, "
                f"Service Location: {self.in_service_country}, Reserved: {self.reserved}")


# helper function to ensure integers are entered as a valid format
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


# helper function to ensure float integers are entered as a valid format
def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# helper function to prompt user for reserved status, and ensure valid user input
def reserved_status():
    while True:
        reserved = input("Is the animal reserved? (y/n): ").strip().lower()
        if reserved == 'y':
            return True
        elif reserved == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


# helper function used to ensure a monkeys species is valid
def valid_monkey_species():
    while True:
        species = input("What is the monkey's species? ").lower()
        if species.capitalize() in Monkey.valid_species:
            return species
        else:
            print("Invalid species. Valid species are: Capuchin, Guenon, Macaque, Marmoset, Squirrel Monkey, Tamarin")


# helper function to ensure duplicate animals are not added to dictionary
def duplicate_animal(animal, animal_dict):
    for existing_animal in animal_dict.values():
        # compare all attributes except unique_id
        if {key: value for key, value in animal.__dict__.items() if key != "unique_id"} == \
           {key: value for key, value in existing_animal.__dict__.items() if key != "unique_id"}:
            return True
    return False


# helper function to collect and return attributes used for both dogs and monkeys
def get_common_animal_data():
    name = input("What is the animal's name? ").lower()
    gender = input("What is the animal's gender? ").lower()
    age = get_valid_int("What is the animal's age? ")
    weight = get_valid_float("What is the animal's weight? ")
    acquisition_date = input("What is the animal's acquisition date? ")
    acquisition_country = input("What is the animal's acquisition country? ").lower()
    training_status = input("What is the animal's training status? ").lower()
    reserved = reserved_status()
    in_service_country = input("Which country is the animal in service? ").lower()
    return {
        "name": name,
        "gender": gender,
        "age": age,
        "weight": weight,
        "acquisition_date": acquisition_date,
        "acquisition_country": acquisition_country,
        "training_status": training_status,
        "reserved": reserved,
        "in_service_country": in_service_country
    }


# function to collect attributes for a new dog
# attributes are used to create an instance, which is appended to the list of dogs
def intake_new_dog():
    data = get_common_animal_data()
    breed = input("What is the dog's breed? ").lower()
    dog = Dog(data["name"], breed, data["gender"], data["age"], data["weight"], data["acquisition_date"],
              data["acquisition_country"], data["training_status"], data["reserved"], data["in_service_country"])
    # check for duplicates
    if duplicate_animal(dog, dog_dict):
        print("This dog is already in the system.")
        return
    # create unique ID for dog and add to dictionary
    dog_dict[dog.unique_id] = dog
    dog_id[dog.name].append(dog.unique_id)
    print(f"Dog {dog.name} has been added.")


# function to collect attributes for a new monkey
# attributes are used to create an instance, which is appended to the list of monkeys
def intake_new_monkey():
    species = valid_monkey_species()
    data = get_common_animal_data()
    tail_length = get_valid_float("What is the monkey's tail length? ")
    height = get_valid_float("What is the monkey's height? ")
    body_length = get_valid_float("What is the monkey's body length? ")
    monkey = Monkey(data["name"], data["gender"], data["age"], data["weight"], data["acquisition_date"],
                    data["acquisition_country"], data["training_status"], data["reserved"], data["in_service_country"],
                    tail_length, height, body_length, species)
    # check for duplicates
    if duplicate_animal(monkey, monkey_dict):
        print("This monkey is already in the system.")
        return
    # create unique ID for monkey and add to dictionary
    monkey_dict[monkey.unique_id] = monkey
    monkey_id[monkey.name].append(monkey.unique_id)
    print(f"Monkey {monkey.name} has been added.")


# function to reserve animals based on animal type and service country entered by user
def reserve_animal():
    # prompt user for animal type and name
    animal_type = input("Would you like to reserve a dog or a monkey? ").lower()
    name = input("What is the name of the animal you'd like to reserve? ").strip().lower()
    # use handle_reservation helper function to help determine which animal to reserve
    if animal_type == "dog" and name in dog_id:
        handle_reservation(dog_id[name], dog_dict)
    elif animal_type == "monkey" and name in monkey_id:
        handle_reservation(monkey_id[name], monkey_dict)
    else:
        print(f"No {animal_type} named {name} found.")


# helper function to help with animal reservation
def handle_reservation(matching_ids, animal_dict):
    # determine if multiple animals share the same attributes prompted for in reservation_animal
    # if only one animal, use this animal
    if len(matching_ids) == 1:
        unique_id = matching_ids[0]
    # if multiple animals, prompt user to select the desired animal, then use this animal
    else:
        print("Multiple animals found")
        for i, unique_id in enumerate(matching_ids, 1):
            print(f"{i}. {animal_dict[unique_id]}")
        choice = get_valid_int("Enter the number of the animal you'd like to reserve: ") - 1
        unique_id = matching_ids[choice]
    animal = animal_dict[unique_id]
    # reserve animal if not reserved
    if not animal.reserved:
        animal.reserved = True
        print(f"{animal.name} has been reserved.")
    else:
        print(f"{animal.name} is already reserved.")


# prints a list of animals based on the users input
# can print animals based on animal type and reserved status
def print_animals(choice):
    if choice == "4":
        print("All dogs:")
        for dog in dog_dict.values():
            print(dog)
    elif choice == "5":
        print("All monkeys:")
        for monkey in monkey_dict.values():
            print(monkey)
    elif choice == "6":
        print("All available animals:")
        for dog in dog_dict.values():
            if not dog.reserved:
                print(dog)
        for monkey in monkey_dict.values():
            if not monkey.reserved:
                print(monkey)
    elif choice == "7":
        print("All reserved animals:")
        for dog in dog_dict.values():
            if dog.reserved:
                print(dog)
        for monkey in monkey_dict.values():
            if monkey.reserved:
                print(monkey)
    else:
        print("Invalid input. Please select a valid menu option.")


# used to display a menu with options to the user
def display_menu():
    print("\n\nRescue Animal System Menu")
    print("[1] Intake a new dog")
    print("[2] Intake a new monkey")
    print("[3] Reserve an animal")
    print("[4] Print a list of all dogs")
    print("[5] Print a list of all monkeys")
    print("[6] Print a list of all animals that are not reserved")
    print("[7] Print a list of all animals that are reserved")
    print("[q] Quit application")
    print("\nEnter a menu selection")


# calls method to display menu to user
# prompts and reads input from user and acts accordingly
def main():
    while True:
        display_menu()
        menu_choice = input()
        if menu_choice == "1":
            intake_new_dog()
        elif menu_choice == "2":
            intake_new_monkey()
        elif menu_choice == "3":
            reserve_animal()
        elif menu_choice in ["4", "5", "6", "7"]:
            print_animals(menu_choice)
        elif menu_choice == "q":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please try again.")


# run the program
if __name__ == "__main__":
    main()
