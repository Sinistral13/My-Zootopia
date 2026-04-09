import json


def load_data(file_path):
  """Load a JSON file."""
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_animals_data(animals_data):
    """Print the animal data in a formatted manner."""
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        animal_type = animal.get("characteristics", {}).get("type")
        locations = animal.get("locations")

        animals_data_for_printing = {}
        if name is not None:
            animals_data_for_printing["Name"] = name
        if diet is not None:
            animals_data_for_printing["Diet"] = diet
        if locations is not None:
            animals_data_for_printing["Location"] = locations
        if animal_type is not None:
            animals_data_for_printing["Type"] = animal_type
        width = max(len(datatype) for datatype in animals_data_for_printing)
        for datatype, datavalue in animals_data_for_printing.items():
            print(f"{datatype:<{width}} : {datavalue}")
        print()


def main():
    animals_data = load_data('animals_data.json')
    print_animals_data(animals_data)
   
    
if __name__ == "__main__":
    main()