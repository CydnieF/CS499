import java.util.ArrayList;
import java.util.Scanner;

public class Driver {
    private static Scanner scnr = new Scanner(System.in);  // scanner object

    // array lists for dogs and monkeys
    private static ArrayList<Dog> dogList = new ArrayList<Dog>();
    private static ArrayList<Monkey> monkeyList = new ArrayList<Monkey>();

    public static void main(String[] args) {

        String menuChoice = ""; // local variable

        // static methods
        initializeDogList();
        initializeMonkeyList();

        displayMenu();  // call display menu method
        menuChoice = scnr.nextLine();  // get menu choice from user
        // loop that displays the menu, accepts user inputs, takes appropriate action
        while(!menuChoice.equalsIgnoreCase("q")) {  // q causes loop to quit executing
            switch (menuChoice) {  // execute menuChoice based on user input
                case "1":  // if user enters 1, execute intakeNewDog method
                    intakeNewDog(scnr);
                    break;
                case "2":  // if user enters 2, execute intakeNewMonkey method
                    intakeNewMonkey(scnr);
                    break;
                case "3":  // if user enters 3, execute reserveAnimal method
                    reserveAnimal(scnr);
                    break;
                case "4":  // if user enters 4, execute printAnimals method
                    printAnimals("4");
                    break;
                case "5":  // if user enters 5, execute printAnimals method
                    printAnimals("5");
                    break;
                case "6":  // if user enters 6, execute printAnimals method
                    printAnimals("6");
                    break;
                default:  // if user input is invalid, print message
                    if (!menuChoice.equalsIgnoreCase("q")) {
                        System.out.println("\n Invalid input, enter 1-6 or q");
                    }
                break;
            }
            // display menu and get menu choice after initial instance
            displayMenu();
            menuChoice = scnr.nextLine();
        }
    }

    // This method prints the menu options
    public static void displayMenu() {
        System.out.println("\n\n");
        System.out.println("\t\t\t\tRescue Animal System Menu");
        System.out.println("[1] Intake a new dog");
        System.out.println("[2] Intake a new monkey");
        System.out.println("[3] Reserve an animal");
        System.out.println("[4] Print a list of all dogs");
        System.out.println("[5] Print a list of all monkeys");
        System.out.println("[6] Print a list of all animals that are not reserved");
        System.out.println("[q] Quit application");
        System.out.println();
        System.out.println("Enter a menu selection");
    }


    // Adds dogs to a list for testing
    public static void initializeDogList() {
        Dog dog1 = new Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", false, "United States");
        Dog dog2 = new Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "Phase I", false, "United States");
        Dog dog3 = new Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", true, "Canada");

