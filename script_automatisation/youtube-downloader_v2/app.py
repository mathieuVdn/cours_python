import tkinter as tk
from tkinter import Tk, Frame, Label, Entry, Button, StringVar, ttk
from PIL import Image, ImageTk
import youtube_downloader
import threading

BG_COLOR = "#e8e2e9"

string_var_url = None  # Déclaration de la variable globale
button_entry = None


def telecharger_video():
    url = string_var_url.get()
    if url:
        button_entry.config(state="disabled")  # Désactive le bouton pendant le téléchargement
        download_thread = threading.Thread(target=youtube_downloader.download_video, args=(url,))
        download_thread.start()
        button_entry.config(state="normal")  # Réactive le bouton après le téléchargement
        

def main():
    global string_var_url
    global button_entry
    window = Tk()
    window.title("Youtube downloader")
    window.geometry("1080x720")
    window.minsize(480, 760)
    window.iconbitmap("assets/youtube-ico")
    window.config(background=BG_COLOR)
    window.resizable(width=False, height=False)

    frame_title = Frame(window, bg=BG_COLOR)
    frame_title.place(x=20, y=23)

    label_title = Label(frame_title, text="                         Downloader", font=("@Yu Gothic UI Semibold", 30),
                        bg=BG_COLOR)
    label_title.pack(anchor="w")

    header_img_open = Image.open("assets/youtube_logo.png")
    header_img_resized = header_img_open.resize((260, 60))
    header_img = ImageTk.PhotoImage(header_img_resized)
    label_header_img = Label(window, image=header_img, background=BG_COLOR)
    label_header_img.place(x=20, y=15)

    label_subtitle = Label(frame_title, text="Outils de téléchargement de vidéo YouTube optimisé",
                           font=("@Microsoft JhengHei UI", 12), bg=BG_COLOR)
    label_subtitle.pack(anchor="w", padx=10)

    frame_entry = Frame(window, bg=BG_COLOR, bd=1)
    frame_entry.place(x=175, y=250)

    label_entry = Label(frame_entry, text="Entrez une URL YouTube", width=20, bg=BG_COLOR)
    label_entry.pack()

    string_var_url = StringVar()
    entry_url = Entry(frame_entry, bd=1, width=80, textvariable=string_var_url, font=("@Microsoft JhengHei UI", 12))
    entry_url.pack(pady=20)

    button_entry = Button(frame_entry, text='Télécharger la vidéo', command=telecharger_video, bg="#ffffff", bd=3,
                          font=("@Microsoft JhengHei UI", 10), activebackground=BG_COLOR,
                          cursor="hand2", relief="ridge")
    button_entry.pack(ipadx=15, ipady=5, pady=10)

    frame_progress_bar = Frame(window, bg=BG_COLOR)

    label_progress_bar = Label(frame_progress_bar, text="Progression", bg=BG_COLOR)
    label_progress_bar.pack(pady=10)
    progress_var = tk.IntVar()
    progress_bar = ttk.Progressbar(frame_progress_bar, variable=progress_var, mode='determinate', length=400)
    progress_bar.pack()

    frame_progress_bar.place(x=338, y=420)

    frame_copy_right = Frame(window, bg=BG_COLOR)
    frame_copy_right.place(x=405, y=730)
    label_copy_right = Label(frame_copy_right, text="© 2021 - Youtube downloader - MathieuVdn", bg=BG_COLOR)
    label_copy_right.pack()

    window.mainloop()


if __name__ == "__main__":
    main()
