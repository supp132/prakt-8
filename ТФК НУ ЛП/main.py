from tkinter import *

window = Tk()
window.title("Shadow Fiend")

canvas = Canvas(window, width=600, height=600, bg="black")
canvas.pack()

canvas.create_oval(200,150,400,350, fill="#220000", outline="red", width=3)

canvas.create_oval(240,220,290,260, fill="red")
canvas.create_oval(310,220,360,260, fill="red")

canvas.create_polygon(200,150, 170,80, 240,150, fill="darkred")
canvas.create_polygon(400,150, 430,80, 360,150, fill="darkred")

canvas.create_arc(250,260,350,320,start=0,extent=-180,style=ARC,outline="red",width=3)

canvas.create_line(300,350,300,450,fill="red",width=2)
canvas.create_line(260,360,240,440,fill="red",width=2)
canvas.create_line(340,360,360,440,fill="red",width=2)

canvas.create_text(300,500, text="Shadow Fiend", fill="red", font=("Arial",20))

window.mainloop()