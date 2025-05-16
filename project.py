import requests
import tkinter as tk
from tkinter import messagebox

# Replace with your own OpenWeatherMap API key
API_KEY = "your_openweathermap_api_key"

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"].capitalize()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"City: {city_name}, {country}\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        output_label.config(text=result)
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found or API error.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_weather():
    city = city_entry.get()
    if city:
        get_weather(city)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# GUI Setup
root = tk.Tk()
root.title("Weather Forecast Dashboard")
root.geometry("400x300")
root.config(bg="lightblue")

tk.Label(root, text="Enter City:", bg="lightblue", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=search_weather, font=("Arial", 12), bg="skyblue").pack(pady=10)
output_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue", justify="left")
output_label.pack(pady=10)

root.mainloop()
