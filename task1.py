import requests
import matplotlib.pyplot as plt

# Replace with your actual API key and city
API_KEY = "f3144e36d1ac0db1dfd81223d5642038"
CITY = "Dehradun"

# ✅ Use HTTPS instead of HTTP
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    response.raise_for_status()  # Raise an error for bad responses
    
    data = response.json()
    
    if data["cod"] == 200:
        print("Data fetched successfully!")
        
        # Extract relevant data
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        weather_description = data['weather'][0]['description']
        
        print(f"\nCity: {CITY}")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_description.capitalize()}")
        
        # ------------------ Plotting Section ------------------ #
        labels = ['Temperature', 'Feels Like']
        values = [temp, feels_like]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        
        # Bar chart
        ax1.bar(labels, values, color=['skyblue', 'salmon'])
        ax1.set_title(f'Current Temperature in {CITY}')
        ax1.set_ylabel('Temperature (°C)')
        ax1.set_ylim(min(values) - 5, max(values) + 5)
        
        # Pie chart for humidity
        humidity_labels = ['Humidity', 'Remaining']
        humidity_values = [humidity, 100 - humidity]
        ax2.pie(humidity_values, labels=humidity_labels, autopct='%1.1f%%', 
                startangle=90, colors=['teal', 'lightgrey'])
        ax2.set_title(f'Humidity in {CITY}')
        
        # Extra text
        fig.suptitle(f'Weather Dashboard for {CITY}', fontsize=16)
        fig.text(0.5, 0.9, f"Weather: {weather_description.capitalize()}",
                
                 ha='center', fontsize=12, style='italic')
        fig.text(0.5, 0.05, "This is a simple weather visualization dashboard.", 
                 ha='center', fontsize=10)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()
        
    else:
        print(f"Error: {data['message']}")

except requests.exceptions.HTTPError as errh:
    print(f"Http Error: {errh}")
except requests.exceptions.ConnectionError as errc:
    print(f"Error Connecting: {errc}")
except requests.exceptions.Timeout as errt:
    print(f"Timeout Error: {errt}")
except requests.exceptions.RequestException as err:
    print(f"Something went wrong: {err}")
