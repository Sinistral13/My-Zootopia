import json
import requests


def load_data(file_path):
  """Load a JSON file."""
  with open(file_path, "r") as handle:
    return json.load(handle)


def get_animal_name():
    """Prompt the user for an animal name."""
    while True:
        animal_name = input("Please enter an animal name:    ")
        if animal_name:
            return animal_name


def get_animal_from_api(animal_name="Fox"):
    """Load animal from API and store it as .json file."""
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": "RKsW2jtYaYDszFRA8SIukjJhp1ujBVANslLfZe1g"}
    data = requests.get(url, headers=headers).json()
    
    if not data:
        data = [{
            "name" : animal_name,
            "taxonomy" : "Not Found"    
                }]
    with open("animal_api.json", "w") as file:
        json.dump(data, file, indent=4)
        print("Website was successfully generated to the file animals.html")
        

def serialize_animal(animal_obj):
    """Create a formatted string with the data of an animal for printing."""
    output = ""
    
    name = animal_obj.get("name", {})
    if not name:
        output += f'<h2>An unexpected error occurred.</h2>'
    
    elif animal_obj.get("taxonomy") == "Not Found":
        output += f'<h2>The animal "{name}" does not exist in the database.</h2>'
    else:
        diet = animal_obj.get("characteristics",{}).get("type",{})
        animal_type = animal_obj.get("characteristics", {}).get("type",{})
        locations = animal_obj.get("locations")[0]

        animals_data_for_printing = {}

        if diet:
            animals_data_for_printing["Diet"] = diet
        if locations:
            animals_data_for_printing["Location"] = locations
        if animal_type:
            animals_data_for_printing["Type"] = animal_type        
        output += '<li class="cards__item">\n'
        
        for datatype, datavalue in animals_data_for_printing.items():
            output += (f"<strong>{datatype}</strong> : {datavalue}<br/>\n")
        
    return output


def print_animals_data(animals_data):
    """Create a formatted string with the data of all animals from animal_data for printing."""
    output = ""
    
    for animal in animals_data:
        output += serialize_animal(animal)
        
    return output
        
        
def get_html_template(html_file):
    """Load a .html file as a template."""
    with open(html_file, "r") as file:
        html_template = file.read()
    return html_template


def write_html_file(html_file, file_name):
    """Write a .html file with the chosen filename to directory."""
    with open(file_name, "w") as file:
        file.write(html_file)   


def replace_placeholder_in_template(template_html_file, placeholder, data_string):
    """Replace the placeholder in a template .html file with the data_string.
    Writes the new .html file to directory."""
    new_html_file = template_html_file.replace(placeholder, data_string)
    write_html_file(new_html_file, "animals.html") 


def main():
    animal_name = get_animal_name()
    get_animal_from_api(animal_name)
    animals_data = load_data("animal_api.json")
    animal_data_for_printing = print_animals_data(animals_data)
    html_file = get_html_template("animals_template.html")
    replace_placeholder_in_template(html_file, "__REPLACE_ANIMALS_INFO__",
    animal_data_for_printing)

   
if __name__ == "__main__":
    main()