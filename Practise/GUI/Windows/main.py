from tkinter import *

window = Tk()   # instantiate an instance of the window
window.geometry('500x500') # sets the dimension of the window
window.title('Hello world')  # sets the title of the window

icon = PhotoImage(file='intFloat.png')  # converts the png to PhotoImage type which is only acceptable in tkinter
window.iconphoto(True, icon)   # sets the icon to the photo

window.config(background='#a1f084')   # sets the background color according to the hex value

window.mainloop()  # places the window on the screen also listens for the event

