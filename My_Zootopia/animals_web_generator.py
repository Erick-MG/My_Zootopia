import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

def load_html(template_path):
    with open(template_path, "r") as file:
        return file.read()

def user_input_animal(animal_data):
    output = ''
    for animal_dict in animal_data:
        output += '<li class="cards__item">\n'
        output += f"<div class='card__title'> {animal_dict['name']}</div>\n"
        output += f"<strong>Diet:</strong> {animal_dict['characteristics']['diet']}<br/>\n"
        output += f"<strong>Location:</strong> {animal_dict['locations'][0]}<br/>\n"
        if "type" in animal_dict["characteristics"]:
            output += f"<strong>Type:</strong> {animal_dict['characteristics']['type']}<br/>\n"
        output += '</li>\n'
    return output

def write_html(output_path, replace_html):
    with open(output_path, "w") as file:
        file.write(replace_html)

def main():
    animals_data = load_data("animals_data.json")
    html_template = load_html("animals_template.html")
    animal_html = user_input_animal(animals_data)

    replace_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animal_html)
    write_html("animals.html", replace_html)

    print("Animals.html has been successfully generated!")

if __name__ == "__main__":
    main()