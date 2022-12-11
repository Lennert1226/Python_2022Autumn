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
def add():
    if int(numlabel["text"]) >=5:
        #建立新視窗 New Windows
        newWindow = Toplevel(root)
        newWindow.geometry("200x100")
        #建立新label在New Windows 裡
        
# 宣告一個文字變數
val = StringVar()