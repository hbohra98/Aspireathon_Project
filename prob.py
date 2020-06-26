import tkinter as tk
import os
import time
import countdown1
HEIGHT = 500
WIDTH = 600

root1 = tk.Toplevel()
root1.title("Lab1")

canvas1 = tk.Canvas(root1, height=HEIGHT, width=WIDTH)
canvas1.pack()

background_image1 = tk.PhotoImage(file='landscape.png')
background_label1 = tk.Label(root1, image=background_image1)
background_label1.place(relwidth=1, relheight=1)



frame1 = tk.Frame(root1, bg='#80c1ff', bd=10)
frame1.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.2, anchor='n')

lb10 = tk.Button(frame1, text = 'Submit Test',font=10, command = lambda: openFile11())
lb10.place(x=10, y=10)

lb11 = tk.Button(frame1, text = 'Show Solution',font=10, command = lambda: openFile11())
lb11.place(x=200, y=10)

lb21 = tk.Button(frame1,text = 'Exit',font=10, command = lambda: openFile21())
lb21.place( x=500, y=10)

exec(open('countdown1.py').read())
label = tk.Label(frame1, text="Time Up", width=40)
label.place(x=200,y=10)

root1.mainloop()
    
