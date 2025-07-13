import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os
import logging

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Ładowanie zmiennych środowiskowych
load_dotenv()

# Pobieranie konfiguracji
config = {
    "openweather_api_key": os.getenv("OPENWEATHER_API_KEY"),
    "twilio_account_sid": os.getenv("TWILIO_ACCOUNT_SID"),
    "twilio_auth_token": os.getenv("TWILIO_AUTH_TOKEN"),
    "phone_number": os.getenv("MY_PHONE_NUMBER"),
    "location": {
        "lat": float(os.getenv("LOCATION_LAT", "50.332133")),
        "lon": float(os.getenv("LOCATION_LON", "18.892080"))
    }
}

# Inicjalizacja klienta Twilio
client = Client(config["twilio_account_sid"], config["twilio_auth_token"])

def get_weather_forecast():
    """Pobiera prognozę pogody z OpenWeatherMap API."""
    params = {
        "lat": config["location"]["lat"],
        "lon": config["location"]["lon"],
        "appid": config["openweather_api_key"],
        "cnt": 6,
        "units": "metric"  # Dodane dla temperatury w °C
    }

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast",
            params=params
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Błąd podczas pobierania danych pogodowych: {e}")
        raise

def analyze_weather(data):
    """Analizuje dane pogodowe i generuje komunikat."""
    result = []
    for hour in data['list']:
        condition_id = int(hour['weather'][0]['id'])
        time = hour['dt_txt']
        desc = hour['weather'][0]['description']
        temp = hour['main']['temp']
        
        alert = "Weź parasol! ☔" if condition_id < 700 else "Nie potrzebujesz parasola ☀️"
        result.append(
            f"{time}: {alert}\n"
            f"   - Warunki: {desc}\n"
            f"   - Temperatura: {temp}°C\n"
        )
    return "\n".join(result)

def send_whatsapp_message(body):
    """Wysyła wiadomość przez WhatsApp."""
    try:
        message = client.messages.create(
            body=body,
            from_="whatsapp:+14155238886",
            to=f"whatsapp:{config['phone_number']}",
        )
        logging.info(f"Wiadomość wysłana! SID: {message.sid}")
    except Exception as e:
        logging.error(f"Błąd wysyłania wiadomości: {e}")
        raise

def main():
    logging.info("Rozpoczynanie sprawdzania pogody...")
    try:
        weather_data = get_weather_forecast()
        analysis = analyze_weather(weather_data)
        message_body = (
            f"Prognoza pogody dla {config['location']['lat']},{config['location']['lon']}:\n\n"
            f"{analysis}"
        )
        send_whatsapp_message(message_body)
    except Exception as e:
        logging.critical(f"Błąd w działaniu aplikacji: {e}")

if __name__ == "__main__":
    main()