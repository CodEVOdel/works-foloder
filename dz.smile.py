import tkinter as tk

def circle(cnv:tk.Canvas,x:int,y:int,radius:int,color:str='yellow'):
    cnv.create_oval(x-radius//2,y-radius//2,x+radius//2,y+radius//2, fill=color,width=3)
def circle_arc(cnv:tk.Canvas,x:int,y:int,radius:int,color:str='yellow'):
    cnv.create_arc(x-radius//2,y-radius//2,x+radius//2,y+radius//2, start=180, extent=180, fill='red',width=3)

def eye(cnv:tk.Canvas,x:int,y:int,radius:int):
    circle(cnv,x-30,y-20,radius,'white')
    circle(cnv,x+30,y-20,radius,'white')
    circle(cnv,x-25,y-20,radius//2,'blue')
    circle(cnv,x+25,y-20,radius//2,'blue')

def head(x:int,y:int,radius:int):
    circle(canvas,x,y,radius)   
    eye(canvas,x=x,y=y,radius=40)
    circle_arc(canvas,x=x,y=y+20,radius=radius//2)

form=tk.Tk()
form.geometry('600x600')
form.update()
x:int = form.winfo_width()//2
y:int= form.winfo_height()//2


canvas=tk.Canvas(width=600, height=600, bg="black")
for i in range(100):
    canvas.move(head,10,y,100)
    canvas.after(100)


# canvas.create_arc(70,110,170,180,start=180, extent=180, fill="red", width=3)
# canvas.create_oval(90,100,110,120, fill="blue", width=3)
# canvas.create_oval(125,130,165,80,fill="white",width=3)
# canvas.create_oval(135,100,155,120,fill="blue",width=3)
canvas.pack()
tk.mainloop()