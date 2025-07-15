import requests
import os       
from dotenv import load_dotenv
import json

load_dotenv()

API_KEY = os.getenv("WEATHER_KEY")


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    return f"Temperature in {city} is {data['main']['temp']:.0f}°C"


if __name__ == "__main__":
    print(get_weather("Krapkowice"))