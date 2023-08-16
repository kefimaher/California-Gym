import tkinter as tk
import webbrowser
from PIL import ImageTk, Image
r = tk.Tk()
# Titre du page
r.title('Stock Net')
#les lien des page
def dashbroad_visibility():
 dashbroad.place(x=400, y=145)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 news.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def item_visibility():
 items.place(x=400, y=145)
 setting.place(x=1500, y=800)
 dashbroad.place(x=1500, y=800)
 news.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def settings_visibility():
 setting.place(x=400, y=145)
 dashbroad.place(x=1500, y=800)
 items.place(x=1500, y=800)
 news.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def news_visibility():
 news.place(x=400, y=145)
 dashbroad.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def document_visibility():
 news.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 document.place(x=400, y=145)
 exp.place(x=1500, y=800)
 dashbroad.place(x=1500, y=800)
def exp_visibility():
 news.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 document.place(x=1500, y=800)
 exp.place(x=400, y=145)
 dashbroad.place(x=1500, y=800)
#button search
def on_submit():
    entered_text = search_zone.get()
    result_label.config(text="Vous avez saisi : " + entered_text)
    search_zone.delete(0, "end")
    search_zone.insert(0, "chercher un produit")
def on_entry_click(event):
    if search_zone.get() == "chercher un produit":
        search_zone.delete(0, "end")  # Delete current text in the entry
#button reset
def reset():
    quantitezone.delete(0, tk.END)
    prixezone.delete(0, tk.END)
    autre.delete(0, tk.END)
#canvas
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
Title = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')
# x = canvas.create_rectangle(400, 800, 1500, 146, fill="white")
# y = canvas.create_rectangle(400, 800, 1500, 146, fill="grey")
canvas.pack()
# button name + width
logout = tk.Button(r, text='Déconnexion', width=10, command=r.destroy, background="white", fg="#683FA9")
logout.place(x=1380, y=10)
# button name + width
search = tk.Button(r, text='OK', width=10, background="#683FA9", fg="white", command=on_submit)
search.place(x=1380, y=113)
# button name + width
test1 = tk.Button(r, text='test1', width=10, background="#683FA9", fg="white")
test1.place(x=420, y=113)
# button name + width
test2 = tk.Button(r, text='test2', width=10, background="#683FA9", fg="white")
test2.place(x=550, y=113)
# button navbar a gauche vertical
#tableau du bord
dashbroad = tk.Button(r, text='Tableau de bord', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=dashbroad_visibility)
dashbroad.place(x=1, y=180)
#Item list : afficher un page contien la list des produit dans la table (id,image,nom,prix,quantite)
items = tk.Button(r, text='Liste des produits', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=item_visibility)
items.place(x=1, y=230)
#Button New items : ajouter un produit dans la table (id,image,nom,prix,quantite)
news = tk.Button(r, text='Importer', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=news_visibility)
news.place(x=1, y=280)
#export
exp = tk.Button(r, text='Exporter', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white")
exp.place(x=1, y=330)
#historique
document = tk.Button(r, text='Historique', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=document_visibility)
document.place(x=1, y=380)
#parametre
setting = tk.Button(r, text='Parametre', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=settings_visibility)
setting.place(x=1, y=700)
#les pages
dashbroad = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
dashbroad.place(x=400, y=145)
setting = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
items = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
exp  = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
document = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
news = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
#contenu du chaque page
dashbroad_text = tk.Label(dashbroad, text="Contenu tableau du broad ", font=("Arial", 20), fg="#683FA9", background="#BBBBBB")
dashbroad_text.place (x=5, y=10)
items_page_text = tk.Label(items, text="Contenu du page items ", font=("Arial", 20), fg="#683FA9", background="#BBBBBB")
items_page_text.place (x=5, y=10)
new_page_text = tk.Label(news, text="Ajouter un produit / matreille", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
new_page_text.place (x=400, y=10)
doc_page_text = tk.Label(document, text="Contenu du page document", font=("Arial", 20), fg="#683FA9", background="#BBBBBB")
doc_page_text.place (x=5, y=10 )
exp_page_text = tk.Label(exp, text="Contenu du page export ", font=("Arial", 20), fg="#683FA9", background="#BBBBBB")
exp_page_text.place (x=5, y=10 )
setting_page_text = tk.Label(setting, text="Contenu du page setting", font=("Arial", 20), fg="#683FA9", background="#BBBBBB")
setting_page_text.place(x=5, y=10)
#serach zone button
search_zone = tk.Entry(r)
search_zone.insert(10, "chercher un produit")
search_zone.place(x=1200, y=117)
result_label = tk.Label(r, text="ZFQVQDVQDV")
result_label.place(x=0, y=10)
search_zone.bind("<FocusIn>", on_entry_click)
#footer du page
footer_page_text = tk.Label(canvas, text="This application Devlopped by Kefi Maher using Python 3.8.10 ", font=("Arial", 9), fg="white", background="#3E4146")
footer_page_text.place(x=5, y=770)
#page new items
#list des option
#ajouter produit
produitajouter = tk.Label(news, text="Produit ajouté en inventaire :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
produitajouter.place(x=5, y=140)
#quantite
quantite = tk.Label(news, text="Quantite:", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
quantite.place(x=350, y=140)
#prix
prix = tk.Label(news, text="Prix pour un seul:", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
prix.place(x=600, y=140)
#list option
options = ["Fraises à métaux", "Abrasifs", "Vis", "VISSEUSE","Electrique", "Colles adhésifs", "Outils pneumatiques", "Scies circulaires", "Ponceuses"]
liste = tk.Listbox(news, bg="#BBBBBB", fg="black", width=20, font=("Arial", 13))
for option in\
        options:
    liste.insert(tk.END, option)
liste.place(x=1, y=180)
#search zone pour quantite
quantitezone = tk.Entry(news)
quantitezone.insert(10, "")
quantitezone.place(x=500, y=180)
#search zone pour prix
prixezone = tk.Entry(news)
prixezone.insert(10, "")
prixezone.place(x=850, y=180)
#butoon ajouter
produitajouterbutton = tk.Button(news, text='Ajouter', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white")
produitajouterbutton.place(x=200, y=600)
#button annuler
produitannulerbutton = tk.Button(news, text='Annuler', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white", command=reset)
produitannulerbutton.place(x=600, y=600)
#button autre
autrebutton = tk.Button(news, text='Autre produit / matreille ', width=20, background="#3E4146", fg="white", activebackground="#3D0E89", activeforeground="white")
autrebutton.place(x=500, y=300)
#text zone pour autre
autre = tk.Entry(news)
autre.insert(10, "")
autre.place(x=750, y=305)
r.mainloop()

