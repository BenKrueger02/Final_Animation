from Tkinter import *
import time

master = Tk()

canvas = Canvas(master, width=800, height=800, bg='white')
canvas.pack()


circle = canvas.create_oval(30.0, 680.0, 100.0, 750.0, fill = 'green')
rectangle2 = canvas.create_rectangle(0, 750, 800, 800, fill = 'brown')

def up_arrow(event):
    for x in range (0, 15):
        canvas.move(circle, 0, -(12))
        master.update()
        time.sleep(0.1)
        print(canvas.coords(circle))
    for j in range(0, 15):
        canvas.move(circle, 0, (12))
        master.update()
        time.sleep(.1)




master.bind('<Up>', up_arrow)
mainloop()

