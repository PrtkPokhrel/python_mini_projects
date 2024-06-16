import tkinter as tk

window = tk.Tk()
window.geometry('500x500')  # sets the dimension of the window
label = tk.Label(window, text='This is the title', font=('Helvetica', 20, 'bold'))
window.title('This is the fist GUI')  # sets the title of the window
label.pack()
window.mainloop()
