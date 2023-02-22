import customtkinter as CTk 
import tkinter as tk
import psutil, platform

app = CTk.CTk()
#TODO: change name 
app.title('My PC')
app.geometry('400x400')
app.resizable(False,False)
def show_sysinfo():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    platform_info = platform.system() + ' ' + platform.release()
    sysinfo = f"""
    CPU Usage: {cpu_percent}% \n
    Memory Usage: {memory_info.percent}% \n
    Disk Usage: {disk_info.percent}% \n
    Platform: {platform_info}\n 
    """
    sysinfo_label.configure(text=sysinfo)
    app.after(1000,show_sysinfo)

sysinfo_label = CTk.CTkLabel(app, text="", font = ('Arial',12), justify= "left")
sysinfo_label.place(x=20,y=100)
show_sysinfo()
app.mainloop()


