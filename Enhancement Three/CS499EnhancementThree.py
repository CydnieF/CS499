from crud import AnimalRescue
import json

# Connect to MongoDB with dataManager credentials
shelter = AnimalRescue(
    username="dataManager",
    password="managerpassword",
    host="127.0.0.1",
    port=27017,
    database="AnimalDB",
    collection="Animals"
)


# import JSON data into MongoDB, skipping duplicates
def import_json_data(file_path, role):
    with open(file_path, "r") as file:
        animal_data = json.load(file)
        inserted_ids = []
        for animal in animal_data:
            # define uniqueness criteria
            query = {
                "name": animal["name"],
                "type": animal["type"],
                "species": animal["species"],
                "acquisition_date": animal["acquisition_date"]
            }
            if not shelter.read(query, role):
                shelter.create(animal, role)
                inserted_ids.append(animal["name"])
        print(f"Inserted animals: {inserted_ids}" if inserted_ids else "No new animals added (duplicates skipped).")


# run the app
if __name__ == "__main__":
    # import JSON data
    import_json_data("animal_data.json", "dataManager")
