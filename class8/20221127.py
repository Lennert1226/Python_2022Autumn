#引入 tkinter module
from tkinter import *


# 建立主視窗Frame
root = Tk()
# 設定視窗標題
root.title("Class7")
# 設定視窗大小為 200x200
root.geometry("200x200")
#更改button文字內容
'''
#方法一
counter = 0
def clicked():
    global counter
    counter += 1
    # 設定button的text為點擊的次數
    mybutton["text"] = "click" + str(counter)
# 建立button按鈕
mybutton = Button(root, text = "Click", command=clicked)
mybutton.pack()
'''
'''
#建立StringVar
mystringvar = StringVar()
mystringvar.set("Click")

counter = 0
def clicked():
    global counter
    counter += 1
    #鑑定button的text為點擊的次數
    mystringvar.set("click" + str(counter))

#建立 button 按鈕
mybutton = Button(root, textvariable=mystringvar, command=clicked)
mybutton.pack()
'''
'''
#Way 1

#建立 計算按鈕次數 label 標籤
mybutton = Button(root, text="Hello World")
mybutton.pack()
#get mylabel的文字內容
Label(root, text=mybutton["text"]).pack()


#Way 2

#建立StringVar
mystringvar = StringVar()
mystringvar.set("Hello World!")
#建立 計算按鈕次數 label 標籤
mybutton = Button(root, textvariable=mystringvar)
mybutton.pack()
#get mylabel的文字內容
Label(root, text=mystringvar.get()).pack()
'''
#引入 Pillow module
from PIL import Image, ImageTk

# #開啟圖片
# img = Image.open("C:/Users/SP513-52N/Documents/Python_2022Autumn/class8/166586341139792_P13371464.jpg")
# #更改圖片大小
# resized_image = img.resize((100,100))
# #轉換為 tk 圖片物件
# tk_img = ImageTk.PhotoImage(resized_image)
# # 在 Lable 中放入圖片
# label = Label(root, image=tk_img)
# label.pack()

# #在 Button 中放入圖片
# mybutton = Button(root, image=tk_img)
# mybutton.pack()
from tkinter import messagebox
# #出現"message test"的普通訊息框
# messagebox.showinfo("showinfo", "message test")
# #出現提問訊息框

def popup():
    #出現是或否訊息框
    # messagebox.askyesno("askyesno", "Do you want to continue?")
    result = messagebox.askquestion("askquestion", "Is it Sunday?")
    print("User click" + result)

#點擊button出現pop up message box
popupbutton = Button(root, text = "Click to Pop Up!", command=popup)
popupbutton.pack()
#宣告一個文字變數
val = StringVar()
#放入第一個單選按鈕
radiobtn1 = Radiobutton(root, text="Black", variable=val, value="Black")
radiobtn1.pack()
#指定選取締一個單選按鈕
radiobtn1.select()
#放入第二個單選按鈕
radiobtn2 = Radiobutton(root, text="Red", variable=val, value="Red")
radiobtn2.pack()
#執行主程式
root.mainloop()