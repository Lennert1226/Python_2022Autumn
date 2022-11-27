from tkinter import *
root = Tk()
root.title("Class4_HW1")
root.geometry("400x400+150+200")
myLabel = Label(root, text="點擊按鈕次數計算", fg="Orange",font=("Garamond",25,"bold"))
myLabel.pack()

x = 0
def clicked():
