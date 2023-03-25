import requests
import datetime as dt
import customtkinter as CTk
from tkinter import *
import json
from tkinter import messagebox
import os
import subprocess

API_KEY = "6c55313b14fc0b07b3ea751d41103c12"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

with open("src/settings.json", 'r')as f:
    settings = json.load(f)
with open("src/user_settings.json", 'r')as f:
    user_settings = json.load(f)
version = settings['version']
username = user_settings['username']
theme = settings['theme']

if not os.path.exists('src/DSP/tasks.json'):
    with open('src/DSP/tasks.json', 'w') as file:
        json.dump([], file)

if not os.path.exists('src/DSP/reminders.json'):
    with open('src/DSP/reminders.json', 'w') as file:
        json.dump([], file)

global zip_code
zip_code = user_settings['zip_code']

if theme == 'Dark':
    CTk.set_appearance_mode("Dark")
else:
    CTk.set_appearance_mode("Light")

CTk.set_default_color_theme("blue")
app = CTk.CTk()
app.geometry("1200x690")
app.wm_iconbitmap("assets/logos/DSP-logo.ico")
app.title(f"Daily Sneak Peek v{version}")
app.bind("<Return>", lambda _: update_zip_code_button.invoke())
app.bind("<Escape>", lambda _: cancel_change_button.invoke())
app.resizable(False, False)
global show_12_hour_button
global twlve_hour_time
### START OF GLOBAL FUNCTIONS ###


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


def toggle_theme():
    with open("src/settings.json", "r")as f:
        settings = json.load(f)
    theme = settings['theme']
    if theme == 'Dark':
        CTk.set_appearance_mode("Light")
        toggle_theme_button.configure(text="\u26ee")
        settings['theme'] = 'Light'
    if theme == 'Light':
        CTk.set_appearance_mode("Dark")
        toggle_theme_button.configure(text="\u2600")
        settings['theme'] = 'Dark'
    with open('src/settings.json', 'w') as f:
        json.dump(settings, f)

### END OF GLOBAL FUNCTIONS ###

### START OF WEATHER FUNCTIONS ###


def update_zip_code():
    global change_zip_code_entry
    change_zip_code_entry = CTk.CTkEntry(app, width=230)
    change_zip_code_entry.focus()
    change_zip_code_entry.place(x=420, y=40)
    global update_zip_code_button
    update_zip_code_button = CTk.CTkButton(
        app, text="\u2714", width=5, font=("Arial", 20), command=save_zip_code)
    update_zip_code_button.place(x=660, y=40)
    global cancel_change_button
    cancel_change_button = CTk.CTkButton(app, width=5, text="\u274C", font=(
        "Arial", 20), command=cancel_zip_code_changes)
    cancel_change_button.place(x=700, y=40)


def save_zip_code():
    global zip_code
    zip_code = change_zip_code_entry.get()
    with open("src/user_settings.json", "r+") as json_file:
        data = json.load(json_file)
    if not zip_code:
        zip_code = '00000'
        data['zip_code'] = zip_code
        welcome_label.configure(
            text=f"Welcome to your Daily Sneak Peek! Your zip code is set to {zip_code}")
        cancel_zip_code_changes()
    else:
        data["zip_code"] = zip_code
        welcome_label.configure(
            text=f"Welcome to your Daily Sneak Peek! Your zip code is set to {zip_code}")
        cancel_zip_code_changes()
    with open('src/user_settings.json', 'w') as f:
        json.dump(data, f)
    weather_info.configure(text="")


def cancel_zip_code_changes():
    update_zip_code_button.destroy()
    change_zip_code_entry.destroy()
    cancel_change_button.destroy()


