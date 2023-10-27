import tkinter as tk
import datetime
r = tk.Tk()
date_et_heure_actuelles = datetime.datetime.now()
# Titre du page
r.title('G-Stock')
#nombrepiece lire
def dashbroad_visibility():
 dashbroad.place(x=400, y=145)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 news.place(x=1500, y=800)
 exp.place(x=1500, y=800)
 produitarecherche.place(x=1500, y=800)
 r1.place(x=1500, y=800)
 r2.place(x=1500, y=800)
 dashbroadstatic1.place(x=100, y=350)
 dashbroadstatic2.place(x=400, y=350)
 dashbroadstatic3.place(x=700, y=350)
 search_zone.delete(0, "end")
 search_zone.insert(0, "")
 produitarecherche.delete(0, "end")
def item_visibility():
 items.place(x=400, y=145)
 setting.place(x=1500, y=800)
 dashbroad.place(x=1500, y=800)
 news.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def settings_visibility():
 setting.place(x=400, y=145)
 dashbroad.place(x=1500, y=800)
 items.place(x=1500, y=800)
 news.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def news_visibility():
 news.place(x=400, y=145)
 dashbroad.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 exp.place(x=1500, y=800)
def document_visibility():
 news.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 exp.place(x=1500, y=800)
 dashbroad.place(x=1500, y=800)
def exp_visibility():
 news.place(x=1500, y=800)
 setting.place(x=1500, y=800)
 items.place(x=1500, y=800)
 exp.place(x=400, y=145)
 dashbroad.place(x=1500, y=800)
#button search
def on_submit():
    entered_text = search_zone.get()
    produitarecherche.delete(0, "end")
    if ((entered_text!="chercher un personne")and(entered_text!="")):
       produitarecherche.insert(10, entered_text)
       produitarecherche.place(x=290, y=604)
       r1.place(x=10, y=600)
       r2.place(x=600, y=600)
       search_zone.delete(0, "end")
       search_zone.insert(0, "chercher un personne")
       news.place(x=1500, y=800)
       setting.place(x=1500, y=800)
       items.place(x=1500, y=800)
       document.place(x=1500, y=800)
       dashbroad.place(x=400, y=145)
       dashbroadstatic1.place(x=100, y=350)
       dashbroadstatic2.place(x=400, y=350)
       dashbroadstatic3.place(x=700, y=350)
def on_entry_click(event):
    if search_zone.get() == "chercher un personne":
       search_zone.delete(0, "end")  # Delete current text in the entry
#button reset
def reset():
    quantitezone.delete(0, tk.END)
    prixezone.delete(0, tk.END)
    autre.delete(0, tk.END)
    numerofacture.delete(0, tk.END)
def exportfonction():
    produitex = exportproduit.get()
    quantiteex = exportquantite.get()
    prixex = exportprix.get()
    if ((produitex!="")and(quantiteex!="")and(prixex!="")):
     xexport = open("export.txt", "a+")
     xexport.write("\n"+produitex+"                   "+quantiteex+"                    "+prixex);
     xexport.close()
def resetexport():
    exportproduit.delete(0, tk.END)
    exportquantite.delete(0, tk.END)
    exportprix.delete(0, tk.END)
