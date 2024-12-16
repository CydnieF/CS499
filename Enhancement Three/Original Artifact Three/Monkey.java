public class Monkey extends RescueAnimal{  // creates class Monkey which extends RescueAnimal
    // private instance variables
    private String tailLength;
    private String height;
    private String bodyLength;
    private String species;

    // valid monkey species
    public final static String[] validSpecies = {"Capuchin", "Guenon", "Macaque", "Marmoset", "Squirrel Monkey", "Tamarin"};

    // default constructor
    public Monkey(){
        // initialize instance variables
        tailLength = "";
        height = "";
        bodyLength = "";
        species = "";
    }
    // constructor with parameters, takes arguments for every Monkey attribute
    public Monkey(String name, String gender, String age,
    String weight, String acquisitionDate, String acquisitionCountry,
    String trainingStatus, boolean reserved, String inServiceCountry,
    String tailLength, String height, String bodyLength, String species) {
        // allow to send data to relative set method
        setName(name);
        setGender(gender);
        setAge(age);
        setWeight(weight);
        setAcquisitionDate(acquisitionDate);
        setAcquisitionLocation(acquisitionCountry);
        setTrainingStatus(trainingStatus);
        setReserved(reserved);
        setInServiceCountry(inServiceCountry);

        setTailLength(tailLength);
        setHeight(height);
        setBodyLength(bodyLength);
        setSpecies(species);

    }

    public String getTailLength() {  // accessor
        return tailLength;           // return value
    }

    public void setTailLength(String tailLength) {  // mutator
        this.tailLength = tailLength;
    }

    public String getHeight() {  // accessor
        return height;           // return value
    }

    public void setHeight(String height) {  // mutator
        this.height = height;
    }

    public String getBodyLength() {  // accessor
        return bodyLength;           // return value
    }

    public void setBodyLength(String bodyLength) {  // mutator
        this.bodyLength = bodyLength;
    }

    public String getSpecies() {  // accessor
        return species;           // return value
    }

    public void setSpecies(String species) {  // mutator
        this.species = species;
    }
    // used to print animal list
    @Override
    public String toString() {
        return " Monkey Name: " + getName() + ", Training Status: " + getTrainingStatus() + ", Service Location: " +
                getInServiceLocation() + ", Reserved: " + getReserved();
    }
}
