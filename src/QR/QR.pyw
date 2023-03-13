import qrcode
import tkinter as tk
import customtkinter as CTk
from PIL import ImageTk, Image
import io


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


# todo: add theme
# todo: add backtodesky
app = CTk.CTk()
# todo: add version
app.title('QR Code Generator')
app.geometry('400x550')
app.resizable(False, False)
app.bind("<Return>", lambda _: generate_button.invoke())
top_label = CTk.CTkLabel(
    app, text='Welcome to QR Generator', font=("Courier New", 20))
top_label.place(x=10, y=30)
link_label = CTk.CTkLabel(app, text='Enter link:')
link_label.place(x=20, y=70)
link_entry = CTk.CTkEntry(app)
link_entry.place(x=90, y=70)

generate_button = CTk.CTkButton(
    app, text='Generate QR Code', command=generate_qr)
generate_button.place(x=240, y=70)

qr_label = CTk.CTkLabel(app, text='')
qr_label.place(x=10, y=120)

app.mainloop()
