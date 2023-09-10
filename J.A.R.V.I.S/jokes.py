import requests


class jokes:
    # Returns a joke
    def get_joke():
        joke = requests.get("https://official-joke-api.appspot.com/random_joke").json()
        return joke
