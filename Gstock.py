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
 exp.place(x=1500, y=800)
 produitarecherche.place(x=1500, y=800)
 r1.place(x=1500, y=800)
 r2.place(x=1500, y=800)
 r3.place(x=1500, y=800)
 dashbroadstatic1.place(x=100, y=350)
 dashbroadstatic2.place(x=400, y=350)
 dashbroadstatic3.place(x=700, y=350)
 search_zone.delete(0, "end")
 search_zone.insert(0, "")
 produitarecherche.delete(0, "end")
 a1.place(x=200, y=125)
 a2.place(x=300, y=90)
 a3.place(x=400, y=208)
 a4.place(x=500, y=176)
 a5.place(x=600, y=108)
 a6.place(x=700, y=70)
 a7.place(x=800, y=206)
 a8.place(x=900, y=223)
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
    if ((entered_text!="chercher un produit")and(entered_text!="")):
       produitarecherche.insert(10, entered_text)
       produitarecherche.place(x=280, y=105)
       r1.place(x=10, y=100)
       r2.place(x=10, y=150)
       r3.place(x=10, y=200)
       search_zone.delete(0, "end")
       search_zone.insert(0, "chercher un produit")
       news.place(x=1500, y=800)
       setting.place(x=1500, y=800)
       items.place(x=1500, y=800)
       document.place(x=1500, y=800)
       dashbroad.place(x=400, y=145)
       dashbroadstatic1.place(x=100, y=350)
       dashbroadstatic2.place(x=400, y=350)
       dashbroadstatic3.place(x=700, y=350)
       a1.place(x=1000, y=1000)
       a2.place(x=1000, y=1000)
       a3.place(x=1000, y=1000)
       a4.place(x=1000, y=1000)
       a5.place(x=1000, y=1000)
       a6.place(x=1000, y=1000)
       a7.place(x=1000, y=1000)
       a8.place(x=1000, y=1000)
def on_entry_click(event):
    if search_zone.get() == "chercher un produit":
       search_zone.delete(0, "end")  # Delete current text in the entry
#button reset
def reset():
    quantitezone.delete(0, tk.END)
    prixezone.delete(0, tk.END)
    autre.delete(0, tk.END)
    numerofacture.delete(0, tk.END)
