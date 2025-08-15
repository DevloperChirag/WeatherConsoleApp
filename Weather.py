import requests as requests
import re
import json as json

print("Temperature of your Location")
flag = True
while(flag):

    location = input("Enter place name:")
    if re.match(r'^[a-zA-Z\s]+$', location):  # match only alphanumeric chars and spaces

        url = f"https://api.weatherapi.com/v1/current.json?key=aac1a8882fe14b55b63162623242212&q={location}"
        response= requests.get(url)
        # Parse JSON response
        data = response.json()
        if "error" in data:{
            print(data["error"]["message"])
        }

        if "location" in data:
            {
            print(f"{data["current"]["temp_c"]}"+" Celsius updated at " + f"{data["current"]["last_updated"]}")
        }
        isExit = input("Do you want to exit ? Type Y or N")
        if isExit == "Y":
            break
        else:
            continue


    print("Please enter only alphabets")
