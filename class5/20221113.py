'''
# anchor 元件在容器中的錨定位置:E,W,S,N,CENTER(預設),NE,SE,SW,NW
#引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Class6")
root.geometry("200x200")

mybutton1 = Button(root, text="東").pack(anchor=E)
mybutton2 = Button(root, text="西").pack(anchor=W)
mybutton3 = Button(root, text="南").pack(anchor=S)
mybutton4 = Button(root, text="北").pack(anchor=N)
mybutton5 = Button(root, text="東南").pack(anchor=SE)
mybutton6 = Button(root, text="西北").pack(anchor=NW)

#執行主程式
root.mainloop()
'''
'''
#引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Class6")
root.geometry("200x200")

mybutton1 = Button(root, text="button1").grid(row=0, column=0)
mybutton2 = Button(root, text="button2").grid(row=0, column=1)
mybutton3 = Button(root, text="button3").grid(row=0, column=2)

mybutton4 = Button(root, text="button4").grid(row=1, column=0)
mybutton5 = Button(root, text="button5").grid(row=1, column=2)

mybutton6 = Button(root, text="button6").grid(row=2, column=1)
#執行主程式
root.mainloop()
'''
'''
#引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Class6")
root.geometry("300x200")

mybutton1 = Button(root, text="button1").grid(row=0, column=0)
mybutton2 = Button(root, text="button2").grid(row=0, column=1)
mybutton3 = Button(root, text="button3").grid(row=0, column=2)

mybutton4 = Button(root, text="button4").grid(row=1, column=0, columnspan=2)
mybutton5 = Button(root, text="button5").grid(row=1, column=2)

mybutton6 = Button(root, text="button6").grid(row=2, column=1)
#rowspan 合併列數
#columnspan 合併行數
#sticky 元件於網路中的錨定位置:E,W,S,N,CENTER(預設)
#執行主程式
root.mainloop()
'''
'''
#引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Class6")
root.geometry("300x200")

mybutton1 = Button(root, text="button1").grid(row=0, column=0)
mybutton2 = Button(root, text="button2").grid(row=0, column=1)
mybutton3 = Button(root, text="button3").grid(row=0, column=2)

mybutton4 = Button(root, text="button4").grid(row=1, column=0, columnspan=2, sticky=W+E)
mybutton5 = Button(root, text="button5").grid(row=1, column=2)

mybutton6 = Button(root, text="button6").grid(row=2, column=1)
#rowspan 合併列數
#columnspan 合併行數
#sticky 元件於網路中的錨定位置:E,W,S,N,CENTER(預設)
#執行主程式
root.mainloop()
'''
'''
from tkinter import *
root = Tk()
root.title("Class6")
root.geometry("300x200")

labelwidth = Label(root, text="Width")
labelwidth.grid(row=0, column=0, sticky=W+N+S)

labelheight = Label(root, text="Height")
labelheight.grid(row=1, column=0, sticky=W+N+S)

entryWidth = Entry(root, width=20)
entryheight = Entry(root, width=20)

entryWidth.grid(row=0, column=1, sticky=N+S)
entryheight.grid(row=1, column=1, sticky=N+S)

resultButton = Button(root, text = "Result")
resultButton.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S)

root.mainloop()
'''
'''
from tkinter import *
root = Tk()
root.title("Class6")
root.geometry("350x100")

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Exit")

menubar.add_cascade(label="file", menu = filemenu)

root.config(menu = menubar)

root.mainloop()
'''
'''
from tkinter import *
root = Tk()
root.title("Class6")
root.geometry("350x100")
#建立主選單
menu = Menu(root)
#建立第一個選單的子選單，有三個選項
menubar1 = Menu(menu, tearoff=0)
menubar1.add_command(label = "Open")
menubar1.add_command(label = "Save")
menubar1.add_command(label = "Exit")
#建立第一個選單 File，綁定子選單
menu.add_cascade(label="File", menu = menubar1)
#建立第二個選單的子選單，有三個選項
menubar2 = Menu(menu, tearoff=0)
menubar2.add_command(label="AAA")
menubar2.add_command(label="BBB")
menubar2.add_command(label="CCC")
#子選單分隔線
menubar2.add_separator()
#建立子選單內的子選單，有三個選項
menubar2more = Menu(menubar2, tearoff=0)
menubar2more.add_command(label = "X")
menubar2more.add_command(label = "Y")
menubar2more.add_command(label = "Z")
menubar2.add_cascade(label="File",menu=menubar2more)
#建立第二個選單 File，綁定子選單
menu.add_cascade(label="Test", menu = menubar2)
#主視窗加入主選單
root.config(menu=menu)
root.mainloop()
'''
'''
from tkinter import *
root = Tk()
root.title("Class6")
root.geometry("350x100")

def open(): print("open")
def save(): print("save")
def exit():
    print("exit")
    root.destroy()
menu = Menu(root)
menubar1 = Menu(menu)
menubar1.add_command(label = "Open", command=open)
menubar1.add_command(label = "Save", command=save)
menubar1.add_command(label = "Exit", command=exit)
menu.add_cascade(label="File", menu=menubar1)

root.config(menu=menu)
root.mainloop()
'''

from tkinter import *
root = Tk()
root.title("Class6")
root.geometry("350x100")

def open(event): print("open")
def save(event): print("save")
def exit(event):
    print("exit")
    root.destroy()
menu = Menu(root)
menubar1 = Menu(menu, tearoff=0)
menubar1.add_command(label = "Open", command=open, accelerator="Control+O")
menubar1.add_command(label = "Save", command=save, accelerator="Control+S")
menubar1.add_command(label = "Exit", command=exit, accelerator="Control+E")
menu.add_cascade(label="File", menu=menubar1)

root.bind_all("<Control-O>", open)
root.bind_all("<Control-s>", save)
root.bind_all("<Control-e>", exit)
root.config(menu=menu)

root.mainloop()

'''
from tkinter import *
root = Tk()
root.title("Class6")
root.geometry("350x100")

def open():
    print("open")
    menubar.entryconfig("Save", state="normal")
def open(): print("open")
def save(): print("save")
def exit():
    print("exit")
    menubar.entryconfig("Save", state="disabled ")

menu = Menu(root)
menubar = Menu(menu, tearoff=0)

menubar.add_command(label = "Open", command=open, state = "normal")
menubar.add_command(label = "Save", command=save, state = "disabled")
menubar.add_command(label = "Exit", command=exit)
menu.add_cascade(label="File", menu=menubar)

root.config(menu=menu)

root.mainloop()
'''