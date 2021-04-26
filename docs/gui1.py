from tkinter import *
from tkinter import ttk #ttk is the newer graphic/style

def calculate(*args): #with * we take any arguments
    try:
        value = float(fahrenheit.get())
        celsius.set((value - 32) * (5/9))
    except ValueError:
        pass #Ignore for now, it won't do anything if we don't input/type a number

root = Tk() #creates a new window
root.title("Convert Fahrenheit to Celsius")

frame = ttk.Frame(root, padding = "3 3 12 12") #padding=left-right-top-bottom
frame.grid(column = 0, row = 0, sticky = (N, S, E, W))
frame.configure(borderwidth = 5)
root.columnconfigure(0, weight = 2)
root.rowconfigure(0, weight = 2)
#Different choices for the frame style
#frame["relief"] = "raised"
frame["relief"] = "sunken"
#frame["relief"] = "ridge"
#frame["relief"] = "groove"

for col in range(1, 4):
    frame.columnconfigure(col, weight = 1)

for row in range(1, 4):
    frame.rowconfigure(row, weight = 1)

fahrenheit = StringVar()
celsius = StringVar()

choice = StringVar()
choice.set("What degrees do you want to convert?")
degreesbox = ttk.Combobox(frame, textvariable = choice)
degreesbox["values"] = ("Fahrenheit", "Celsius")
degreesbox.grid(column = 1, row = 1)

fahrEntry = ttk.Entry(frame, width = 7, textvariable = fahrenheit)
fahrEntry.grid(column = 2, row = 1, sticky = (W, E))

fahrLabel = ttk.Label(frame, text = "Degrees F")
fahrLabel.grid(column = 3, row = 1, sticky = W)

equiLabel = ttk.Label(frame, text = "Fahrenheit is equivalent to")
equiLabel.grid(column = 1, row = 2, sticky = E)

celsiusLabel = ttk.Label(frame, textvariable = celsius)
celsiusLabel.grid(column = 2, row = 2, sticky = (W, E))

degreesCLabel = ttk.Label(frame, text = "Degrees C")
degreesCLabel.grid(column = 3, row = 2, sticky = W)

goButton = ttk.Button(frame, text = "Convert", command = calculate) #when we press the Go button, run the calculate function
goButton.grid(column = 3, row = 3, sticky = W)

for child in frame.winfo_children():
    child.grid_configure(padx = 15, pady = 10)

fahrEntry.focus()
root.bind("<Return>", calculate)

root.mainloop() #without this line of command, the window will disappear
