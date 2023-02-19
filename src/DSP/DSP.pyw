import tkinter as tk
import pytz
from datetime import datetime
import time

# Define timezones
LA = pytz.timezone('America/Los_Angeles')
NYC = pytz.timezone('America/New_York')
LONDON = pytz.timezone('Europe/London')
ISTANBUL = pytz.timezone('Europe/Istanbul')
CHINA = pytz.timezone('Asia/Shanghai')

# Get the user's time format preference
user_time_format = time.strftime('%H:%M:%S') == '00:00:00'

# Create a window
root = tk.Tk()
root.title("World Clocks")

# Create labels for displaying times
la_label = tk.Label(root, text="LA")
la_label.pack(side=tk.LEFT)
nyc_label = tk.Label(root, text="NYC")
nyc_label.pack(side=tk.LEFT)
london_label = tk.Label(root, text="London")
london_label.pack(side=tk.LEFT)
istanbul_label = tk.Label(root, text="Istanbul")
istanbul_label.pack(side=tk.LEFT)
china_label = tk.Label(root, text="China")
china_label.pack(side=tk.LEFT)

# Update the time labels
def update_time():
    la_time = datetime.now(LA).strftime('%I:%M:%S %p' if user_time_format else '%H:%M:%S')
    nyc_time = datetime.now(NYC).strftime('%I:%M:%S %p' if user_time_format else '%H:%M:%S')
    london_time = datetime.now(LONDON).strftime('%I:%M:%S %p' if user_time_format else '%H:%M:%S')
    istanbul_time = datetime.now(ISTANBUL).strftime('%I:%M:%S %p' if user_time_format else '%H:%M:%S')
    china_time = datetime.now(CHINA).strftime('%I:%M:%S %p' if user_time_format else '%H:%M:%S')
    
    la_label.config(text=la_time)
    nyc_label.config(text=nyc_time)
    london_label.config(text=london_time)
    istanbul_label.config(text=istanbul_time)
    china_label.config(text=china_time)
    
    root.after(1000, update_time) # Update every second

update_time()

# Run the program
root.mainloop()
