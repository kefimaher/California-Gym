import tkinter as tk

def submit_subpage():
    entered_text = sub_entry.get()
    sub_result_label.config(text=f"You entered: {entered_text}")

def submit_mainpage():
    entered_text = main_entry.get()
    main_result_label.config(text=f"You entered: {entered_text}")

root = tk.Tk()
root.title("Nested Frames Example")

# Crée le frame principal (la page principale)
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack()

# Crée un label dans le frame principal
main_label = tk.Label(main_frame, text="Main Page")
main_label.pack()

# Crée un sous-frame (la sous-page)
sub_frame = tk.Frame(main_frame, padx=10, pady=10, bg="lightblue")
sub_frame.pack()

# Crée un label dans le sous-frame
sub_label = tk.Label(sub_frame, text="Sub Page", bg="lightblue")
sub_label.pack()

# Crée un entry et un bouton dans le sous-frame
sub_entry = tk.Entry(sub_frame)
sub_entry.pack()
sub_button = tk.Button(sub_frame, text="Submit Subpage", command=submit_subpage)
sub_button.pack()
sub_result_label = tk.Label(sub_frame, text="", bg="lightblue")
sub_result_label.pack()

# Crée un entry et un bouton dans le frame principal
main_entry = tk.Entry(main_frame)
main_entry.pack()
main_button = tk.Button(main_frame, text="Submit Mainpage", command=submit_mainpage)
main_button.pack()
main_result_label = tk.Label(main_frame, text="")
main_result_label.pack()

root.mainloop()
