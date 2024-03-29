import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):

     def __init__(self, master):
         Frame.__init__(self, master)
         self.master.title("Web Page Generator")
         self.varText = StringVar()
         
         self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
         self.btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))
         #The button for the submit custom text
         self.btn = Button(self.master, text="Submit Custom Test", width=30, height=2, command=self.customHTML)
         self.btn.grid(row=2, column=3, padx=(10,10), pady=(10,10))
         self.lbl = Label(self.master, text="Enter custom or click the Default HTML page button", font=("Helvetica", 10), fg='black')
         self.lbl.grid(row=0, column=0, padx=(30,0), pady=(30.0))
         #The entry box for if people want to enter in their custom text
         self.txt = Entry(self.master, text=self.varText, font=("Helvetica", 16), fg="black")
         self.txt.grid(row=1, column=0, padx=(30,0), pady=(30,0))
         
         
     def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

     #The function that will allow the custom text typed to be displayed the HTML website
     def customHTML(self):
          #Grabs the custom text that was typed
          text = self.varText.get()
          htmlFile = open("index.html", "w")
          htmlContent = "<html>\n<body>\n<h1>" + text + "</h1>\n</body>\n</html>"
          #Writes the custom text on the page
          htmlFile.write(htmlContent)
          htmlFile.close()
          webbrowser.open_new_tab("index.html")





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
