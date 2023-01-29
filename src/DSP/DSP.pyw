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

with open("settings.json", 'r')as f:
    settings = json.load(f)
version = settings['version']
username = settings['username']
theme = settings['theme']


if not os.path.exists('src/DSP/tasks.json'):
    with open('src/DSP/tasks.json', 'w') as file:
        json.dump([], file)

if not os.path.exists('src/DSP/reminders.json'):
    with open('src/DSP/reminders.json', 'w') as file:
        json.dump([], file)

global zip_code
zip_code = settings['zip_code']

if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

CTk.set_default_color_theme("blue")
app = CTk.CTk()
app.geometry("1200x600")
app.title("Daily Sneak Peek")
app.resizable(False, False)


def update_zip_code():
    global change_zip_code_entry
    change_zip_code_entry = CTk.CTkEntry(app, width=230)
    change_zip_code_entry.focus()
    change_zip_code_entry.place(x=580, y=50)
    global update_zip_code_button
    update_zip_code_button = CTk.CTkButton(
        app, text="\u2714", width=5, font=("Courier New", 20), command=save_zip_code)
    update_zip_code_button.place(x=820, y=50)
    global cancel_change_button
    cancel_change_button = CTk.CTkButton(app, width=5, text="\u274C", font=(
        "Courier New", 20), command=cancel_zip_code_changes)
    cancel_change_button.place(x=860, y=50)


def save_zip_code():
    global zip_code
    zip_code = change_zip_code_entry.get()

    with open("settings.json", "r+") as json_file:
        data = json.load(json_file)
        data["zip_code"] = zip_code
    with open('settings.json', 'w') as f:
        json.dump(data, f)
    zip_code = data['zip_code']
    if zip_code == '':
        error = messagebox.showinfo(
            title="Empty entry", message="Please enter a zip code.")
    else:
        welcome_label.configure(
            text=f"Welcome to your Daily Sneak Peek! Your zip code is set to {zip_code}")
        cancel_zip_code_changes()
    weather_info.configure(text="")


def cancel_zip_code_changes():
    update_zip_code_button.destroy()
    change_zip_code_entry.destroy()
    cancel_change_button.destroy()


def get_weather():
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
    except:
        weather_info.configure(
            text="Something went wrong...\nPlease try again later. \nCurrently only USA zip codes are supported.")


def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahreinheit = celsius * (9/5) + 32
    return celsius, fahreinheit


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
    for tasklabel in tasklabels:
        tasklabel.destroy()
    tasks.clear()
    tasklabels.clear()
    with open("src/DSP/tasks.json", "w") as f:
        json.dump([], f)


# reminders
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
    for reminderlabel in reminderlabels:
        reminderlabel.destroy()
    reminders.clear()
    reminderlabels.clear()
    with open("src/DSP/reminders.json", "w") as f:
        json.dump([], f)


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)

tasklabels = []
taskbuttons = []
reminderlabels = []
reminderbuttons = []

load_reminders()
create_reminder_labels()

load_tasks()
create_task_labels()

welcome_label = CTk.CTkLabel(
    app, text=f"Welcome to your Daily Sneak Peek! Your zip code is set to {zip_code}", font=("Courier New", 20))
welcome_label.place(x=0, y=0)
change_zip_code_button = CTk.CTkButton(
    app, text="Change", font=("Courier New", 22), command=update_zip_code)
change_zip_code_button.place(x=770, y=10)

get_weather_button = CTk.CTkButton(
    app, text="Get Today's Weather", font=("Courier New", 20), command=get_weather)
get_weather_button.place(x=30, y=60)
weather_info = CTk.CTkLabel(app, text="")
weather_info.place(x=5, y=110)

todo_top_label = CTk.CTkLabel(
    app, text="Today's To-Dos", font=("Courier New", 20))
todo_top_label.place(x=370, y=60)

todo_entry = CTk.CTkEntry(app, width=260)
todo_entry.place(x=370, y=120)
add_todo_button = CTk.CTkButton(
    app, text="+", font=("Courier New", 20), width=40, command=add_task)
add_todo_button.place(x=650, y=120)

delete_all_button = CTk.CTkButton(app, text="Delete All", font=(
    "Courier New", 20), width=40, command=delete_all_tasks)
delete_all_button.place(x=370, y=520)

reminders_top_label = CTk.CTkLabel(
    app, text="All-Time Reminders", font=("Courier New", 20))
reminders_top_label.place(x=760, y=60)
reminder_entry = CTk.CTkEntry(app, width=260)
reminder_entry.place(x=760, y=120)
add_reminder_button = CTk.CTkButton(
    app, text="+", font=("Courier New", 20), width=40, command=add_reminder)
add_reminder_button.place(x=1040, y=120)

delete_all_reminders_button = CTk.CTkButton(app, text="Delete All", font=(
    "Courier New", 20), width=40, command=delete_all_reminders)
delete_all_reminders_button.place(x=960, y=520)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", font=("Courier New", 20), command=back_to_desky)
back_to_desky_button.place(x=5, y=550)
exit_button = CTk.CTkButton(
    app, text="Exit", font=("Courier New", 20), command=exit)
exit_button.place(x=190, y=550)
app.mainloop()
