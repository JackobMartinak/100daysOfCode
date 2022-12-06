import tkinter as tk

# window
window = tk.Tk()
window.title("Password GUI")
window.minsize(width=800, height=600)

# Label                                     font ,  size, type
label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
label.pack()  # Placing label on the screen


# Mainloop keeping window open
window.mainloop()
