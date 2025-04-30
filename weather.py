import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set Seaborn style
sns.set(style="darkgrid")

# Your OpenWeatherMap API key and city
API_KEY = "e6c76ccfad2809f24b578e0f28af5e28"
CITY = "Mumbai"  # Example city
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

# API parameters
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

# Fetch data from API
response = requests.get(BASE_URL, params=params)
data = response.json()

# Check API response
if data["cod"] != "200":
    print(f"Failed to fetch data: {data.get('message')}")
else:
    # Extract data
    times = [datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S") for entry in data["list"]]
    temperatures = [entry["main"]["temp"] for entry in data["list"]]
    humidity = [entry["main"]["humidity"] for entry in data["list"]]
    pressure = [entry["main"]["pressure"] for entry in data["list"]]

    # Create visualization dashboard with subplots
    plt.figure(figsize=(16, 10))

    # Temperature plot
    plt.subplot(3, 1, 1)
    sns.lineplot(x=times, y=temperatures, marker="o", color="tab:red")
    plt.title(f"Temperature Forecast for {CITY}")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)

    # Humidity plot
    plt.subplot(3, 1, 2)
    sns.lineplot(x=times, y=humidity, marker="s", color="tab:blue")
    plt.title(f"Humidity Forecast for {CITY}")
    plt.ylabel("Humidity (%)")
    plt.xticks(rotation=45)

    # Pressure plot
    plt.subplot(3, 1, 3)
    sns.lineplot(x=times, y=pressure, marker="^", color="tab:green")
    plt.title(f"Pressure Forecast for {CITY}")
    plt.ylabel("Pressure (hPa)")
    plt.xlabel("Time")
    plt.xticks(rotation=45)

    # Layout adjustment and display
    plt.tight_layout()
    plt.show()
