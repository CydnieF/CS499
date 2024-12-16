""" Created by Cydnie Fisher on November 17th, 2024.
    This is the first for the first enhancement category for CS 499.
    This program is able to store dogs and monkeys with the respective attributes.
    Users are able to enter animals into a list,
    and print animals based on the animal type and reserved status.
    Reserved animals can be sent on missions to search for and rescue humans.
"""


# base class for program, represents common attributes for rescue animals
class RescueAnimal:
    # method which initializes common attributes for rescue animals
    def __init__(self, name="", animal_type="", gender="", age=0, weight=0.0, acquisition_date="",
                 acquisition_country="", training_status="", reserved=False, in_service_country=""):
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


# list to store instances of Dog class and Monkey class
dog_list = []
monkey_list = []


# helper function to ensure integers are entered as a valid format
def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")


# helper function to ensure float integers are entered as a valid format
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


# helper function to prompt user for reserved status, and ensure valid user input
def reserved_status():
    while True:
        reserved = input("Is the animal reserved? (y/n): ").strip().lower()
        # sets y as True and n as False
        if reserved == 'y':
            return True
        elif reserved == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


# helper function used to ensure a monkeys species is valid
def valid_monkey_species():
    while True:
        species = input("What is the monkey's species? ")
        if species.capitalize() in Monkey.valid_species:
            return species
        else:
            print("Invalid species. Please enter a valid species. Valid species are:\n"
                  "Capuchin, Guenon, Macaque, Marmoset, Squirrel Monkey, Tamarin")


# helper function to collect and return attributes used for both dogs and monkeys
def get_common_animal_data():
    name = input("What is the animal's name? ")
    gender = input("What is the animal's gender? ")
    age = get_valid_int("What is the animal's age? ")
    weight = get_valid_float("What is the animal's weight? ")
    acquisition_date = input("What is the animal's acquisition date? ")
    acquisition_country = input("What is the animal's acquisition country? ")
    training_status = input("What is the animal's training status? ")
    reserved = reserved_status()
    in_service_country = input("Which country is the animal in service? ")
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
    breed = input("What is the dog's breed? ")
    dog = Dog(data["name"], breed, data["gender"], data["age"], data["weight"], data["acquisition_date"],
              data["acquisition_country"], data["training_status"], data["reserved"], data["in_service_country"])
    dog_list.append(dog)
    # validates that dog has been added to list of dogs
    print("This dog has been added to the Dog List.")


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
    monkey_list.append(monkey)
    # validates that monkey has been added to list of monkeys
    print("This monkey has been added to the Monkey List.")


# function to reserve animals based on animal type and service country entered by user
def reserve_animal():
    # prompt user for animal type and service country, validating each input
    animal_type = input("Would you like to reserve a dog or a monkey? ").lower()
    while animal_type not in ["dog", "monkey"]:
        print("Invalid animal type. Please enter 'dog' or 'monkey'.")
        animal_type = input().lower()
    service_location = input(f"Which country will the {animal_type} be serving in? ")
    reserved_animal = None

    # if animal type is dog, search the dog list, and set as reserved if not already
    if animal_type == "dog":
        for dog in dog_list:
            if dog.in_service_country.lower() == service_location.lower() and not dog.reserved:
                dog.reserved = True
                dog.in_service_country = service_location
                reserved_animal = dog
                break
    # if animal type is monkey, search the monkey list, and set as reserved if not already
    else:
        for monkey in monkey_list:
            if monkey.in_service_country.lower() == service_location.lower() and not monkey.reserved:
                monkey.reserved = True
                monkey.in_service_country = service_location
                reserved_animal = monkey
                break

    # if animal is reserved, output conformation message
    if reserved_animal:
        print(f"{reserved_animal.name} has been reserved.")
    # if animal cannot be reserved, output message
    else:
        print(f"No available {animal_type}s found in {service_location} to reserve.")


# prints a list of animals based on the users input
# can print animals based on animal type and reserved status
def print_animals(choice):
    if choice == "4":
        print("All dogs:")
        for dog in dog_list:
            print(dog)
    elif choice == "5":
        print("All monkeys:")
        for monkey in monkey_list:
            print(monkey)
    elif choice == "6":
        print("All available animals:")
        for animal in dog_list + monkey_list:
            if not animal.reserved:
                print(animal)
    elif choice == "7":
        print("All reserved animals:")
        for animal in dog_list + monkey_list:
            if animal.reserved:
                print(animal)
    else:
        print("Invalid input. Please select a valid menu option.")


# used to display a menu with options to the user
def display_menu():
    print("\n\n\t\t\tRescue Animal System Menu")
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
        else:
            print("Invalid input. Please select a valid menu option.")


# run the program
if __name__ == "__main__":
    main()
