import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


# crear una function para  for loop con toda la info
def user_input_animal(animal_data):
  for animal_dict in animal_data:
    name = animal_dict["name"]
    diet = animal_dict["characteristics"]["diet"]
    locations = animal_dict["locations"][0]


    print(f"Name: {name}")
    print(f"Diet: {diet}")
    print(f"Location: {locations}")
    if "type" in animal_dict["characteristics"]:
      print(f"Type: {animal_dict["characteristics"]["type"]}")


def main():
    animals_data = load_data('animals_data.json')
    print(animals_data)
    user_input_animal(animals_data)


if __name__ == "__main__":
  main()