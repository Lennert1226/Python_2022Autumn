from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("KubeTech Shop")

root.geometry("880x650")

val = StringVar()
# row=0
titleimg = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class10/image/logo_tree.png")
titleimg = titleimg.resize((32,32))
titleimg = ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image=titleimg, width=32, height=32)
titlelabel.grid(row=0, column=0, sticky=W)
sofabtn1 = Button(root, text="沙發", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2)
sofabtn1.grid(row=0, column=1, sticky=E+W)
bedding= Button(root, text="寢具", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2)
bedding.grid(row=0, column=2, sticky=E+W)
kitchen = Button(root, text="廚具", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2)
kitchen.grid(row=0, column=3, sticky=E+W)
loginbutton = Button(root, text="會員登入/註冊", font=("Inter", 18), fg="#1E1E1E", bg="#ECE8E7", width=12, pady=2)
loginbutton.grid(row=0, column=7, sticky=E+W, padx=5)
# row=1
bannerimg = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class10/image/banner.jpg")
bannerimg = bannerimg.resize((852,298))
bannerimg = ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image=bannerimg, width=852, height=298)
bannerlabel.grid(row=1, column=1, sticky=W, padx=5, columnspan=8)
# row=2
sofa1img = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class10/image/sofa1.jpg")
sofa1img = sofa1img.resize((202,200))
sofa1img = ImageTk.PhotoImage(sofa1img)
sofa1label = Label(root, image=sofa1img, width=202, height=200)
sofa1label.grid(row=2, column=0, sticky=W, padx=5, columnspan=2)

sofa2img = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class10/image/sofa2.jpg")
sofa2img = sofa2img.resize((202,200))
sofa2img = ImageTk.PhotoImage(sofa2img)
sofa2label = Label(root, image=sofa2img, width=202, height=200)
sofa2label.grid(row=2, column=2, sticky=W, padx=5, columnspan=2)

sofa3img = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class10/image/sofa3.jpg")
sofa3img = sofa3img.resize((202,200))
sofa3img = ImageTk.PhotoImage(sofa3img)
sofa3label = Label(root, image=sofa3img, width=202, height=200)
sofa3label.grid(row=2, column=4, sticky=W, padx=5, columnspan=2)

sofa4img = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class10/image/sofa4.jpg")
sofa4img = sofa4img.resize((202,200))
sofa4img = ImageTk.PhotoImage(sofa4img)
sofa4label = Label(root, image=sofa4img, width=202, height=200)
sofa4label.grid(row=2, column=6, sticky=W, padx=5, columnspan=2)
# row=3
productname1 = Label(root, text="三人座沙發, grann/bomstad 黑色/金屬", font=("Inter", 11), fg="#000000")
productname2 = Label(root, text="三人座沙發, grann/bomstad 黑色/木材", font=("Inter", 11), fg="#000000")
productname3 = Label(root, text="三人座沙發, grann/bomstad 米色/金屬", font=("Inter", 11), fg="#000000")
productname4 = Label(root, text="三人座沙發, grann/bomstad 米色/木頭", font=("Inter", 11), fg="#000000")

productname1.grid(row=3, column=0, sticky=W, padx=5, columnspan=2)
productname2.grid(row=3, column=2, sticky=W, padx=5, columnspan=2)
productname3.grid(row=3, column=4, sticky=W, padx=5, columnspan=2)
productname4.grid(row=3, column=6, sticky=W, padx=5, columnspan=2)
# row=4
productprice1 = Label(root, text="NT.28,900", font=("Inter", 11), fg="#000000")
productprice2 = Label(root, text="NT.28,900", font=("Inter", 11), fg="#000000")
productprice3 = Label(root, text="NT.28,900", font=("Inter", 11), fg="#000000")
productprice4 = Label(root, text="NT.28,900", font=("Inter", 11), fg="#000000")

productname1.grid(row=3, column=0, sticky=W, padx=5)
productname2.grid(row=3, column=2, sticky=W, padx=5)
productname3.grid(row=3, column=4, sticky=W, padx=5)
productname4.grid(row=3, column=6, sticky=W, padx=5)
root.mainloop()