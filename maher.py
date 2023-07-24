import tkinter as tk
from tkinter import RIGHT

from PIL import ImageTk, Image
r = tk.Tk()
r.title('MY Iptv')
# Load the image
img = Image.open('/home/test/Desktop/gitproject/IPTV/assets/1.jpg')
# logo_image.resize((90,50), resample=Image.LANCZOS)
bg = ImageTk.PhotoImage(img)

    #    logo_image = Image.open(get_resource_path ("assets/act2.png"))
     #   self.resized_logo = logo_image.resize((90,50), resample=Image.LANCZOS)
    #    self.logo_image = ImageTk.PhotoImage(self.resized_logo)

# Create a label with the image and add it to the window
r.geometry("1000x1000")
background_label = tk.Label(r, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(r, text='Close', width=25, command=r.destroy)
button.place(x=400,y=400)
#button.pack(side=RIGHT, padx=200, pady=50)
r.mainloop()


