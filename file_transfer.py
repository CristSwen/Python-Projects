import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
import time
from datetime import timedelta



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")
        
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))
        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid padx and pady are the same
        #as the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in GUI using tkinter grid
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #Creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #Positions the Exit Button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0, 15))


    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0, END) will clear the content that is inserted in the entry widget,
        #This allows the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        # The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)
        

    def transferFiles(self):
        #Gets source directory
        source = self.source_dir.get()
        #Gets destination directory
        destination = self.destination_dir.get()
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each filein the source directory
        for i in source_files:
            #fileTime grabs the age of all the files in source_files. time gets the current date. delta is set to 0 time while delta2 is set to 24 hours
            fileTime = os.path.getmtime(source_files[i])
            time = datetime.datetime.now()
            delta = timedelta(
                days = 0,
                seconds = 0,
                microseconds = 0,
                milliseconds = 0,
                minutes = 0,
                hours = 0,
                weeks = 0
            )
            delta2 = timedelta(
                days = 1,
                seconds = 0,
                microseconds = 0,
                milliseconds = 0,
                minutes = 0,
                hours = 0,
                weeks = 0
            )
            #if time minus fileTime is less than or greater than delta2 and greaters than or equal to delta it will add the files
            if time - fileTime <= delta2 and time >= delta:
                #moves each file from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')


    def exit_program(self):
        #Root is the main GUI window, the Tkinter destroy method
        #Tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()