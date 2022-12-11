'''
#引入 tkinter module
from tkinter import *
#引入 tkinter 的 messagebox
from tkinter import messagebox

# 建立主視窗Frame
root = Tk()
# 設定視窗標題
root.title("Class8")
# 設定視窗大小為 300x200
root.geometry("300x200")
# #宣告一個文字變數
# val = StringVar()

# # label顏色依顏色內容更換
# def clickradiobtn1():
#     selectlabel["fg"] = "Blue"
#     selectlabel["textvariable"] = val
# def clickradiobtn2():
#     selectlabel["fg"] = "Green"
#     selectlabel["textvariable"] = val
# def clickradiobtn3():
#     selectlabel["fg"] = "Pink"
#     selectlabel["textvariable"] = val
# titlelable = Label(root, text="Please select the color you prefer")
# titlelable.pack()
# #放入第一個單選按鈕
# radiobtn1 = Radiobutton(root, text="Blue", variable=val, value="Blue", fg="Blue", command=clickradiobtn1)
# radiobtn1.pack()
# #放入第二個單選按鈕
# radiobtn2 = Radiobutton(root, text="Green", variable=val, value="Green", fg="Green", command=clickradiobtn2)
# radiobtn2.pack()
# #指定選取締二個單選按鈕
# radiobtn2.select()
# #放入第三個單選按鈕
# radiobtn3 = Radiobutton(root, text="Pink", variable=val, value="Pink", fg="Pink", command=clickradiobtn3)
# radiobtn3.pack()

# #顯示被選取按鈕之value
# selectlabel = Label(root, textvariable=val, font={"Arial", 20})
# selectlabel.pack()
#點擊button跳出 New Windows
def createNewWindow():
    #建立新視窗 New Windows
    newWindow = Toplevel(root)
    #建立新label在New Windows 裡
    mylabel = Label(newWindow, text = "New Window")
    mylabel.pack()
    # #建立新button在 New Windows 裡
    # mybutton = Button(newWindow, text="New Window button")
    # mybutton.pack()

    #建立新button在 New Windows 裡
    destroybutton = Button(newWindow, text= "Quit", command=newWindow.destroy)
    destroybutton.pack()       #關閉視窗

    #建立hide button 在 New Windows 裡
    hidebutton = Button(newWindow, text = "Hide", command=root.iconify)
    hidebutton.pack()
    #建立hide button 在 New Windows 裡
    showbutton = Button(newWindow, text = "Show", command=root.deiconify)
    showbutton.pack()

    #建立 withdraw button 在 New Windows 裡
    withdrawbutton = Button(newWindow, text= "Withdraw Main Window", command=root.withdraw)
    withdrawbutton.pack()
    #建立 Kill button 在 New Windows 裡
    killmainbutton= Button(newWindow, text= "Quit Main Window", command=root.destroy)
    killmainbutton.pack()
    #執行新視窗程式
    newWindow.mainloop()

#點擊button產生 New Windows
createNewWindowbtn = Button(root, text="Click to Create New Windows!", command=createNewWindow)
createNewWindowbtn.pack()
#執行主程式                                    
root.mainloop()
'''
'''
def function(n, a=1, b=2):
    print(n+a+b)

#呼叫執行function，並給三個參數傳入該function
function(1,2,3) # result: 6 -> 1+2+3=6

#呼叫執行function，只給一個參數傳入該function
#當只給一個參數時，其餘參數會自動依照預設值來填入
function(4) # result: 7 -> 4+1+2=7
'''
'''
def function(n, a=1, b=2)
'''
'''
#*args 可變參數
def function(n, *args):
    print(n)
    print(args)

# 呼叫執行function，並給多個(>2個)參數值傳入該function
# 除了 1 為變數 n 外，其餘都是 *args 的輸入值
function(1,2,3,4,5,6,7)
'''
#**kwargs關鍵字可變參數
def function(*args, **kwargs):
    print(kwargs)
    print(args)

# 呼叫執行function，並給多個(>2個)參數值傳入該function
# 前四個值為*args可變參數，後兩個值為**kwargs關鍵字可變參數
function(1,2,3,4, num1=5, num2=10)