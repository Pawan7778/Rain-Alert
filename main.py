import requests
from twilio.rest import Client
import os

api_key = "c15b5e635985c41c0f2f9a3f2a9cfacf"
MY_LAT = 24.176250
MY_LONG = 85.887863
account_sid = "AC938365b63840d7c37099cc46c6de77eb"
auth_token = "e45cdd5f45087a1de901ce80d7cd5543"



response = requests.get(url = f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LONG}&exclude=current,minutely,daily&appid={api_key}")
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][0:12]

will_rain = False
for hour_data in weather_slice:
   condition_code =  hour_data["weather"][0]["id"]
   if int(condition_code) < 700:
       will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☔☔",
                     from_='+17196244591',
                     to='+918789267173'
                 )
    
    print(message.status)