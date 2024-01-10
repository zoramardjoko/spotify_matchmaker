import tkinter as tk
from tkinter import *


def create_song_similarity():
    import SpotipyTest
    SpotipyTest


def create_playlist():
    import Recommendations
    Recommendations


def create_graph():
    import Graph
    Graph


root = tk.Tk()
root.title("Spotipy Matchmaker")

# Create a canvas widget
canvas = tk.Canvas(root, width=150, height=100, bg='white')
canvas.pack()

# Create some buttons
button1 = tk.Button(root, text='Get a new playlist', font=('Times New Roman', 12), bg='#3498DB', height=12, width=30,
                    command=create_playlist)
button1.pack(side='left', padx=10)
button2 = tk.Button(root, text='Find out your two most similar songs', font=('Times New Roman', 12), bg='#45B39D',
                    height=12, width=30, command=create_song_similarity)
button2.pack(side='left', padx=10)
button3 = tk.Button(root, text='Get most similar artists (with degrees)', font=('Times New Roman', 12), bg='#EC7063',
                    height=12, width=30, command=create_graph)
button3.pack(side='left', padx=10)
lf = LabelFrame(canvas, text='Created by Brandon Tsai, Shruthi Kunjur, Zora Mardjoko')
lf.pack()
label = Label(lf, text="Choose an option to learn more about your music and artists!")
label.config(font='Times 12')
label.pack(padx=20, pady=20)

# Start the main event loop
root.mainloop()
