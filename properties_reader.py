separator = "="


def get_properties_dict():
    config_dict = {}
    with open('configuration.properties') as f:
        for line in f:
            if separator in line:

                # Find the name and value by splitting the string
                name, value = line.split(separator, 1)

                # Assign key value pair to dict
                # strip() removes white space from the ends of strings
                config_dict[name.strip()] = value.strip()
    print("Config Loaded: " + str(config_dict))
    return config_dict