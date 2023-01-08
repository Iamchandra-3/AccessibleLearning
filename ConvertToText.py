# Importing the necessary libraries
import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Function to convert audio file to text


def audio_to_text():
    r = sr.Recognizer()
    audio_file = sr.AudioFile(file_path)

    with audio_file as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)

    # Display the converted text in a message box
    messagebox.showinfo("Converted Text", text)


def convertAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Something!")
        audio = r.listen(source)
        print("Over, Thanks!")
    try:
        text = r.recognize_google(audio)
        label.insert('end', text)
    except:
        pass
    messagebox.showinfo("Converted Text", text)

# Creating the GUI
root = tk.Tk()
root.geometry("500x200")
root.title("Audio to Text ")

# Adding a label
label = tk.Label(root, text="Convert Audio File to Text")
label.pack()


# Adding a button
button = tk.Button(root, text="Browse Audio File",
                   command=lambda: browse_file(root))
button.pack()


b1 = tk.Button(root, text="Convert Audio to Text", command=convertAudio)
b1.pack()


def browse_file(root):
    global file_path
    file_path = filedialog.askopenfilename()
    convert_button = tk.Button(
        root, text="Convert", command=lambda: audio_to_text())
    convert_button.pack()


# Keep the GUI running
root.mainloop()

