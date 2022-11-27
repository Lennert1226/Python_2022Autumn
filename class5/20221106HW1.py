from tkinter import *
root = Tk()
root.geometry("400x400+150+200")
mybutton1 = Button(root, text = "1")
mybutton2 = Button(root, text = "2")
mybutton3 = Button(root, text = "3")

mybutton1.pack()
mybutton2.pack(side = "left")
mybutton3.pack(side = "bottom")
root.mainloop()