def get_weather():
    global show_12_hour_button

    def check_and_convert_time(sunrise_time, sunset_time):
        global twlve_hour_time
        twlve_hour_time = CTk.CTkLabel(app, text='', font=("Arial", 15))
        twlve_hour_time.place(x=10, y=420)
        if sunrise_time.strftime('%H:%M') == sunrise_time.strftime('%I:%M %p') and sunset_time.strftime('%H:%M') == sunset_time.strftime('%I:%M %p'):
            twlve_hour_time.configure(text='Already 12 formats')
        else:
            sunrise_12hr = sunrise_time.strftime('%I:%M %p')
            sunset_12hr = sunset_time.strftime('%I:%M %p')
            twlve_hour_time.configure(
                text=f"\nSunrise time (12 hour format): {sunrise_12hr} \n\nSunset time (12 hour format): {sunset_12hr}")
    global zip_code
    try:
        request_url = BASE_URL + "?appid="+API_KEY+"&zip="+zip_code
        response = requests.get(request_url).json()
        state_response = requests.get(
            f'http://api.zippopotam.us/us/{zip_code}')
        data = state_response.json()
        state = data['places'][0]['state']
        city_name = response['name']
        temp_kelvin = response['main']['temp']
        temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(
            temp_kelvin)
        feels_like_kelvin = response["main"]['feels_like']
        feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(
            feels_like_kelvin)
        wind_speed = response['wind']['speed']
        humidity = response["main"]['humidity']
        description = response["weather"][0]["description"]
        sunrise_time = dt.datetime.utcfromtimestamp(
            response['sys']['sunrise']+response['timezone'])
        sunset_time = dt.datetime.utcfromtimestamp(
            response['sys']['sunset']+response['timezone'])
        weather_info.configure(
            text=f"""Weather in {city_name}, {state}: \n\n General Weather Description: {description}\n\n Temperature: {temp_fahrenheit: .2f}°F or {temp_celsius: .2f}°C \n\nTemperature feels like: {feels_like_fahrenheit: .2f}°F
             or {feels_like_celsius: .2f}°C\n\nHumidity: {humidity}%\n\nWind Speed: {wind_speed}m/s\n\nSun rises: at {sunrise_time} local time\n\nSun sets: at {sunset_time} local time""")
        show_12_hour_button = CTk.CTkButton(
            app, text='Show In 12-hour', command=lambda: check_and_convert_time(sunrise_time, sunset_time))
        show_12_hour_button.place(x=40, y=390)
    except:
        weather_info.configure(
            text="Something went wrong...\nPlease try again later.")


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahreinheit = celsius * (9/5) + 32
    return celsius, fahreinheit


def clear_weather_info():
    confirm_clear = messagebox.showinfo(
        'Confirm Clear', 'Are you sure you would like to clear weather info?')
    if confirm_clear:
        weather_info.configure(text='')
        show_12_hour_button.destroy()
        twlve_hour_time.configure(text='')

### END OF WEATHER FUNCTIONS ###

### START OF TODOS FUNCTIONS ###


if os.path.getsize('src/DSP/tasks.json') == 0:
    tasks = []
else:
    with open('src/DSP/tasks.json', 'r') as file:
        tasks = json.load(file)


def save_tasks():
    with open("src/DSP/tasks.json", "w") as file:
        json.dump(tasks, file)


def load_tasks():
    global tasks
    try:
        with open("src/DSP/tasks.json", "r")as file:
            tasks = json.load(file)
            create_task_labels()
    except:
        pass


def add_task():
    task = todo_entry.get()
    if task == "":
        pass
    else:
        task = todo_entry.get()
        tasks.append(task)
        with open('src/DSP/tasks.json', 'w') as file:
            json.dump(tasks, file)
        create_task_labels()
        todo_entry.delete(0, END)


def create_task_labels():
    for i, task in enumerate(tasks):
        tasklabel = CTk.CTkLabel(app, text=task)
        tasklabel.place(x=370, y=120+(i+1)*30)
        tasklabels.append(tasklabel)


def delete_all_tasks():
    confirm_clear = messagebox.showinfo(
        'Confirm Clear', 'Are you sure you would like to clear your to-do list?')
    if confirm_clear:
        for tasklabel in tasklabels:
            tasklabel.destroy()
        tasks.clear()
        tasklabels.clear()
        with open("src/DSP/tasks.json", "w") as f:
            json.dump([], f)
### END OF TODOS FUNCTIONS ###

### START OF REMINDERS FUNCTIONS ###


if os.path.getsize('src/DSP/reminders.json') == 0:
    reminders = []
else:
    with open('src/DSP/reminders.json', 'r') as file:
        reminders = json.load(file)


def save_reminders():
    with open("src/DSP/reminders.json", "w") as file:
        json.dump(reminders, file)


def load_reminders():
    global reminders
    try:
        with open("src/DSP/reminders.json", "r")as file:
            reminders = json.load(file)
            create_reminder_labels()
    except:
        pass


