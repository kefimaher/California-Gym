import tkinter as tk
from PIL import ImageTk, Image
r = tk.Tk()
# Titre du page
r.title('Stock Net')
# canva

def cacher_rectangle():
    canvas.itemconfigure(a, state=tk.HIDDEN)

def afficher_rectangle():
    canvas.itemconfigure(a, state=tk.NORMAL)
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
maher = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')




a = canvas.create_rectangle(400, 10, 900, 500, fill="black")

b = canvas.create_rectangle(400, 400, 600, 500, fill="red")

# x = canvas.create_rectangle(400, 800, 1500, 146, fill="white")
# y = canvas.create_rectangle(400, 800, 1500, 146, fill="grey")
canvas.pack()
# button name + width
logout = tk.Button(r, text='Log out', width=10, command=r.destroy, background="white", fg="#683FA9")
logout.place(x=1380, y=10)
# button name + width
search = tk.Button(r, text='Search', width=10, background="#683FA9", fg="white")
search.place(x=1380, y=113)
# button name + width
test = tk.Button(r, text='test', width=10, background="#683FA9", fg="white")
test.place(x=420, y=113)
# button name + width
test2 = tk.Button(r, text='test 2', width=10, background="#683FA9", fg="white")
test2.place(x=550, y=113)

# button navbar a gauche vertical
#Item list : afficher un page contien la list des produit dans la table (id,image,nom,prix,quantite)
list = tk.Button(r, text='Items List', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=afficher_rectangle())
list.place(x=1, y=180)
#Button New items : ajouter un produit dans la table (id,image,nom,prix,quantite)
newitems = tk.Button(r, text='New Items', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=cacher_rectangle)
newitems.place(x=1, y=230)
#Tout les fisher
document = tk.Button(r, text='Document', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
document.place(x=1, y=280)
#Tout les entrant et sorant
exp = tk.Button(r, text='Expences', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
exp.place(x=1, y=330)
#Modifer
setting = tk.Button(r, text='Setting', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
setting.place(x=1, y=380)
r.mainloop()
# fg = coleur du text dans buton
# background = coleur du button
# highlightbackground = coleure du cadre du button
