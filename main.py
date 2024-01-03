from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20,pady=20)

# Labels
my_label = Label(text="is equal to")
my_label.grid(column=0,row=1)

mile_input = Entry(width=10)
mile_input.grid(column=1,row=0)

km_result_label = Label(text=0)
km_result_label.grid(column=1,row=1)

my_label2 = Label(text="Miles")
my_label2.grid(column=2,row=0)

my_label3 = Label(text="Km")
my_label3.grid(column=2,row=1)


def calculate():
    mile = int(mile_input.get())
    km = mile * 1.609344
    km_result_label.config(text=f"{km} km")

button = Button(text="Calculate", command=calculate)
button.grid(column=1,row=2)






window.mainloop()
