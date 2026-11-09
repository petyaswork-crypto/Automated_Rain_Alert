import requests
from twilio.rest import Client

# OpenWeatherMap API endpoint for the 5-day / 3-hour forecast
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# Your personal API key for OpenWeatherMap
api_key = "your personal api key"

# Your Twilio credentials (used to send the WhatsApp message)
account_sid = "your personal account sid"
auth_token = "your personal auth token"

# Your location coordinates
MY_LAT = "your latitude" # int
MY_LONG = "your longitude" # int

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4, # next 12 hours (4 × 3-hour forecast steps)
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    # Codes < 700 mean precipitation (rain, drizzle, snow, thunderstorm)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_="whatsapp:+14155238886", # Twilio WhatsApp sandbox number
        to="whatsapp:your phone number",
    )

    print(message.status)