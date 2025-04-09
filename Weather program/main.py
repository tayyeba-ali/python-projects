import requests

API_Key = 'fd894ec3f547cc17dc721b1c029454c7'

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            print(f"\n📍 Weather in {data['name']}, {data['sys']['country']}:")
            print(f"🌡️ Temperature     : {data['main']['temp']}°C")
            print(f"🥵 Feels Like      : {data['main']['feels_like']}°C")
            print(f"🌤️ Weather         : {data['weather'][0]['description'].title()}")
            print(f"💧 Humidity        : {data['main']['humidity']}%")
            print(f"💨 Wind Speed      : {data['wind']['speed']} m/s")
        else:
            print(f"\n❌ Error: {data['message'].capitalize()}")

    except requests.exceptions.RequestException as e:
        print("\n⚠️ Network error occurred:", e)

if __name__ == "__main__":
    city = input("🧭 Enter the city name: ")
    get_weather(city)
