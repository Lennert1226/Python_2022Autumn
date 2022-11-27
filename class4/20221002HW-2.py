from tkinter import *
from datetime import *
root = Tk()
root.title("CLass4_HW2")
root.geometry("400x400+150+200")
myLabel = Label(root, text="Enter your Birthday:\nInput format is yyyy.mm.dd", fg="Lightskyblue", bg="lightgreen",font=("",20,"bold"))
myLabel.pack()
mybutton = Button(root, text="Click me!")

enterbox = Entry(root, width = 30, font = ("Arial",18, "bold"))
enterbox.pack()
def count():
    time_string = enterbox.get()
    t1 = datetime.strptime(time_string, "%Y.%m.%d")
    t2 = datetime.now()
    result = t2.year-t1.year
    label = Label(root, text="You are " + str(result) + "years old.")
    label.pack()

Button1 = Button(root, text = "Enter!", command = count, font = ("Garamond", 16))
Button1.pack(pady = 20)
root.mainloop()