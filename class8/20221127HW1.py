#引入 tkinter module
from tkinter import *
from tkinter import messagebox
#引入 Pillow module
from PIL import Image, ImageTk
# 建立主視窗Frame
root = Tk()
# 設定視窗標題
root.title("Class7")
# 設定視窗大小為 200x200
root.geometry("300x200")

def add():
    # numlabel的text +1
    numlabel["text"] = int(numlabel["text"])+1
def minus():
    #當numlabel大於0時，才會進行減1
    if int(numlabel["text"])>0:
        # numlabel的text +1
        numlabel["text"] = int(numlabel["text"])-1
    #當numlabel小於0時，跳出警告訊息框
    else:
        messagebox.showwarning("showwarning", "The number of products can\'t be below 0.")

#開啟圖片
img = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class8/sofa.jpg")
#更改圖片大小
resized_image = img.resize((150,100))
#轉換為 tk 圖片物件
tk_img = ImageTk.PhotoImage(resized_image)
#在 Label 中放入圖片
imagelabel = Label(root, image=tk_img)
# Label 元件
titlelabel = Label(root, text="Kube shop")
productnamelabel = Label(root, text="沙發組")
pricelabel = Label(root, text="$1200")
numlabel = Label(root, text="0")

#Button 元件
addbutton = Button(root, text="+", command=add)
minusbutton = Button(root, text="-", command=minus)

titlelabel.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S)
imagelabel.grid(row=1, column=0, columnspan=2)
productnamelabel.grid(row=2, column=0, columnspan=2, sticky=W)
pricelabel.grid(row=2, column=2, columnspan=2, sticky=W)
minusbutton.grid(row=3, column=2, sticky=W)
numlabel.grid(row=3, column=3, sticky=W+E+N+S)
addbutton.grid(row=3, column=4, sticky=E)
#執行主程式
root.mainloop()