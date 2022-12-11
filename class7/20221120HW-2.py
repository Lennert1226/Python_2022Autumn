#引入 tkinter module
from tkinter import *

root = Tk()
root.title("Class7")
root.geometry("350x100")

#加入 Frame 框架
frame = Frame(root)
frame.pack()

#放到 frame1 裡的 label
frame1 = Frame(root, pady=10, padx=2, bg="lightblue")
#放到 frame2 裡的 label
frame2 = Frame(root, pady=5, padx=10, bg="lightgreen")

label1 = Label(frame1, text="Second", width=10) 
label1.pack()

label2 = Label(frame2, text="First", width=10)
label2.pack()

#先放 frame2
frame2.pack(side="left")
#再放 frame1
frame1.pack(side="right")
#執行主程式
root.mainloop()