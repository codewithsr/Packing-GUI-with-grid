from tkinter import *
root = Tk()

root.geometry("245x255")

root.title("grid")


def b1_function():
    print("Your entered uservalue is:- ", user_value.get())   #.get() hume vahi value provide karata h jo humne bhari h
    print("Your entered passvalue is:- ", pass_value.get())


user = Label(root,text="Username")
passsword = Label(root, text="Password")
user.grid()                         #pack() ki hi tarah grid() bhi usi kaam ata h bas fayda itna h ki aap isme row and column ki positioning bhi change kar sakte h
passsword.grid(row=1)               #row and column by default 0 hote h. That's why humne uper user me rown nhi likha



#Various variable classes in timkter :- BooleanVar, Doublevar, IntVar, StringVar
user_value = StringVar()
pass_value = StringVar()

user_entry = Entry(root, textvariable=user_value)
pass_entry = Entry(root, textvariable=pass_value)
user_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

b1 = Button(root, text="Submit", command=b1_function)
b1.grid()




root.mainloop()