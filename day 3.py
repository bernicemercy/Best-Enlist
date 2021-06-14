from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Registration Screen")
window.geometry('300x400')
window.configure(background = "#ECFFDC")

a = Label(window,text="First Name",background="#ECFFDC",foreground="black").grid(row=0,column=0)
b = Label(window,text="last Name",background="#ECFFDC",foreground="black").grid(row=1,column=0)

# gender radiobox
l = Label(window,text="Gender : ",background="#ECFFDC",foreground="black").grid(row=2,column = 0)
l1 = Radiobutton(window,text="M",background="#ECFFDC",foreground="black",).grid(row=3,column = 0)
l2 = Radiobutton(window,text="F",background="#ECFFDC",foreground="black",).grid(row=4,column = 0)
l3 = Radiobutton(window,text="T",background="#ECFFDC",foreground="black").grid(row=5,column = 0)

c = Label(window,text="Email ID",background="#ECFFDC",foreground="black").grid(row=6,column=0)
d = Label(window,text="Contact number",background="#ECFFDC",foreground="black").grid(row=7,column=0)
e = Label(window,text="Father's Name",background="#ECFFDC",foreground="black").grid(row=8,column=0)
f = Label(window,text="Occupation",background="#ECFFDC",foreground="black").grid(row=9,column=0)
g = Label(window,text="Contact number",background="#ECFFDC",foreground="black").grid(row=10,column=0)
h = Label(window,text="Mother's Name",background="#ECFFDC",foreground="black").grid(row=11,column=0)
i = Label(window,text="Occupation",background="#ECFFDC",foreground="black").grid(row=12,column=0)
j = Label(window,text="Contact Number",background="#ECFFDC",foreground="black").grid(row = 13, column = 0)

# drop down menu box
m = Label(window,text ="Course",background="#ECFFDC",foreground="black").grid(row = 15, column =0)
menu = StringVar()
menu.set("Select the course")

drop = OptionMenu(window,menu,"C++","C","C#","Python","Java","JavaScript").grid(row=15,column=1)

#entry box

a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = Entry(window).grid(row = 6,column = 1)
d1 = Entry(window).grid(row = 7,column = 1)
e1 = Entry(window).grid(row = 8,column = 1)
f1 = Entry(window).grid(row = 9,column = 1)
g1 = Entry(window).grid(row = 10,column = 1)
h1 = Entry(window).grid(row = 11,column = 1)
i1 = Entry(window).grid(row = 12,column = 1)
j1 = Entry(window).grid(row = 13,column = 1)


def clicked():
    res = "Welcome to Best Enlist"
    lbl.configure(text = res)
btn = ttk.Button(window,text="submit").grid(row = 17,column = 2)
window.mainloop()
