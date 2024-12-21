from owm_key import owm_api_key
from getweatherdata import get_weather_data
import json

if __name__ == '__main__':
    # Пример городов
    cities = ["Moscow", "Chicago", "Dhaka"]

    for city in cities:
        print(f"Fetching weather data for {city}...")
        weather_data = get_weather_data(city, api_key=owm_api_key)

        if weather_data:
            print(json.dumps(json.loads(weather_data), indent=4, ensure_ascii=False))
        else:
            print(f"Failed to fetch weather data for {city}")
