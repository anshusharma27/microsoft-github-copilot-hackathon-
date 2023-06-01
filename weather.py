import requests
import json

def get_weather(city_name):
    api_key = "5c1109abb18db33f9cd49688aa50a0b4"  # My OpenWeatherMap API key

    # API endpoint for current weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = json.loads(response.text)

        # Extracting relevant information from the API response
        description = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]

        # Converting temperature from Kelvin to Celsius
        temperature = round(temperature - 273.15, 2)

        # Printing the weather forecast
        print(f"Weather forecast for {city_name}:")
        print(f"Description: {description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")

    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except (KeyError, IndexError, json.JSONDecodeError) as err:
        print(f"Failed to parse weather data: {err}")


if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)


    