import os
separator = "="

def load_properties():
    with open('configuration.properties') as f:
        for line in f:
            if line.startswith("#"): # A comment
                continue
            if separator in line:
                # Find the name and value by splitting the string
                name, value = line.split(separator, 1)

                # Set environment variable
                os.environ[name.strip()] = value.strip()
    print("Config Loaded")