def violette():
 canvas.create_rectangle(400, 800, 1500, 0, fill="white")
 canvas.create_rectangle(400, 70, 1500, 0, fill="#55259F")
 canvas.create_rectangle(0, 70, 400, 0, fill="#55259F")
 Title = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')
 canvas.create_line(400, 145, 1500, 145, fill="black", width=2)
 search = tk.Button(r, text='Chercher', width=10,  background="#683FA9", fg="white", command=on_submit, activebackground="#3D0E89", activeforeground="white")
 search.place(x=1380, y=113)
 test1 = tk.Button(r, text='Test', width=10, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white")
 test1.place(x=420, y=113)
 test2 = tk.Button(r, text='Test', width=10, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white")
 test2.place(x=550, y=113)
 logout = tk.Button(r, text='Déconnexion', highlightbackground="#683FA9",  width=10, background="#683FA9", fg="white", command=r.destroy, activebackground="#3D0E89", activeforeground="white")
 logout.place(x=1380, y=10)
def blue():
 canvas.create_rectangle(400, 800, 1500, 0, fill="white")
 canvas.create_rectangle(400, 70, 1500, 0, fill="#5DADE2")
 canvas.create_rectangle(0, 70, 400, 0, fill="#5DADE2")
 Title = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')
 canvas.create_line(400, 145, 1500, 145, fill="black", width=2)
 search = tk.Button(r, text='Chercher', width=10, background="#5DADE2", fg="white", command=on_submit, activebackground="#3D0E89", activeforeground="white")
 search.place(x=1380, y=113)
 test1 = tk.Button(r, text='Test', width=10, background="#5DADE2", fg="white", activebackground="#3D0E89", activeforeground="white")
 test1.place(x=420, y=113)
 test2 = tk.Button(r, text='Test', width=10, background="#5DADE2", fg="white", activebackground="#3D0E89", activeforeground="white")
 test2.place(x=550, y=113)
 logout = tk.Button(r, text='Déconnexion', highlightbackground="#683FA9",  width=10, background="#4F91BD", fg="white", command=r.destroy, activebackground="#3C7092", activeforeground="white")
 logout.place(x=1380, y=10)



 a1= tk.Button(dashbroad, text='80', height=8, width=1, background="#3C7092", state='disabled')
 a2= tk.Button(dashbroad, text='100', height=10, width=1, background="#3C7092", state='disabled')
 a3= tk.Button(dashbroad, text='30', height=3, width=1, background="#3C7092", state='disabled')
 a4= tk.Button(dashbroad, text='50', height=5, width=1, background="#3C7092", state='disabled')
 a5= tk.Button(dashbroad, text='90', height=9, width=1, background="#3C7092", state='disabled')
 a6= tk.Button(dashbroad, text='110', height=11, width=1, background="#3C7092", state='disabled')
 a7= tk.Button(dashbroad, text='30', height=3, width=1, background="#3C7092", state='disabled')
 a8= tk.Button(dashbroad, text='20', height=2, width=1,  background="#3C7092", state='disabled')
 a1.place(x=200, y=125)
 a2.place(x=300, y=90)
 a3.place(x=400, y=208)
 a4.place(x=500, y=176)
 a5.place(x=600, y=108)
 a6.place(x=700, y=70)
 a7.place(x=800, y=206)
 a8.place(x=900, y=223)
 dashbroadstatic1 = tk.Button(dashbroad, text='Total Piece : 3610', height=8, width=30,  background="#3C7092", state='disabled')
 dashbroadstatic2 = tk.Button(dashbroad, text='Nombre Des Commandes : 1500', height=8, width=30, background="#3C7092", state='disabled')
 dashbroadstatic3 = tk.Button(dashbroad, text='chiffre d"affaire : 366,500$', height=8, width=30, background="#3C7092", state='disabled')
 dashbroadstatic1.place(x=100, y=350)
 dashbroadstatic2.place(x=400, y=350)
 dashbroadstatic3.place(x=700, y=350)



def green():
 canvas.create_rectangle(400, 800, 1500, 0, fill="white")
 canvas.create_rectangle(400, 70, 1500, 0, fill="#72B62E")
 canvas.create_rectangle(0, 70, 400, 0, fill="#72B62E")
 Title = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')
 canvas.create_line(400, 145, 1500, 145, fill="black", width=2)
 search = tk.Button(r, text='Chercher', width=10, background="#72B62E", fg="white", command=on_submit, activebackground="#609928", activeforeground="white")
 search.place(x=1380, y=113)
 test1 = tk.Button(r, text='Test', width=10, background="#72B62E", fg="white", activebackground="#609928", activeforeground="white")
 test1.place(x=420, y=113)
 test2 = tk.Button(r, text='Test', width=10, background="#72B62E", fg="white", activebackground="#609928", activeforeground="white")
 test2.place(x=550, y=113)
 logout = tk.Button(r, text='Déconnexion', highlightbackground="#609928",  width=10, background="#609928", fg="white", command=r.destroy, activebackground="#609928", activeforeground="white")
 logout.place(x=1380, y=10)




 a1= tk.Button(dashbroad, text='80', height=8, width=1, background="#609928", state='disabled')
 a2= tk.Button(dashbroad, text='100', height=10, width=1, background="#609928", state='disabled')
 a3= tk.Button(dashbroad, text='30', height=3, width=1, background="#609928", state='disabled')
 a4= tk.Button(dashbroad, text='50', height=5, width=1, background="#609928", state='disabled')
 a5= tk.Button(dashbroad, text='90', height=9, width=1, background="#609928", state='disabled')
 a6= tk.Button(dashbroad, text='110', height=11, width=1, background="#609928", state='disabled')
 a7= tk.Button(dashbroad, text='30', height=3, width=1, background="#609928", state='disabled')
 a8= tk.Button(dashbroad, text='20', height=2, width=1,  background="#609928", state='disabled')
 a1.place(x=200, y=125)
 a2.place(x=300, y=90)
 a3.place(x=400, y=208)
 a4.place(x=500, y=176)
 a5.place(x=600, y=108)
 a6.place(x=700, y=70)
 a7.place(x=800, y=206)
 a8.place(x=900, y=223)
 dashbroadstatic1 = tk.Button(dashbroad, text='Total Piece : 3610', height=8, width=30,  background="#609928", state='disabled')
 dashbroadstatic2 = tk.Button(dashbroad, text='Nombre Des Commandes : 1500', height=8, width=30, background="#609928", state='disabled')
 dashbroadstatic3 = tk.Button(dashbroad, text='chiffre d"affaire : 366,500$', height=8, width=30, background="#609928", state='disabled')
 dashbroadstatic1.place(x=100, y=350)
 dashbroadstatic2.place(x=400, y=350)
 dashbroadstatic3.place(x=700, y=350)
















def red():
 canvas.create_rectangle(400, 800, 1500, 0, fill="white")
 canvas.create_rectangle(400, 70, 1500, 0, fill="#C65680")
 canvas.create_rectangle(0, 70, 400, 0, fill="#C65680")
 canvas.create_line(400, 145, 1500, 145, fill="black", width=2)
 Title = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')
 canvas.create_line(400, 145, 1500, 145, fill="black", width=2)
 search = tk.Button(r, text='Chercher', width=10, background="#C65680", fg="white", command=on_submit, activebackground="#A94A6E", activeforeground="white")
 search.place(x=1380, y=113)
 test1 = tk.Button(r, text='Test', width=10, background="#C65680", fg="white", activebackground="#A94A6E", activeforeground="white")
 test1.place(x=420, y=113)
 test2 = tk.Button(r, text='Test', width=10, background="#C65680", fg="white", activebackground="#A94A6E", activeforeground="white")
 test2.place(x=550, y=113)
 logout = tk.Button(r, text='Déconnexion', highlightbackground="#A94A6E",  width=10, background="#A94A6E", fg="white", command=r.destroy, activebackground="#954161", activeforeground="white")
 logout.place(x=1380, y=10)
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
canvas.create_rectangle(0, 70, 400, 0, fill="#55259F")
canvas.create_line(400, 145, 1500, 145, fill="#492089", width=2)
Title = canvas.create_text(200, 40, text="Stock Net", fill="white", font='Helvetica 15 bold')
# y = canvas.create_rectangle(400, 800, 1500, 146, fill="grey")
canvas.pack()
# button name + width
search = tk.Button(r, text='Chercher', width=10, background="#683FA9", fg="white", command=on_submit, activebackground="#3D0E89", activeforeground="white")
search.place(x=1380, y=113)
# button name + width
test1 = tk.Button(r, text='Test', width=10, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white")
test1.place(x=420, y=113)
# button name + width
test2 = tk.Button(r, text='Test', width=10, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white")
test2.place(x=550, y=113)
# button navbar a gauche vertical
#tableau du bord
dashbroad = tk.Button(r, text='Tableau du Bord', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=dashbroad_visibility)
dashbroad.place(x=1, y=180)
#Item list : afficher un page contien la list des produit dans la table (id,image,nom,prix,quantite)
items = tk.Button(r, text='Liste des produits', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=item_visibility)
items.place(x=1, y=230)
#Button New items : ajouter un produit dans la table (id,image,nom,prix,quantite)
news = tk.Button(r, text='Importer', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=news_visibility)
news.place(x=1, y=280)
#export
exp = tk.Button(r, text='Exporter', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=exp_visibility)
exp.place(x=1, y=330)
setting = tk.Button(r, text='Setting', width=46, background="#3E4146", fg="white", highlightbackground="#3E4146", activebackground="#683FA9", activeforeground="white", command=settings_visibility)
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
setting_page_text = tk.Label(setting, text="Contenu du page setting", font=("Arial", 24), fg="#683FA9", background="#BBBBBB")
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
autre = tk.Entry(exp)
autre.insert(10, "")
autre.place(x=550, y=155)
#quantite
quantitezone = tk.Entry(exp)
quantitezone.insert(10, "")
quantitezone.place(x=550, y=205)
#prix
prixezone = tk.Entry(exp)
prixezone.insert(10, "")
prixezone.place(x=550, y=255)
#butoon ajouter
produitajouterbutton = tk.Button(exp, text='Ajouter', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white")
produitajouterbutton.place(x=200, y=500)
#button annuler
produitannulerbutton = tk.Button(exp, text='Annuler', width=30, background="#683FA9", fg="white", activebackground="#3D0E89", activeforeground="white", command=reset)
produitannulerbutton.place(x=600, y=500)
#page rechrcher
#serach zone button
search_zone = tk.Entry(r)
search_zone.insert(10, "chercher un produit")
search_zone.place(x=1200, y=117)
r1 = tk.Label(dashbroad, text="Produit a Rechercher :", font=("Arial", 20), fg="#683FA9", background="#BBBBBB")
r2 = tk.Label(dashbroad, text="Nombre des Pièce Trouve :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
r3 = tk.Label(dashbroad, text="Prix de Chaque Pièce :", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
search_zone.bind("<FocusIn>", on_entry_click)
#rectangele du tableu du bord
dashbroadstatic1 = tk.Button(dashbroad, text='Total Piece : 3610', height=8, width=30,  background="#683FA9", state='disabled')
dashbroadstatic2 = tk.Button(dashbroad, text='Nombre Des Commandes : 1500', height=8, width=30, background="#683FA9", state='disabled')
dashbroadstatic3 = tk.Button(dashbroad, text='chiffre d"affaire : 366,500$', height=8, width=30, background="#683FA9", state='disabled')
produitarecherche  = tk.Entry(dashbroad, background="#BBBBBB", bd="0", fg="#683FA9", font=("Arial", 16), highlightbackground="#BBBBBB")
dashbroadstatic1.place(x=100, y=350)
dashbroadstatic2.place(x=400, y=350)
dashbroadstatic3.place(x=700, y=350)
#xyz
a1= tk.Button(dashbroad, text='80', height=8, width=1, background="#683FA9", state='disabled')
a2= tk.Button(dashbroad, text='100', height=10, width=1, background="#683FA9", state='disabled')
a3= tk.Button(dashbroad, text='30', height=3, width=1, background="#683FA9", state='disabled')
a4= tk.Button(dashbroad, text='50', height=5, width=1, background="#683FA9", state='disabled')
a5= tk.Button(dashbroad, text='90', height=9, width=1, background="#683FA9", state='disabled')
a6= tk.Button(dashbroad, text='110', height=11, width=1, background="#683FA9", state='disabled')
a7= tk.Button(dashbroad, text='30', height=3, width=1, background="#683FA9", state='disabled')
a8= tk.Button(dashbroad, text='20', height=2, width=1,  background="#683FA9", state='disabled')
a1.place(x=200, y=125)
a2.place(x=300, y=90)
a3.place(x=400, y=208)
a4.place(x=500, y=176)
a5.place(x=600, y=108)
a6.place(x=700, y=70)
a7.place(x=800, y=206)
a8.place(x=900, y=223)
image = Image.open("7.jpg")
nouvelle_taille = (500, 500)
image_redimensionnee = image.resize(nouvelle_taille)
image_tk = ImageTk.PhotoImage(image_redimensionnee)
label_image = tk.Label(r, image=image_tk)
#label_image.place(x=400, y=400)
logout = tk.Button(r, text='Déconnexion', highlightbackground="#683FA9",  width=10, background="#683FA9", fg="white", command=r.destroy, activebackground="#3D0E89", activeforeground="white")
logout.place(x=1380, y=10)
#page setting
setting_page_text = tk.Label(setting, text="Change la couleur de l'application", font=("Arial", 18), fg="#683FA9", background="#BBBBBB")
setting_page_text.place (x=10, y=100)
s1= tk.Button(setting, text='', height=2, width=3, background="#683FA9", activebackground="#683FA9", command=violette)
s2= tk.Button(setting, text='', height=2, width=3, background="#5DADE2", activebackground="#5DADE2", command=blue)
s3= tk.Button(setting, text='', height=2, width=3, background="#72B62E", activebackground="#72B62E", command=green)
s4= tk.Button(setting, text='', height=2, width=3, background="#C65680", activebackground="#C65680", command=red)
s1.place(x=0, y=150)
s2.place(x=100, y=150)
s3.place(x=200, y=150)
s4.place(x=300, y=150)
r.mainloop()



