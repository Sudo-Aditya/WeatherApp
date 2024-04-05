import json
import pyttsx3
import requests

engine = pyttsx3.init()

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=5813c28680c241f5b9652910240504&q={city}"

r= requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
temp = wdic["current"]["temp_c"]
print(temp)

engine.say(f"The current weather in {city} is {temp} degrees")
engine.runAndWait()