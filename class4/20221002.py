#引入 tkinter module
from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("Hello World")
#設定視窗大小為 300x100，視窗(左上角)在螢幕上的座標位置為(500,150)
root.geometry("300x100+500+150")
#寫法一
#建立 label 標籤
myLabel = Label(root, text="Hello World", fg="Lightskyblue", bg="lightgreen",font=("",20,"bold"))
#加入視窗中
myLabel.pack(pady=20)
mybutton = Button(root, text="Click me!")
def clicked():
    label1 = Label(root, text="Button is clicked")
    label1.pack()
#建立button按鈕
mybutton = Button(root, text="Click me!", command=clicked)
#加入視窗中
mybutton.pack()
#建立 Input Entry Boxes
e = Entry(root, width=30, font=("Comic Sans MN", 16))
#加入視窗中
e.pack()
def getcontent():
    a= Label(root, text=e.get())
    a.pack()
#建立button按鈕
Enterbutton = Button(root, text="Enter!", command=getcontent)
#加入視窗中
Enterbutton.pack()
#執行主程式
#mainloop()永遠要在最底下
root.mainloop()