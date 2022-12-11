from tkinter import *

root = Tk()
root.title("Class7")
root.geometry("200x200")

number = 0

def add():
    # numlabel的text+1
    numlabel["text"] = int(numlabel["text"])+1
    amountLabel["text"] = "總額:$" + str(int(numlabel["text"])*1200)+"元"
def minus():
    # 當numlabel大於0時，才會進行減1
    if int(numlabel["text"])>0:
        # numlabel的text -1
        numlabel["text"] = int(numlabel["text"])-1
        amountLabel["text"] = "總額:$" +str(int(numlabel["text"])*1200)+"元"

# Label 元件
titlelabel = Label(root, text="Kube shop")
productnamelabel = Label(root, text="沙發組")
pricelabel = Label(root, text="$ 1200")
numlabel = Label(root, text = "0")
amountLabel = Label(root, text="總額:$ 0元")

#Button 元件
addbutton =Button(root, text="+", command=add)
minusbutton = Button(root, text="-", command=minus)

titlelabel.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
productnamelabel.grid(row=1, column=0, columnspan=2, sticky=W)
pricelabel.grid(row=1, column=2, sticky=W+E+N+S)
minusbutton.grid(row=3, column=0, sticky=W)
numlabel.grid(row=3, column=1, sticky=W+N+S)
amountLabel.grid(row=4)
addbutton.grid(row=3, column=2)
#執行主程式
root.mainloop()