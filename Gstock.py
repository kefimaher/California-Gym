import tkinter as tk
from PIL import ImageTk, Image
r = tk.Tk()
# Titre du page
r.title('Gestion Du Stock')
# canva
canvas = tk.Canvas(r, width=1500, height=800, background='grey')
# line
canvas.create_line(400, 0, 400, 800)
# text
txt = canvas.create_text(200, 100, text="Cible", font="Arial 16 italic", fill="black")
# page content
canvas.create_rectangle(0,800,400,0,fill="#3E4146")
# barre de navigation a gauche
canvas.create_rectangle(400,800,1500,0,fill="white")
# barre de navigation a haut a droite
canvas.create_rectangle(400,70,1500,0,fill="#55259F")
# barre de navigation a haut a droite
canvas.create_rectangle(0,70,400,0,fill="#4  92089")
canvas.create_line(400,145,1500,145, fill="#492089", width=2)
canvas.pack()


# button name + width
button = tk.Button(r, text='Close', width=10, command=r.destroy)
# les cordonne du button
button.place(x=1380, y=10)
# button name + width
button = tk.Button(r, text='test 1', width=10, background="#683FA9", fg="white", highlightbackground="red", highlightcolor="red")
# les cordonne du button
button.place(x=1380, y=113)
# button name + width
button = tk.Button(r, text='test', width=10, background="#683FA9", fg="white")
# les cordonne du button
button.place(x=420, y=113)
# button name + width
button = tk.Button(r, text='test', width=10, background="#683FA9", fg="white")
# les cordonne du button
button.place(x=550, y=113)
r.mainloop()
