import requests
import json

url = "https://api.weatherapi.com/v1/current.json"
apiKey = "7a3baefaf8e44c098c892850241512"

location = input("Enter your location --> ")

response = requests.get(url, params={
    "key": apiKey,
    "q": location
})

# Check if the response is OK
if response.status_code == 200:
    try:
        result = response.json()
        
        # Debug: print the full response to see its structure
        print(json.dumps(result, indent=4))
        
        # Extract data if the structure is correct
        city = result["location"]["name"]
        forecast = result["current"]["temp_c"]
        text = result["current"]["condition"]["text"]

        print(f"In {city}, the forecast is {forecast}°C and the condition is {text}.")
    
    except KeyError:
        print("Error: The expected data is not present in the response.")
    except requests.exceptions.JSONDecodeError:
        print("Error: Could not decode JSON response.")
else:
    print(f"Error: Received status code {response.status_code}")
    print(response.text)  # Print the raw response for debugging
