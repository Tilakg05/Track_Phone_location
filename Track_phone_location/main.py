import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import pycountry
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import region_code_for_number
from opencage.geocoder import OpenCageGeocode
import folium
import os


#if #os.path.exists("mylocation.html"):
  #os.remove("mylocation.html")
try:
  number = input("Enter Phone Number: ")
  pepnumbers = phonenumbers.parse(number)
  country = pycountry.countries.get(alpha_2=region_code_for_number(pepnumbers))
  location = country.name
  #print(location)
  print(carrier.name_for_number(phonenumbers.parse(number), "en"))
  print(location)
  Key = input("Entry Your API KEY:")
  geocoder = OpenCageGeocode(Key)
  query = str(location)
  results = geocoder.geocode(query)
  lat = results[0]['geometry']['lat']
  lng = results[0]['geometry']['lng']
  print(lat,lng)

  myMap = folium.Map(location=[lat , lng], zoom_start=20)
  folium.CircleMarker([lat,lng],popup=location).add_to(myMap)
  folium.Marker([lat,lng],popup=location).add_to(myMap)
  myMap.save("mylocation.html")
  #os.system("mylocation.html")
except:
    print("Missing or invalid number\nPlease enter your phone number with country code")
