import json


def load_data(file_path):
  """Load a JSON file."""
  with open(file_path, "r") as handle:
    return json.load(handle)


def print_animals_data(animals_data):
    """Create a formatted string with the animal data for printing."""
    output = ""
    
    for animal in animals_data:
        name = animal.get("name")
        diet = animal.get("characteristics", {}).get("diet")
        animal_type = animal.get("characteristics", {}).get("type")
        locations = animal.get("locations")[0]

        animals_data_for_printing = {}
        if name is not None:
            animals_data_for_printing["Name"] = name
        if diet is not None:
            animals_data_for_printing["Diet"] = diet
        if locations is not None:
            animals_data_for_printing["Location"] = locations
        if animal_type is not None:
            animals_data_for_printing["Type"] = animal_type        

        for datatype, datavalue in animals_data_for_printing.items():
            output += (f"<strong>{datatype}</strong> : {datavalue}<br/>\n")
        output += "<br/>\n"
        
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


def replace_placeholder_in_html(html_file, placeholder, data):
    """Replace the placeholder with the data in a .html file.
    Writes the new .html file to directory."""
    new_html_file = html_file.replace(placeholder, data)
    write_html_file(new_html_file, "animal_data.html") 


def main():
    animals_data = load_data('animals_data.json')
    animal_data_for_printing = print_animals_data(animals_data)
    html_file = get_html_template("animals_template.html")
    replace_placeholder_in_html(html_file, "__REPLACE_ANIMALS_INFO__",
     animal_data_for_printing)
   
    
if __name__ == "__main__":
    main()