        dogList.add(dog1);
        dogList.add(dog2);
        dogList.add(dog3);
    }


    // Adds monkeys to a list for testing
    public static void initializeMonkeyList() {
        Monkey monkey1 = new Monkey("Monty", "male", "5", "27","02-10-2024", "United States", "intake", false, "United States", "3", "1.9", "16", "macaque");

        monkeyList.add(monkey1);
    }

    // create intakeNewDog method
    public static void intakeNewDog(Scanner scnr) {
        // get dog's name and assign value
        System.out.println("What is the dog's name?");
        String name = scnr.nextLine();
        // input validation if dog is already in dogList
        for(Dog dog: dogList) {
            if(dog.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis dog is already in our system\n\n");
                return; //returns to menu
            }
        }

        // code to instantiate new dog and add to list
        // get dog's breed and assign value
        System.out.println("What is the dog's breed?");
        String breed = scnr.nextLine();
        // get dog's gender and assign value
        System.out.println("What is the dog's gender?");
        String gender = scnr.nextLine();
        // get dog's age and assign value
        System.out.println("What is the dog's age?");
        String age = scnr.nextLine();
        //get dog's weight and assign value
        System.out.println("What is the dog's weight?");
        String weight = scnr.nextLine();
        // get dog's acquisition date and assign value
        System.out.println("What is the dog's acquisition date?");
        String acquisitionDate = scnr.nextLine();
        // get dog's acquisition country and assign value
        System.out.println("What is the dog's acquisition country?");
        String acquisitionCountry = scnr.nextLine();
        // get dog's training status and assign value
        System.out.println("What is the dog's training status?");
        String trainingStatus = scnr.nextLine();
        // get if dog is reserved and assign value
        System.out.println("Is this dog reserved?");
        boolean reserved = scnr.nextBoolean();
        // get country dog is serviced in and assign value
        System.out.println("Which country is the dog in service");
        String inServiceCountry = scnr.nextLine();

        // creates new dog object, includes data for attributes
        Dog dog = new Dog(name, breed, gender, age, weight, acquisitionDate,
                           acquisitionCountry, trainingStatus, reserved, inServiceCountry);
        dogList.add(dog); // add new dog to Dog ArrayList
        System.out.println("This dog has been added to the Dog List");  // input validation
    }

    public static void intakeNewMonkey(Scanner scnr) {
        // get monkey's name and assign value
        System.out.println("What is the monkey's name?");
        String name = scnr.nextLine();
        // input validation if monkey is already in monkeyList
        for (Monkey monkey : monkeyList) {
            if (monkey.getName().equalsIgnoreCase(name)) {
                System.out.println("\n\nThis monkey is already in our system\n\n");
                return; //returns to menu
            }
        }
        // monkey species must be valid
        boolean invalidSpecies = true;
        String species;
        // get monkey's species, execute loop until valid species is entered
        do {
            System.out.println("What is the monkey's species?");
            species = scnr.nextLine();

            for(String validSpecies : Monkey.validSpecies)
                if(species.equalsIgnoreCase(validSpecies))
                    invalidSpecies = false;

            if(invalidSpecies)  // print error message
                System.out.println("Invalid species. Please enter a valid species.");
        } while(invalidSpecies);

        // get monkey's gender and assign value
        System.out.println("What is the monkey's gender?");
        String gender = scnr.nextLine();
        // get monkey's age and assign value
        System.out.println("What is the monkey's age?");
        String age = scnr.nextLine();
        //get monkey's weight and assign value
        System.out.println("What is the monkey's weight?");
        String weight = scnr.nextLine();
        // get monkey's acquisition date and assign value
        System.out.println("What is the monkey's acquisition date?");
        String acquisitionDate = scnr.nextLine();
        // get monkey's acquisition country and assign value
        System.out.println("What is the monkey's acquisition country?");
        String acquisitionCountry = scnr.nextLine();
        // get monkey's training status and assign value
        System.out.println("What is the monkey's training status?");
        String trainingStatus = scnr.nextLine();
        // get if monkey is reserved and assign value
        System.out.println("Is this monkey reserved?");
        boolean reserved = scnr.nextBoolean();
        // get country monkey is serviced in and assign value
        System.out.println("Which country is the monkey in service");
        String inServiceCountry = scnr.nextLine();
        // get monkey's tail length and assign value
        System.out.print("What is the monkey's tail length");
        String tailLength = scnr.nextLine();
        // get monkey's height and assign value
        System.out.print("What is the monkey's height");
        String height = scnr.nextLine();
        // get monkey's body length and assign value
        System.out.print("What is the monkey's body length");
        String bodyLength = scnr.nextLine();

        // creates new monkey object, includes data for attributes
        Monkey monkey = new Monkey(name, gender, age, weight, acquisitionDate, acquisitionCountry, trainingStatus,
                                   reserved, inServiceCountry, tailLength, height, bodyLength, species);
        monkeyList.add(monkey); // add new monkey to Monkey ArrayList
        System.out.println("This monkey has been added to the Monkey List");
    }
    // reserveAnimal method
    public static void reserveAnimal(Scanner scnr) {
        // get animal type
        System.out.println("Would you like to reserve a dog or a monkey?");
        String animalType = scnr.nextLine();
        // get country
        System.out.println("Which country will the " + animalType + " be serving in?");
        String serviceLocation = scnr.nextLine(); // correct variable??

        // if animal type is dog
        if (animalType.equalsIgnoreCase("dog")) {
            // search dog ArrayList for a dog that matches serviceLocation of country entered.
            for (Dog dog : dogList) {
                // if service location matches country and not reserved
                if (dog.getInServiceLocation().equalsIgnoreCase(serviceLocation) && !dog.getReserved()) {
                    dog.setReserved(true);                     // set reserved to true
                    dog.setInServiceCountry(serviceLocation);  // set inServiceCountry to serviceLocation
                    // output found message to user
                    System.out.println(dog.getName() + " has been reserved.");
                    return;

                }
            }
        }
        // if animal type is monkey
        else {
            // search monkey ArrayList for a monkey that matches service location of country entered
            for (Monkey monkey : monkeyList) {
                // if service location matches country and not reserved
                if (monkey.getInServiceLocation().equalsIgnoreCase(serviceLocation) && !monkey.getReserved()) {
                    monkey.setReserved(true);                     // set reserved to true
                    monkey.setInServiceCountry(serviceLocation);  // set inServiceCountry to serviceLocation
                    System.out.println(monkey.getName() + " has been reserved.");
                    return;
                }
            }
        }
    }

    // printAnimals method
    public static void printAnimals(String printAnimals) {
        switch (printAnimals) {
            case "4":  // if user enters 4, print all dogs
                System.out.println("All dogs: ");
                // output all dogs in dogList
                for (Dog dog : dogList) {
                    System.out.println(dog);
                }
                break;
            case "5":  // if user enters 5, print all monkeys
                System.out.println("All monkeys: ");
                // output all monkeys in monkeyList
                for (Monkey monkey: monkeyList) {
                    System.out.println(monkey);
                }
                break;
            case "6":  // if user enters 6, print all animals
                // determine and print all available dogs
                System.out.println("All available animals: ");
                for (Dog dog : dogList) {
                    if (!dog.getReserved()) {
                        System.out.println(dog);
                    }
                }
                // determine and print all available monkeys
                for (Monkey monkey : monkeyList) {
                    if (!monkey.getReserved()) {
                        System.out.println(" ");
                        System.out.println(monkey);
                    }
                }
                System.out.println(" ");
                System.out.println(" ");

                System.out.println("All reserved animals: ");
                // determine and print all reserved dogs
                for (Dog dog : dogList) {
                    if (dog.getReserved()) {
                        System.out.println(" ");
                        System.out.println(dog);
                    }
                }
                // determine and print all reserved monkeys
                for (Monkey monkey : monkeyList) {
                    if (monkey.getReserved()) {
                        System.out.println(" ");
                        System.out.println(monkey);
                    }
                }
                break;
            default:
                System.out.println("Invalid input for printAnimals.");  // user validation

        }
    }
}