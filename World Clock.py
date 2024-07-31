import tkinter as tk
import requests
from datetime import datetime
import time
from dateutil import parser

def fetch_time_from_worldtimeapi(timezone):
    response = requests.get(f'http://worldtimeapi.org/api/timezone/{timezone}')
    data = response.json()
    datetime_str = data['datetime']
    datetime_obj = parser.isoparse(datetime_str)
    return datetime_obj.strftime('%H:%M:%S')

def update_time():
    # To update lpocal time
    local_time = time.strftime('%H:%M:%S')
    local_time_label.config(text=f"Local Time: {local_time}")

    # To Update selected timezone time
    selected_timezone = timezone_var.get()
    timezone_time = fetch_time_from_worldtimeapi(selected_timezone)
    timezone_time_label.config(text=f"{selected_timezone.split('/')[-1]} Time: {timezone_time}")

    root.after(1000, update_time)

# List of timzoens
timezones = {
    "New York (USA)": "America/New_York",
    "London (Europe)": "Europe/London",
    "Tokyo (Asia)": "Asia/Tokyo",
    "Sydney (Australia)": "Australia/Sydney",
    "Cape Town (Africa)": "Africa/Johannesburg",
    "Sao Paulo (South America)": "America/Sao_Paulo"
}

# Makes Window
root = tk.Tk()
root.title("World Clock")

# Create labels for local time and selected timezone time
local_time_label = tk.Label(root, font=('Helvetica', 24), fg='black')
local_time_label.pack(pady=20)

timezone_time_label = tk.Label(root, font=('Helvetica', 24), fg='black')
timezone_time_label.pack(pady=20)

# Variable to store the timezone
timezone_var = tk.StringVar(root)
timezone_var.set("America/New_York") 

# Create an OptionMenu for selecting timezone
timezone_menu = tk.OptionMenu(root, timezone_var, *timezones.values())
timezone_menu.pack(pady=20)

# Starts the time clock
update_time()

# Main loop
root.mainloop()