
from tkinter import *
from turtle import bgcolor, delay

root = Tk()
root.title("Assignment0_1")
var = StringVar()
label = Label(root, textvariable=var)
root.geometry("400x400")

var.set("What has to be assembled ?")
label.pack()


def Close():
    root.destroy()


exit_button = Button(root, text="Exit", command=Close)  
exit_button.pack(pady=20)



c = Canvas()
c.pack()
c.create_rectangle(0, 10, 100, 100, outline="#fb5", fill="#f128cb")
c.create_rectangle(200, 10, 100, 100, outline="#fb5", fill="#fb5")
c.create_rectangle(300, 10, 200, 100, outline="#fb5", fill="#2a22a2")

c.create_oval(0,200,100, 100, outline="#fb5", fill="#F9FF33")
c.create_oval(200,200,100, 100, outline="#fb5", fill="#6EFF33")
c.create_oval(300,200,200, 100, outline="#fb5", fill="#FF3333")




root.mainloop()