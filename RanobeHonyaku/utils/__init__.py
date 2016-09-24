import json

# Reads our intial setup file
with open("./setup.json") as file:
    setup_file = json.load(file)

# I need to make this better
apps = []