#canvas
canvas = tk.Canvas(r, width=1500, height=800, background='grey')
# line
canvas.create_line(400, 0, 400, 800)
# barre de navigation a gauche
canvas.create_rectangle(0, 800, 400, 0, fill="#3E4146")
# page content
canvas.create_rectangle(400, 800, 1500, 0, fill="#3E4146")
# barre de navigation a haut a droite
canvas.create_rectangle(400, 70, 1500, 0, fill="black")
# barre de navigation a haut a droite
canvas.create_rectangle(0, 70, 400, 0, fill="#D3CD00")
canvas.create_line(400, 145, 1500, 145, fill="#492089", width=2)
Title = canvas.create_text(200, 40, text="G-Stock", fill="black", font='Helvetica 15 bold')
#date et heure
heure_actuelle = date_et_heure_actuelles.now()
minutes_actuelles = date_et_heure_actuelles.minute
date_actuelle = date_et_heure_actuelles.date()
# button name + width
search = tk.Button(r, text='Chercher', width=10, background="#959100", fg="black", command=on_submit, activebackground="#D3CD00", activeforeground="black", highlightbackground="#DFD800")
search.place(x=1380, y=113)
# button name + width
test1 = tk.Button(r, text='Test', width=10, background="#959100", fg="black", activebackground="#D3CD00", activeforeground="black", highlightbackground="#DFD800")
test1.place(x=420, y=113)
# button name + width
test2 = tk.Button(r, text='Test', width=10, background="#959100", fg="black", activebackground="#D3CD00", activeforeground="black", highlightbackground="#DFD800")
test2.place(x=550, y=113)
# button navbar a gauche vertical
#tableau du bord
dashbroad = tk.Button(r, text='Tableau du Bord', width=46, background="#D3CD00", fg="black", highlightbackground="red", activebackground="#EED153", activeforeground="black", command=dashbroad_visibility)
dashbroad.place(x=1, y=180)
#Item list : afficher un page contien la list des produit dans la table (id,image,nom,prix,quantite)
items = tk.Button(r, text='Liste des personnes', width=46, background="#D3CD00", fg="black", highlightbackground="#3E4146", activebackground="#D3CD00", activeforeground="black", command=item_visibility)
items.place(x=1, y=230)
#Button New items : ajouter un produit dans la table (id,image,nom,prix,quantite)
news = tk.Button(r, text='Ajouter un presonne', width=46, background="#D3CD00", fg="black", highlightbackground="#3E4146", activebackground="#D3CD00", activeforeground="black", command=news_visibility)
news.place(x=1, y=280)
#export
exp = tk.Button(r, text='Exporter', width=46, background="#D3CD00", fg="black", highlightbackground="#3E4146", activebackground="#D3CD00", activeforeground="black", command=exp_visibility)
exp.place(x=1, y=330)
setting = tk.Button(r, text='Parametre', width=46, background="#D3CD00", fg="black", highlightbackground="#3E4146", activebackground="#D3CD00", activeforeground="black", command=settings_visibility)
setting.place(x=1, y=700)
#les pages
dashbroad = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
dashbroad.place(x=400, y=145)
setting = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
items = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
exp= tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
document = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
news = tk.Frame(canvas, width=1500, height=800, background='#BBBBBB')
#contenu du chaque page
dashbroad_text = tk.Label(dashbroad, text="Tableau du Bord", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
dashbroad_text.place (x=350, y=20)
items_page_text = tk.Label(items, text="Contenu du page items ", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
items_page_text.place (x=350, y=20)
new_page_text = tk.Label(news, text="Ajout d'un Nouveau Produit", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
new_page_text.place (x=350, y=20)
doc_page_text = tk.Label(document, text="Contenu du page document", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
doc_page_text.place (x=350, y=20)
exp_page_text = tk.Label(exp, text="Vente du Nouveau Produit", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
exp_page_text.place (x=350, y=20)
setting_page_text = tk.Label(setting, text="Parametre", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
setting_page_text.place (x=350, y=20)
#footer du page
footer_page_text = tk.Label(canvas, text="This application Devlopped by Kefi Maher using Python 3.8.10 ", font=("Arial", 10), fg="white", background="#3E4146")
footer_page_text.place(x=5, y=770)
#page new items
#list des option
#numero du facture
numerofacture = tk.Label(news, text="N facture :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
numerofacture.place(x=400, y=150)
#ajouter produit
produitajouter = tk.Label(news, text="Produit    :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
produitajouter.place(x=400, y=200)
#quantite
quantite = tk.Label(news, text="Quantite  :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
quantite.place(x=400, y=250)
#prix
prix = tk.Label(news, text="Prix         :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
prix.place(x=400, y=300)
#numro fcature
numerofacture = tk.Entry(news)
numerofacture.insert(10, "")
numerofacture.place(x=550, y=155)
#produit
autre = tk.Entry(news)
autre.insert(10, "")
autre.place(x=550, y=205)
#quantite
quantitezone = tk.Entry(news)
quantitezone.insert(10, "")
quantitezone.place(x=550, y=255)
#prix
prixezone = tk.Entry(news)
prixezone.insert(10, "")
prixezone.place(x=550, y=305)
#butoon ajouter
produitajouterbutton = tk.Button(news, text='Ajouter', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white")
produitajouterbutton.place(x=200, y=500)
#button annuler
produitannulerbutton = tk.Button(news, text='Annuler', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white", command=reset)
produitannulerbutton.place(x=600, y=500)
#page export
#ajouter produit
produitajouter = tk.Label(exp, text="Produit    :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
produitajouter.place(x=400, y=150)
#quantite
quantite = tk.Label(exp, text="Quantite  :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
quantite.place(x=400, y=200)
#prix
prix = tk.Label(exp, text="Prix         :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
prix.place(x=400, y=250)
#produit
exportproduit = tk.Entry(exp)
exportproduit.insert(10, "")
exportproduit.place(x=550, y=155)
#quantite
exportquantite = tk.Entry(exp)
exportquantite.insert(10, "")
exportquantite.place(x=550, y=205)
#prix
exportprix = tk.Entry(exp)
exportprix.insert(10, "")
exportprix.place(x=550, y=255)
#butoon ajouter
produitajouterbutton = tk.Button(exp, text='Ajouter', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white", command=exportfonction)
produitajouterbutton.place(x=200, y=500)
#button annuler
produitannulerbutton = tk.Button(exp, text='Annuler', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white", command=resetexport)
produitannulerbutton.place(x=600, y=500)
#page rechrcher
#serach zone button
search_zone = tk.Entry(r)
search_zone.insert(10, "chercher un personne")
search_zone.place(x=1200, y=117)
r1 = tk.Label(dashbroad, text="Produit a Rechercher :", font=("Arial", 20), fg="#683FA9", background="#BBBBBB")
r2 = tk.Label(dashbroad, text="Nombre des Pièce Trouve :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
search_zone.bind("<FocusIn>", on_entry_click)
#rectangele du tableu du bord
dashbroadstatic1 = tk.Button(dashbroad, text='Nombre des personne abonnés : 300', height=8, width=30,  background="#683FA9", state='disabled')
dashbroadstatic2 = tk.Button(dashbroad, text='Personnes dans la salle : 1500', height=8, width=30, background="#683FA9", state='disabled')
dashbroadstatic3 = tk.Button(dashbroad, text='', height=8, width=30, background="#683FA9", state='disabled')
produitarecherche  = tk.Entry(dashbroad, background="#BBBBBB", bd="0", fg="#683FA9", font=("Arial", 16), highlightbackground="#BBBBBB")
dashbroadstatic1.place(x=100, y=350)
dashbroadstatic2.place(x=400, y=350)
dashbroadstatic3.place(x=700, y=350)
#xyz
logout = tk.Button(r, text='Déconnexion', highlightbackground="#DFD800", font=("Helvetica 15 bold", 10),  width=10, background="#959100", fg="black", command=r.destroy, activebackground="#D3CD00", activeforeground="black")
logout.place(x=1380, y=20)
#page setting

#date
date = datetime.date.today()
date = canvas.create_text(200, 120, text=date, fill="white", font='Helvetica 15 bold')
canvas.pack()
r.mainloop()



