import tkinter as tk  
from tkinter import messagebox  
  
def show_message():  
    messagebox.showinfo("Message", "这是一个信息对话框")  
  
def button_click_1():  
    print("按钮1被点击了")  
  
def button_click_2():  
    print("按钮2被点击了")  
  
def button_click_3():  
    print("按钮3被点击了")  
  
# 创建主窗口  
root = tk.Tk()  
root.title("我的对话框和按钮")  
  
# 创建三个按钮，并分别绑定到三个函数  
button1 = tk.Button(root, text="按钮1", command=button_click_1)  
button1.pack()  
  
button2 = tk.Button(root, text="按钮2", command=button_click_2)  
button2.pack()  
  
button3 = tk.Button(root, text="按钮3", command=button_click_3)  
button3.pack()  
  
# 当窗口关闭时，结束程序  
root.protocol("WM_DELETE_WINDOW", root.quit)  
  
# 显示窗口  
root.mainloop()