from Tkinter import *

master = Tk()

canvas = Canvas(master, width=800, height=800, bg='white')
canvas.pack()

speed = input('Speed: ')


rectangle = canvas.create_rectangle(30,30,100,100, fill = 'green')


def up_arrow():
    canvas.move(rectangle, 0, -(speed))
    master.update()

def down_arrow():
    canvas.move(rectangle, 0, speed)
    master.update()


up = Button(master, text = 'Up', command = up_arrow)
up.pack()
up.place(x = 200,y=50)
down = Button(master, text = 'Down', command = down_arrow)
down.pack()
down.place(x = 200,y=150)


mainloop()
