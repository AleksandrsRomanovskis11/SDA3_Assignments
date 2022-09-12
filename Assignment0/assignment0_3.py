from cgitb import text
from tkinter import*
from turtle import clear

root=Tk()
var = StringVar()
root.title("Assignemnet0_3")
root.geometry("300x200")
label= Label(root, textvariable=var)
var.set ("Type the name of a country:")
label.pack(pady= 10)

#clear function 

def clear():
    text_box.delete(1.0,END)
    root.destroy()

text_box = Text(root, width=20, height =2, font=("Arial"))
text_box.pack(pady= 40)
button_ok = Frame (root)
button_ok.pack()

clear_button = Button(button_ok, text = "Cancel", command= clear)
clear_button.grid(row = 0, column=0)



root.mainloop()