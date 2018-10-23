from geopy.geocoders import Nominatim
from geopy.distance import geodesic

import http.client, urllib, base64, json
import requests, xml.etree.ElementTree as ET 

print("Welcome to Martian Health.")

# Call the Text Translate API
def translate(input):
    translateapi_key = '249cb975a60a464a9852b61510176146'

    authentication_url = 'https://api.cognitive.microsoft.com/sts/v1.0/issueToken'
    authentication_headers = {'Ocp-Apim-Subscription-Key': translateapi_key}
    authentication_token = requests.post(authentication_url, headers=authentication_headers).text
    translate_url = 'https://api.microsofttranslator.com/v2/http.svc/Translate'
    params = {
        'appid': 'Bearer '+ authentication_token, 
        'text': input,
        'to': "ru"   # language to be used for translation
    } 

    translate_headers = {'Accept': 'application/xml'}
    translate_response = requests.get(translate_url, params=params, headers=translate_headers) 
    caption_translation = ET.fromstring(translate_response.text.encode('utf-8')).text

    print ("Input (translated) >> " + caption_translation)

bloodpressure = int(input("This is the blood pressure: "))
oxylevel = int(input("This is the blood oxygen levels: "))
temperature = int(input("This is the body temperature: "))
radiation = int(input("This is the radiation level: "))
if bloodpressure < 80:
    bpmessage = "blood pressure is too low. get to shelter."
    translate(bpmessage)
    safe = False
else:
    bpmessage = "blood pressure is okay."
    translate(bpmessage)
    safe = True
if oxylevel < 90:
    oxmessage = "oxygen levels are too low. get to shelter."
    translate(oxmessage)
    safe = False
else:
    oxmessage = "oxygen levels are okay."
    translate(oxmessage)
    safe = True
if temperature > 60:
    tpmessage = "temperature is too high. get to shelter."
    translate(tpmessage)
    safe = False
elif temperature < 0:
    tpmessage = "temperature is too low. get to shelter."
    translate(tpmessage)
    safe = False
else:
    tpmessage = "temperature is okay."
    translate(tpmessage)
    safe = True
if radiation > 20:
    rdmessage = "radiation levels are too high. get to shelter."
    translate(rdmessage)
    safe = False
else:
    rdmessage = "radiation levels are okay."
    translate(rdmessage)
    safe = True

    


if safe == False:
  geolocator = Nominatim(user_agent="Martian Health")
  location = geolocator.geocode("70 Wilson St, London UK EC2A 2DB")
  your_location = (location.latitude, location.longitude)
  print("Your location is: ") #this would be in Russian too
  print(your_location)

  nearest_shelter = (41.499498, -81.695391)
  print("Your distance from the nearest shelter is...")
  distance = geodesic(your_location,nearest_shelter).miles
  print(distance, "miles")
else:
  print("You are safe...for the moment >:)")
  
