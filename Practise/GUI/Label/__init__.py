# label = an area widget that holds text and/or an image  within a window

from tkinter import *

window = Tk()
window.geometry('500x500')

label = Label(window,text='Currecy Converter')
# label.place(x=100,y=0)
label.pack()
mainloop()
