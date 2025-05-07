from tkinter import *

def miles_to_km():
    calculated_km.config(text= float(entry.get()) * 1.60934)

screen = Tk()

screen.minsize(width=200, height=200)
screen.config(padx=20, pady=20)
screen.title("Miles to Km")

button = Button(text="Click Me", command=miles_to_km)
button.grid(column=1, row=0)

text = Label(text="Into the km")
text.grid(column=0, row=1)

calculated_km=Label(text="0")
calculated_km.grid(column=1, row=1)

km_text=Label(text="KM")
km_text.grid(column=2, row=1)

entry = Entry(width=7)
entry.grid(column=0, row=0)

screen.mainloop()