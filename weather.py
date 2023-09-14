def get_weather_data(location):
    data = {
        "main": {
            "temp": 25.0,
            "humidity": 60,
        },
        "weather": [
            {
                "description": "clear sky",
            }
        ],
        "wind": {
            "speed": 3.5,
        },
    }
    return data

def display_weather(data):
    if data:
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("No weather data to display.")

def main():
    location = input("Enter a city name or zip code: ")

    weather_data = get_weather_data(location)

    if weather_data:
        display_weather(weather_data)

if __name__ == "__main__":
    main()
