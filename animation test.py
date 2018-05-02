from Tkinter import *

master = Tk()

canvas = Canvas(master, width=800, height=800, bg='white')
canvas.pack()

time = input('Time: ')
speed = input('Speed: ')

rectangle = canvas.create_rectangle(30,30,100,100, fill = 'green')


def return_move():
    canvas.move(rectangle, speed, 0)
    master.update()

for x in range(0, int(time)):
    if x < time:
        yes = input(':')
        if yes == 'right':
            return_move()
    else:
        print('nothing to move')

mainloop()