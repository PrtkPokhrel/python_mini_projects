# import tkinter as tk
#
# window = tk.Tk()
# window.geometry('500x500')  # sets the dimension of the window
# label = tk.Label(window, text='This is the title', font=('Helvetica', 20, 'bold'))
# window.title('This is the fist GUI')  # sets the title of the window
# label.pack()
# window.mainloop()

"""
import tkinter as tk

window = tk.Tk()  # initializes Tk()
window.geometry('500x500')  # sets the dimension of the windows
window.title('Practise')  # sets the title
label = tk.Label(window, text='Welcome to the application', font=('Helvetica', 18))

textbox = tk.Text(window, height=4, font=('Arial', 18))  # sets the text box and gives the height in number or line

label.pack(padx=30, pady=30)  # essential to show the label in the window just like java
textbox.pack(padx=30, pady=30)
window.mainloop()  # runs an infinite loop so that the window can always be seen unless exited using cross arrow
"""

import tkinter as tk

window = tk.Tk()
dimension = window.geometry('500x500')

title = window.title('Practise')

label = tk.Label(window, text='My Notepad', font=('Bold', 18))

textbox = tk.Text(window, height=3, font=('Arial', 12))

myentry = tk.Entry(window)

button = tk.Button(window, text='Click me')

label.pack(padx=20, pady=20)
button.pack()
textbox.pack()
myentry.pack()
window.mainloop()