def add_reminder():
    reminder = reminder_entry.get()
    if reminder == "":
        pass
    else:
        reminder = reminder_entry.get()
        reminders.append(reminder)
        with open('src/DSP/reminders.json', 'w') as file:
            json.dump(reminders, file)
        create_reminder_labels()
        reminder_entry.delete(0, END)


def create_reminder_labels():
    for i, reminder in enumerate(reminders):
        reminderlabel = CTk.CTkLabel(app, text=reminder)
        reminderlabel.place(x=760, y=120+(i+1)*30)
        reminderlabels.append(reminderlabel)


def delete_all_reminders():
    confirm_clear = messagebox.showinfo(
        'Confirm Clear', 'Are you sure you would like to clear all reminders?')
    if confirm_clear:
        for reminderlabel in reminderlabels:
            reminderlabel.destroy()
        reminders.clear()
        reminderlabels.clear()
        with open("src/DSP/reminders.json", "w") as f:
            json.dump([], f)


### END OF REMINDERS FUNCTIONS ###


### START OF WEATHER ELEMENTS ###
toggle_theme_button = CTk.CTkButton(app, text="\u2600", font=(
    "Arial", 18), width=3, command=toggle_theme)
toggle_theme_button.place(x=240, y=590)
welcome_label = CTk.CTkLabel(
    app, text=f"Welcome to your Daily Sneak Peek!", font=("Arial", 20))
zipcode_label = CTk.CTkLabel(
    app, text=f"Your zip code is set to {zip_code}", font=("Arial", 20))
welcome_label.place(x=10, y=0)
zipcode_label.place(x=10, y=40)
change_zip_code_button = CTk.CTkButton(
    app, text="Change", font=("Arial", 22), command=update_zip_code)
change_zip_code_button.place(x=270, y=40)

outside_US_label = CTk.CTkLabel(
    app, text="Outside the U.S.?", font=("Arial", 22))
outside_US_label.place(x=850, y=10)
international_button = CTk.CTkButton(
    app, text="International", font=("Arial", 22))
international_button.place(x=1040, y=10)

get_weather_button = CTk.CTkButton(
    app, text="Get Today's Weather", font=("Arial", 20), command=get_weather)
get_weather_button.place(x=30, y=100)
weather_info = CTk.CTkLabel(app, text="", font=("Arial", 15))
weather_info.place(x=5, y=150)

clear_weather_info_button = CTk.CTkButton(
    app, text='Clear All', font=("Arial", 20), command=clear_weather_info)
clear_weather_info_button.place(x=70, y=590)
### END OF WEATHER ELEMENTS ###


### START OF TODOS ELEMENTS ###
tasklabels = []
taskbuttons = []
load_tasks()
create_task_labels()

todo_top_label = CTk.CTkLabel(
    app, text="Today's To-Dos", font=("Arial", 20))
todo_top_label.place(x=370, y=100)

todo_entry = CTk.CTkEntry(app, width=260)
todo_entry.place(x=370, y=160)
add_todo_button = CTk.CTkButton(
    app, text="+", font=("Arial", 20), width=40, command=add_task)
add_todo_button.place(x=650, y=160)

delete_all_button = CTk.CTkButton(app, text="Delete All To-Dos", font=(
    "Arial", 20), width=40, command=delete_all_tasks)
delete_all_button.place(x=370, y=640)

### END OF TODOS ELEMENTS ###


### START OF REMINDERS ELEMENTS ###
reminderlabels = []
reminderbuttons = []
load_reminders()
create_reminder_labels()

reminders_top_label = CTk.CTkLabel(
    app, text="All-Time Reminders", font=("Arial", 20))
reminders_top_label.place(x=760, y=100)
reminder_entry = CTk.CTkEntry(app, width=260)
reminder_entry.place(x=760, y=160)
add_reminder_button = CTk.CTkButton(
    app, text="+", font=("Arial", 20), width=40, command=add_reminder)
add_reminder_button.place(x=1040, y=160)

delete_all_reminders_button = CTk.CTkButton(app, text="Delete All Reminders", font=(
    "Arial", 20), width=40, command=delete_all_reminders)
delete_all_reminders_button.place(x=760, y=640)
### END OF REMINDERS ELEMENTS ###


back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", font=("Arial", 20), command=back_to_desky)
back_to_desky_button.place(x=5, y=640)
exit_button = CTk.CTkButton(
    app, text="Exit", font=("Arial", 20), command=exit)
exit_button.place(x=190, y=640)
app.mainloop()
