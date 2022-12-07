import tkinter as tk

# window
window = tk.Tk()
window.title("Password GUI")
window.minsize(width=800, height=600)


# Label                                     font ,  size, type
label = tk.Label(text="New Text", font=("Arial", 24, "bold"))
label.pack()  # Placing label on the screen

# Button


def button_clicked():

    label.config(text=input.get())


button = tk.Button(text="Click ME", command=button_clicked)
button.pack()

# Entry

input = tk.Entry(width=20)
input.pack()


# Mainloop keeping window open
window.mainloop()
