import tkinter as tk
import customtkinter as CTk
import subprocess
import json

def start_stopwatch():
    global sw_running, sw_time_elapsed
    sw_running = not sw_running
    if sw_running:
        start_button.configure(text='Stop')
        update_time()
    else:
        start_button.configure(text='Start')


def update_time():
    global sw_running, sw_time_elapsed
    if sw_running:
        sw_time_elapsed += 0.1
        minutes, seconds = divmod(sw_time_elapsed, 60)
        millisecs = (sw_time_elapsed - int(sw_time_elapsed))*1000
        display.configure(
            text=f'{int(minutes):02d}:{int(seconds):02d}.{int(millisecs):03d}')
        display.after(100, update_time)


def reset_stopwatch():
    global sw_running, sw_time_elapsed
    sw_running = False
    start_button.configure(text='Start')
    sw_time_elapsed = 0
    display.configure(text='00:00.000')


def start_countdown():
    global cd_is_running, cd_remaining
    if not cd_is_running and cd_remaining > 0:
        cd_is_running = True
        update_cd()


def stop_countdown():
    global cd_is_running
    cd_is_running = False


def reset_countdown():
    global cd_is_running, cd_remaining
    cd_is_running = False
    countdown = 0
    cd_remaining = 0
    update_cd_label()


def set_countdown(minutes):
    global countdown, cd_remaining
    countdown = minutes * 60
    cd_remaining = countdown
    update_cd_label()


def set_custom_time():
    global countdown, cd_remaining
    custom_time = custom_time_entry.get()
    try:
        minutes, seconds = custom_time.split(':')
        minutes = int(minutes)
        seconds = int(seconds)
        countdown = minutes * 60 + seconds
        cd_remaining = countdown
        update_cd_label()
    except ValueError:
        pass


def update_cd_label():
    global cd_remaining
    minutes = cd_remaining // 60
    seconds = cd_remaining % 60
    time_label.configure(text=f'{minutes:02d}:{seconds:02d}')


def update_cd():
    global cd_is_running, cd_remaining
    if cd_is_running and cd_remaining > 0:
        cd_remaining -= 1
        update_cd_label()
        app.after(1000, update_cd)
    elif cd_remaining == 0:
        cd_is_running = False


countdown = 0
cd_remaining = 0
cd_is_running = False


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)

with open("settings.json", 'r')as f:
    settings = json.load(f)
version = settings['version']
theme = settings['theme']
if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

app = CTk.CTk()
app.title(f'Tok Tik v{version}')
app.geometry('1200x500')
app.resizable(False, False)


############ START OF STOPWATCH ############
sw_running = False
sw_time_elapsed = 0
top_label = CTk.CTkLabel(app, text='Stopwatch', font=('Arial', 18))
top_label.place(x=20, y=10)
display = CTk.CTkLabel(app, text='00:00.000', font=('Arial', 24))
display.place(x=90, y=90)

start_button = CTk.CTkButton(app, text='Start', command=start_stopwatch)
start_button.place(x=20, y=160)

reset_button = CTk.CTkButton(app, text='Reset', command=reset_stopwatch)
reset_button.place(x=170, y=160)

############ END OF STOPWATCH ############

############ START OF COUNTDOWN ############
countdown_label =CTk.CTkLabel(app,text='Countdown', font=('Arial', 18))
countdown_label.place(x=420,y=10)
time_label = CTk.CTkLabel(app, text='00:00:00', font=('Arial', 24))
cd_start_button = CTk.CTkButton(app, text='Start', command=start_countdown)
cd_stop_button = CTk.CTkButton(app, text='Stop', command=stop_countdown)
cd_reset_button = CTk.CTkButton(app, text='Reset', command=reset_countdown)

five_minutes_button = CTk.CTkButton(
    app, text='5', command=lambda: set_countdown(5), width=50)
ten_minutes_button = CTk.CTkButton(
    app, text='10', command=lambda: set_countdown(10), width=50)
fifteen_minutes_button = CTk.CTkButton(
    app, text='15', command=lambda: set_countdown(15), width=50)

custom_time_label = CTk.CTkLabel(
    app, text='Set custom time(mm:ss):', font=('Arial', 24))
custom_time_entry = CTk.CTkEntry(app)
custom_time_button = CTk.CTkButton(app, text='Set', command=set_custom_time)

time_label.place(x=450, y=90)
cd_start_button.place(x=420, y=160)
cd_stop_button.place(x=570, y=160)
cd_reset_button.place(x=495, y=200)
five_minutes_button.place(x=520, y=10)
ten_minutes_button.place(x=590, y=10)
fifteen_minutes_button.place(x=660, y=10)
custom_time_label.place(x=420,y=260)
custom_time_entry.place(x=420,y=310)
custom_time_button.place(x=610,y=310)
############ END OF COUNTDOWN ############

back_to_desky_button = CTk.CTkButton(
    app, text='Back To Desky', command=back_to_desky)
back_to_desky_button.place(x=480, y=450)

exit_button = CTk.CTkButton(app, text='Exit', command=exit)
exit_button.place(x=640, y=450)

app.mainloop()
