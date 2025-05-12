import tkinter as tk
form=tk.Tk()
form.geometry('600x600')

canvas=tk.Canvas(width=500, height=500, bg="black")

canvas.create_oval(190,50,250,125, fill='beige', width=3) # Голова

canvas.create_line(210,70,210,90, fill='black', width=3) # Лев глаз
canvas.create_line(230,70,230,90, fill='black', width=3) # Прав глаз
canvas.create_line(210,110,230,110, fill='black', width=3) # Рот

canvas.create_rectangle(210,124,230,150, fill='beige',width=3) # Шея

canvas.create_rectangle(180,145,260,190, fill='turquoise',width=3) # Вверх туловища

canvas.create_oval(170,135,190,165, fill='turquoise', width=3) # Плечо (лв)
canvas.create_rectangle(125,140,173,160, fill='turquoise', width=3) # Вер руки (лв)
canvas.create_oval(115,137,135,163, fill='turquoise', width=3) # Локать (лв)
canvas.create_rectangle(70,142,117,157, fill='turquoise', width=3) # Низ руки (лв)
canvas.create_oval(50,138,70,160, fill='beige', width=3) # Ладонь (лв)

canvas.create_oval(250,135,270,165, fill='turquoise', width=3) # Плечо (пр)
canvas.create_rectangle(267,140,315,160, fill='turquoise', width=3) # Вер руки (пр)
canvas.create_oval(305,137,325,163, fill='turquoise', width=3) # Локать (пр)
canvas.create_rectangle(323,142,370,157, fill='turquoise', width=3) # Низ руки (пр)
canvas.create_oval(370,138,390,160, fill='beige', width=3) # Ладонь (пр)

canvas.create_rectangle(190,190,250,250, fill='turquoise',width=3) # Живот

canvas.create_rectangle(180,250,260,280, fill='blue',width=3) # Низ туловища

canvas.create_oval(180,270,210,300, fill='blue', width=3) # Скрепление ног (лв)
canvas.create_oval(230,270,260,300, fill='blue', width=3) # Скрепление ног (пр)
canvas.create_rectangle(235,290,255,355, fill='blue',width=3) # Нога (пр)
canvas.create_rectangle(185,290,205,355, fill='blue',width=3) # Нога (лв)
canvas.create_oval(180,350,210,365, fill='blue', width=3) # Колено (лв)
canvas.create_oval(230,350,260,365, fill='blue', width=3) # Колено (пр)
canvas.create_rectangle(235,360,255,430, fill='blue',width=3) # Ниж ноги (пр)
canvas.create_rectangle(185,360,205,430, fill='blue',width=3) # Ниж ноги (лв)
canvas.create_rectangle(165,430,205,445, fill='grey',width=3) # Стопа (лв)
canvas.create_rectangle(235,430,275,445, fill='grey',width=3) # Стопа (пр)

canvas.pack()
tk.mainloop()