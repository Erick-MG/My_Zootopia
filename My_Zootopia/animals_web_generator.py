import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_html(animals_template):
  with open(animals_template, "r") as file:
    return file.read()


def user_input_animal(animal_data):

    output = ''
    for animal_dict in animal_data:
        output += f"Name: {animal_dict["name"]}\n"
        output += f"Diet: {animal_dict["characteristics"]["diet"]}\n"
        output += f"Location: {animal_dict["locations"][0]}\n"
        if "type" in animal_dict["characteristics"]:
            output += f"Type: {animal_dict["characteristics"]["type"]}\n"
    return output

def write_html(replace_html):
    with open('animals.html', "w") as file:
        return file.write(replace_html)


def main():
    animals_data = load_data('animals_data.json')
    print(animals_data)
    user_input_animal(animals_data)
    html_data = load_html("animals_template.html")
    output = user_input_animal(animals_data)
    replace_html =  html_data.replace("__REPLACE_ANIMALS_INFO__", output)
    write_html(replace_html)

if __name__ == "__main__":
  main()