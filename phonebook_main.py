



from tkinter import *
import tkinter as tk
from tkinter import messagebox

import phonebook_gui
import phonebook_func


# Frame is the tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #defining the master frame config
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #This centerWIndow method will center the app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if the user click the upper corner, "X" on windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        phonebook_gui.load_gui(self)

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q", command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo")
        menubar.add_cascade(label="Help", menu=helpmenu)


        self.master.config(menu=menubar, borderwidth='1')
        







if __name__ == "__main__":
    #This creates the window
    root = tk.Tk()
    App = ParentWindow(root)
    # The window will disappear unless we have this loop
    root.mainloop()
                       
