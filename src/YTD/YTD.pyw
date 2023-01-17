import tkinter
import customtkinter
from pytube import YouTube


class YTD():
    def __init__(self):
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

        app = customtkinter.CTk()
        app.geometry("320x320")
        app.title("YouTube Downloader")
        app.resizable(False, False)
        title = customtkinter.CTkLabel(
            app, text="Please insert a YouTube link below:")
        title.pack(padx=10, pady=10)

        url_var = tkinter.StringVar()

        self.link = customtkinter.CTkEntry(
            app, width=230, height=40, textvariable=url_var)
        self.link.pack()

        self.finishLabel = customtkinter.CTkLabel(app, text="")
        self.finishLabel.pack()

        self.progressPercent = customtkinter.CTkLabel(app, text="0%")
        self.progressPercent.pack()

        self.progressBar = customtkinter.CTkProgressBar(app, width=400)
        self.progressBar.set(0)
        self.progressBar.pack(padx=10, pady=10)

        download_highest_res_button = customtkinter.CTkButton(
            app, text="Highest Res Download", command=self.download_highest_res)
        download_highest_res_button.place(x=13, y=229)
        lowest_res_button = customtkinter.CTkButton(
            app, text="Lowest Res Download", command=self.download_lowest_res)
        lowest_res_button.place(x=169, y=229)
        download_in_720p = customtkinter.CTkButton(
            app, text="Download in 720p60p", command=self.download_720p)
        download_in_720p.place(x=13, y=270)
        audio_only_button = customtkinter.CTkButton(app,
                                                    text="Audio Only", command=self.audio_only)
        audio_only_button.place(x=169, y=270)
        app.mainloop()

    def download_highest_res(self):
        try:
            ytLink = self.link.get()
            ytObject = YouTube(ytLink, on_progress_callback=self.on_progress)
            video = ytObject.streams.get_highest_resolution()
            self.finishLabel.configure(text="")
            video.download()
            self.finishLabel.configure(text="Downloaded!")
        except:
            self.finishLabel.configure(
                text="Youtube link is invalid.", text_color="red")

    def download_lowest_res(self):
        try:
            ytLink = self.link.get()
            ytObject = YouTube(ytLink, on_progress_callback=self.on_progress)
            video = ytObject.streams.get_lowest_resolution()
            self.finishLabel.configure(text="")
            video.download()
            self.finishLabel.configure(text="Downloaded!")
        except:
            self.finishLabel.configure(
                text="Youtube link is invalid.", text_color="red")

    def download_720p(self):
        try:
            ytLink = self.link.get()
            ytObject = YouTube(ytLink, on_progress_callback=self.on_progress)
            video = ytObject.streams.get_by_resolution("720p")
            self.finishLabel.configure(text="")
            video.download()
            self.finishLabel.configure(text="Downloaded!")
        except:
            self.finishLabel.configure(
                text="Youtube link is invalid.", text_color="red")

    def audio_only(self):
        try:
            ytLink = self.link.get()
            ytObject = YouTube(ytLink, on_progress_callback=self.on_progress)
            video = ytObject.streams.get_audio_only()
            self.finishLabel.configure(text="")
            video.download()
            self.finishLabel.configure(text="Downloaded!")
        except:
            self.finishLabel.configure(
                text="Youtube link is invalid.", text_color="red")

    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size ^ bytes_remaining
        percentage_of_compeletion = bytes_downloaded / total_size * 100
        per = str(int(percentage_of_compeletion))
        self.progressPercent.configure(text=per + '%')
        self.progressPercent.update()
        self.progressBar.set(float(percentage_of_compeletion)/100)


YTD()
