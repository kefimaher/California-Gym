import tkinter as tk
import pandas as pd

df = pd.DataFrame()
# print(df)


from PIL import ImageTk, Image
r = tk.Tk()

r.title('MY Iptv')

img = Image.open('/home/test/Desktop/gitproject/GStock/assets/Photos/1.jpeg')

bg = ImageTk.PhotoImage(img)


r.geometry("1500x800")
background_label = tk.Label(r, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(r, text='Close', width=10, command=r.destroy)
button.place(x=1380,y=10)

button = tk.Button(r, text='Close', width=10, command="")
button.place(x=10,y=10)









r.mainloop()


