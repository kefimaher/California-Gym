import tkinter as tk
import pandas as pd

df = pd.DataFrame()
# print(df)


from PIL import ImageTk, Image
r = tk.Tk()

r.title('MY Iptv')

img = Image.open('/home/test/Desktop/gitproject/GStock/assets/Photos/1.jpeg')

bg = ImageTk.PhotoImage(img)

# demention de page
r.geometry("1500x800")
background_label = tk.Label(r, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# canva
canvas = tk.Canvas(r, width=1500, height=800, background='grey')
# text
txt = canvas.create_text(200, 100, text="Cible", font="Arial 16 italic", fill="black")
# page content
canvas.create_rectangle(0,800,400,0,fill="#3E4146")
# barre de navigation a gauche
canvas.create_rectangle(400,800,1500,0,fill="white")
# barre de navigation a haut a droite
canvas.create_rectangle(400,70,1500,0,fill="#55259F")
# barre de navigation a haut a droite
canvas.create_rectangle(0,70,400,0,fill="#50337D")
# line vertical
canvas.create_line(400, 150, 1500, 150,fill="#492089" , width=2)
canvas.pack()
# button name + width
button = tk.Button(r, text='Close', width=10, command=r.destroy)
# les cordonne du button
button.place(x=1380,y=10)
# button name + width
button = tk.Button(r, text='maher', width=10, command="")
# les cordonne du button
button.place(x=10,y=10)

r.mainloop()


