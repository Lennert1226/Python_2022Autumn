# from tkinter import *
# root = Tk()
# root.geometry("400x400+150+200")

# #side 排列方向:TOP(預設),BOTTOM,LEFT,RIGHT
# #建立label標籤
# mybutton1 = Button(root, text = "West")
# mybutton2 = Button(root, text = "East")
# # mybutton3 = Button(root, text = "East2")

# # mybuttom1.pack(side = "left")
# # mybutton2.pack(side = "right")
# # mybutton3.pack(side = "right")
# # fill 填滿所分配空間之方向:NONE(預設),X,Y,BOTH
# # mybutton1.pack(fill = "x")
# # mybutton2.pack(side = "right", fill = "y")
# # expand 填滿容器:True/False(預設)
# # mybutton1 = Button(root, text="expand = 0")
# # mybutton1.pack(fill = "both",expand = 0)
# # mybutton2 = Button(root, text="expand = 1")
# # mybutton2.pack(fill = "both",expand = 1)
# # padx/pady 元件邊框與容器之距離(px, 預設=0)
# # mybutton1.pack(side = "left", padx = 20)
# # mybutton2.pack(side = "right", padx = 30)
# # ipadx/ipady 元件內容(文字/圖像)與其邊框之距離(px, 預設=0)
# mybutton1.pack(side = "left", ipadx = 30)
# mybutton2.pack(side = "right", ipady = 30)


# from tkinter import *
# root = Tk()
# root.geometry("400x400+150+200")
# mybutton1 = Button(root, text = "button1")
# mybutton2 = Button(root, text = "button2")
# mybutton3 = Button(root, text = "button3")

# mybutton1.pack()
# mybutton2.pack(side = "left")
# mybutton3.pack(side = "bottom")
# root.mainloop()

from tkinter import *
root = Tk()
root.geometry("400x400+150+200")
mybutton1 = Button(root, text = "button1")
mybutton2 = Button(root, text = "button2")
mybutton3 = Button(root, text = "button3")
mybutton4 = Button(root, text = "button4")
mybutton5 = Button(root, text = "button5")

mybutton1.pack(fill = X)
mybutton2.pack(side = "left", fill = Y)
mybutton3.pack(side = "left")
mybutton4.pack(side = "right")
mybutton5.pack(side = "top")
root.mainloop()