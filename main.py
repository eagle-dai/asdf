import tkinter as tk
from tkinter import *
import ctypes
import win32con
from ghk import GlobalHotKeys
import _thread
import game


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

        # user32 = ctypes.windll.user32
        # if user32.RegisterHotKey(None, 1, win32con.MOD_SHIFT, win32con.VK_F1):
        #     print("hotkey registered")
        # else:
        #     print("Cannot register hotkey")
        #
        # root.protocol("WM_HOTKEY", self.hotkey_received)

    def hotkey_received(self):
        print("hotkey")

    @GlobalHotKeys.register(GlobalHotKeys.VK_F1, GlobalHotKeys.MOD_SHIFT)
    def hello_world():
        print("Hello World!")
        root.destroy()

    def create_widgets(self):
        self.user = Label(self, text="用户:")
        self.user.grid(row=0, sticky=EW)
        self.userv = StringVar()
        self.usere = Entry(self, textvariable=self.userv)
        self.usere.grid(row=0, column=1, sticky=EW, columnspan=3)

        self.pwd = Label(self, text="密码:")
        self.pwd.grid(row=1, sticky=EW)
        self.pwdv = StringVar()
        self.pwde = Entry(self, textvariable=self.pwdv)
        self.pwde.grid(row=1, column=1, sticky=EW, columnspan=3)

        Label(self, text="副本:").grid(row=2, sticky=EW)
        fbf = Frame(self)
        fbf.grid(row=2, column=1, sticky=EW, columnspan=3)
        self.fb = self.creat_fb(fbf)


        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "挂机"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=3)

        self.quit = tk.Button(self, text="退出", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=3, column=3)

        self.start_in_char= tk.Button(self)
        self.start_in_char["text"] = "开始"
        self.start_in_char["command"] = self.say_hi
        self.start_in_char.grid(row=3, column=1)

        self.start_in_char= tk.Button(self)
        self.start_in_char["text"] = "战斗"
        self.start_in_char["command"] = self.say_hi
        self.start_in_char.grid(row=3, column=2)

    def say_hi(self):

        print("hi there, everyone!")
        game.start_guajji()


    def print_item(self, event):
        print(self.fb.get(self.fb.curselection()))
        print(self.usere.get())
        print(self.pwde.get())

    def creat_fb(self, frame):
        var = StringVar()
        lb = Listbox(frame, height=5, selectmode=BROWSE, listvariable=var)
        lb.bind('<ButtonRelease-1>', self.print_item)
        list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        for item in list_item:
            lb.insert(END, item)
        scrl = Scrollbar(frame)
        scrl.pack(side=RIGHT, fill=Y)
        lb.configure(yscrollcommand=scrl.set)  # 指定Listbox的yscrollbar的回调函数为Scrollbar的set，表示滚动条在窗口变化时实时更新
        lb.pack(side=LEFT, fill=BOTH)
        scrl['command'] = lb.yview  # 指定Scrollbar的command的回调函数是Listbar的yview
        return lb

def create_app():
    root = tk.Tk()
    root.resizable(width=False, height=False)
    root.title('ops')
    # root.iconbitmap('ic.ico')
    # root.geometry('500x300+500+200')
    app = Application(master=root)
    try:
        _thread.start_new_thread(GlobalHotKeys.listen, ())
    except:
        print("Error: 无法启动线程")
        exit(-1)
    return app

if __name__ == "__main__":
    app = create_app()
    root = app.master
    app.mainloop()