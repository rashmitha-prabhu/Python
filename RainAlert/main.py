import requests

api_key = "6dcdd109c0854b4760a71b3c72001bce"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
LATITUDE = 13.355498
LONGITUDE = 74.810292

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

data = requests.get(OWM_endpoint, params=weather_params)
data.raise_for_status()

weather_data = data.json()
weather_12hrs = weather_data['hourly'][:12]

will_rain = False

for hour in weather_12hrs:
    condition = hour['weather'][0]['id']
    if condition < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
