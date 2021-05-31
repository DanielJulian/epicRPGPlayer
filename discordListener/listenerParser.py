import re

def getLifeRemaining(text):
    regex = "[a-zA-Z0-9]*remaining HP is (.+?)/(.+?)"

    try:
        found = re.search(regex, text).group(1)
    except AttributeError:
        # Regex not found
        found = None

    return found
