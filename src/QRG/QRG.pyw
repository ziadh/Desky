import qrcode
import customtkinter as CTk
from PIL import ImageTk, Image
import io
import json
import subprocess


def generate_qr():
    link = link_entry.get()

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    tk_img = ImageTk.PhotoImage(Image.open(img_bytes))

    qr_label.configure(image=tk_img)
    qr_label.image = tk_img


def back_to_desky():
    app.destroy()
    subprocess.run(["python", "Desky.pyw"],
                   creationflags=subprocess.CREATE_NO_WINDOW)


with open("settings.json", 'r')as f:
    settings = json.load(f)

theme = settings['theme']
version = settings['version']

if theme == 'dark':
    CTk.set_appearance_mode("dark")
else:
    CTk.set_appearance_mode("light")

CTk.set_default_color_theme("blue")
app = CTk.CTk()
app.title(f'QR Code Generator v{version}')
app.geometry('400x500')
app.resizable(False, False)
app.bind("<Return>", lambda _: generate_button.invoke())
top_label = CTk.CTkLabel(
    app, text='Welcome to QR Generator', font=("Courier New", 20))
top_label.place(x=10, y=30)
link_entry = CTk.CTkEntry(app,width=220)
link_entry.place(x=10, y=70)

generate_button = CTk.CTkButton(
    app, text='Generate QR Code', command=generate_qr)
generate_button.place(x=250, y=70)

qr_label = CTk.CTkLabel(app, text='')
qr_label.place(x=50, y=120)

back_to_desky_button = CTk.CTkButton(
    app, text="Back To Desky", font=("Courier New", 20), command=back_to_desky,width=10)
back_to_desky_button.place(x=50, y=450)
exit_button = CTk.CTkButton(
    app, text="Exit", font=("Courier New", 20), command=exit,width=10)
exit_button.place(x=300, y=450)

app.mainloop()
