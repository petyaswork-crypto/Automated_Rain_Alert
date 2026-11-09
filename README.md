# ☔ Automated Rain Alert

Hello! This is my small Python script that checks the weather forecast for your location and 
sends you a WhatsApp message if rain is expected in the next 12 hours — so you never leave home without an umbrella.


##  How It Works

1. The app fetches a 12-hour weather forecast from OpenWeatherMap using your own coordinates.

2. It checks the weather condition codes — anything below 700 means rain, drizzle, snow or thunderstorm.

3. If rain is detected, the app sends a WhatsApp message via Twilio with a reminder to bring an umbrella.

4. The Twilio message status (queued, sent, delivered, etc.) is printed in the end.


## Getting Your Credentials

### OpenWeatherMap API key

1. Sign up at openweathermap.org.

2. Go to API keys in your account dashboard.

3. Copy your key into api_key.

Note: new keys can take up to ~2 hours to activate.

### Twilio account SID and auth token

1. Sign up at twilio.com.

2. From the Twilio Console, copy your Account SID and Auth Token.

3. Enable the WhatsApp Sandbox under Messaging → Try it out → Send a WhatsApp message.

4. Send the sandbox join code from your WhatsApp to +1 415 523 8886 — this "opts in" your number, so Twilio can message you.


## Credits

Inspired by Day 35 of the course
"100 Days of Code: The Complete Python Pro Bootcamp".

The project idea, structure, and learning path came from the course.
The code in this repository was written by me as I followed along,
and I have added my own comments and tweaks along the way.

##  License

The project is free to use and change.
OpenWeatherMap and Twilio have their own terms of service — review them before any non-personal use.