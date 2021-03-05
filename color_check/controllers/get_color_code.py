# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.

import json

def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.

    with open ("data/css-color-names.json" , "r") as read_json:
        deserialized_json = json.load(read_json)

    # hex_code = '#0000ff'

    # print("hi")

    #return hex_code
    if color_name in deserialized_json:
        return deserialized_json[color_name]
    else:
        return None



