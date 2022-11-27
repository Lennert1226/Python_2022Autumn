#引入 tkinter module
from tkinter import *

root = Tk()
root.title("Class6")
root.geometry("350x100")

#加入 Frame 框架
frame = Frame(root)
frame.pack()


frame1 = Frame(root, pady=5, padx=20, bg="lightblue")
frame2 = Frame(root, pady=20, padx=10, bg="pink")

#放到 frame1 裡的 label
label1 = Label(frame1, text="hello", width=10)
label1.pack()
#放到 frame2 裡的 label
label2 = Label(frame2, text="world", width=20) 
label2.pack()

#先放 frame2
frame2.pack()
#再放 frame1
frame1.pack()
#執行主程式
root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Class7")
# root.geometry("350x100")
# #更改Label文字內容
# #建立StringVar
# mystringvar = StringVar()
# mystringvar.set("Hello world!")
# #建立 計算按鈕此數 label 標籤
# mylabel = Label(root, textvariable=mystringvar)
# mylabel.pack()
# root.mainloop()


'''

#Way1
from tkinter import *

root = Tk()
root.title("Class7")
root.geometry("350x100")

#建立 計算按鈕次數 label 標籤
mylabel = Label(root, text="Hello World")
mylabel.pack()
# get mylabel的文字內容
Label(root, text=mylabel["text"]).pack()
root.mainloop()
'''
'''
#Way2
from tkinter import *

root = Tk()
root.title("Class7")
root.geometry("350x100")
#建立Stringvar
mystringvar = StringVar()
mystringvar.set("Hello World!")
#建立 計算按鈕次數 label 標籤
mylabel = Label(root, textvariable=mystringvar)
mylabel.pack()
#get mylabel的文字內容
Label(root, text=mystringvar.get()).pack()
root.mainloop()
'''