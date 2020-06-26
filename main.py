import tkinter as tk
import os

HEIGHT = 500
WIDTH = 600

def openFile1():
    os.startfile("D:\Work Internship\Aspirathon\GUI-master\prototype\DB Scripts\teams_block.exe")
    exec(open('prob.py').read())
def openFile2():
    os.startfile("D:\Work Internship\Aspirathon\GUI-master\dns_change.exe - Shortcut")
    exec(open('prob.py').read())
        
def openFile3():
    os.startfile("D:\Work Internship\ProcessExplorer\procexp64.exe")
    exec(open('prob.py').read())

def openFile11():
    print("Showing solution")
    
def openFile21():
    print("Thank You")

root = tk.Tk()
root.title("Learning By doing")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=1, relheight=0.2, anchor='n')
lb1 = tk.Button(frame, text = 'Teams Not working Lab',font=10, command = lambda: openFile1())
lb1.place(x=10, y=10)

lb2 = tk.Button(frame,text = 'DNS Resolution LAB',font=10, command = lambda: openFile2())
lb2.place( x=220, y=10)

lb3 = tk.Button(frame,text = 'Os Memory Leak Lab',font=10, command = lambda: openFile3())
lb3.place(x=400,y=10)
root.mainloop()
    
