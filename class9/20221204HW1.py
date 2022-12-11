# 引入 tkinter module
from tkinter import *
# 引入 tkinter 的 messagebox
from tkinter import messagebox

# 建立主視窗Frame
root = Tk()
# 設定視窗標題
root.title("Class8")
# 設定視窗大小為 300x200
root.geometry("300x200")
# 宣告一個文字變數
val = StringVar()
# Radio Button 元件
def add:
    # numlabel的text +1

addbutton = Button

radiobutton1 = Radiobutton(root, text="黑色", variable=val, value="黑色")
radiobutton2 = Radiobutton(root, text="灰色", variable=val, value="灰色", state=DISABLED)
radiobutton3 = Radiobutton(root, text="咖啡色", variable=val, value="咖啡色")
selectlabel = Label(root, textvariable=val)

titlelabel.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
imagelabel.grid(row=1, column=0, rowspan=3, )