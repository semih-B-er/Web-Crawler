import wikipedia
from  tkinter import *

uygulama = Tk()
uygulama.minsize(width=500,height=500)

başlık = Label(text="wikipedia özet",font=("Arial",30) )
başlık.pack(pady=10)
w_entry = Entry(width=40)
w_entry.pack(pady=5)
w_label = Label(text="",wraplength=450,justify="left",font=("Arial",12))
w_label.pack(pady=10)
def w_wikipedia():
    yaz = w_entry.get()
    x = wikipedia.summary(yaz , sentences = 3)
    w_label.config(text=x)
w_buton = Button(text="özetle",command=w_wikipedia)
w_buton.pack()

uygulama.mainloop()