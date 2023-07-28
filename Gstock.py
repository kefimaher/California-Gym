import tkinter as tk
from PIL import ImageTk, Image
r = tk.Tk()
# Titre du page
r.title('Stock Net')
# canva
canvas = tk.Canvas(r, width=1500, height=800, background='grey')
# line
canvas.create_line(400, 0, 400, 800)
# barre de navigation a gauche
canvas.create_rectangle(0, 800, 400, 0, fill="#3E4146")
# page content
canvas.create_rectangle(400, 800, 1500, 0, fill="white")
# barre de navigation a haut a droite
canvas.create_rectangle(400, 70, 1500, 0, fill="#55259F")
# barre de navigation a haut a droite
canvas.create_rectangle(0, 70, 400, 0, fill="#492089")
canvas.create_line(400, 145, 1500, 145, fill="#492089", width=2)
canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')

canvas.pack()

# button name + width
button = tk.Button(r, text='Log out', width=10, command=r.destroy, background="white", fg="#683FA9")
button.place(x=1380, y=10)
# button name + width
button = tk.Button(r, text='Search', width=10, background="#683FA9", fg="white")
button.place(x=1380, y=113)
# button name + width
button = tk.Button(r, text='button2', width=10, background="#683FA9", fg="white")
button.place(x=420, y=113)
# button name + width
button = tk.Button(r, text='button3', width=10, background="#683FA9", fg="white")
button.place(x=550, y=113)

# button navbar a gauche vertical
#Item list : afficher un page contien la list des produit dans la table (id,image,nom,prix,quantite)
button = tk.Button(r, text='Items List', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
button.place(x=1, y=180)
#Button New items : ajouter un produit dans la table (id,image,nom,prix,quantite)
button = tk.Button(r, text='New Items', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
button.place(x=1, y=230)
#Tout les fisher
button = tk.Button(r, text='Document', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
button.place(x=1, y=280)
#Tout les entrant et sorant
button = tk.Button(r, text='Expences', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
button.place(x=1, y=330)
#Modifer
button = tk.Button(r, text='Setting', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
button.place(x=1, y=380)

r.mainloop()

# fg = coleur du text dans buton
# background = coleur du button
# highlightbackground = coleure du cadre du button
