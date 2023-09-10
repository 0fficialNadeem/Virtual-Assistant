import requests


class Weather:
    def __init__(self) -> None:
        self.API_KEY = ""

    # Get weather information for a city
    def getWeather(self, city):
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.API_KEY}"
        ).json()
        str = f"In {city} it is {round(data['main']['temp']-273)} degrees celsius with some {data['weather'][0]['main']}"
        return str
