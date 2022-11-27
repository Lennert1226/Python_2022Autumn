from tkinter import *
root = Tk()
root.title("HW_1")
root.geometry("200x100")

#Label 元件
titlelabel = Label(root, text="Kube shop")
productnamelabel = Label(root, text="戶外餐桌椅組")
pricelabel = Label(root, text="$ 1200")
numlabel = Label(root, text="0")

#Button 元件
addbutton = Button(root, text="+")
minusbutton = Button(root, text="-")

titlelabel.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
productnamelabel.grid(row=1, column=0, columnspan=2, sticky=W)
pricelabel.grid(row=2, column=0, sticky=W)
addbutton.grid(row=3, column=0, sticky=W)
numlabel.grid(row=3, column=1, sticky=W)
minusbutton.grid(row=3, column=2, sticky=W)

root.mainloop()