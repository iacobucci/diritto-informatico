import markdown
import vml_parser.vml as vml
import sys
import os

def get_item_and_level(elements, level=0):
    flat_elements = []

    for element in elements:
        flat_elements.append((element.name, level))

        if len(element.children) > 0:
            flat_elements.extend(get_item_and_level(
                element.children, level + 1))

    return flat_elements

# for every file in ./chapters sort numeric
for f in os.listdir('./chapters'):
    print("# " + f.split(".")[0].replace("_", " ").replace("-", " "))

    lines = open("./chapters/" + f).readlines()
    elements = vml.parse(lines)
    elements = list(get_item_and_level(elements))

    for element in elements:
        if element[1] == 0:
            print("## " + element[0])
        else:
            print("\t" * (element[1] - 1) + "- " + element[0])
