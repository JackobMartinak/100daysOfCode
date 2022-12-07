from tkinter import Tk, Canvas, PhotoImage

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
# window.minsize(width=500, height=500)
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(
    file="C:\\Users\\Repik\\OneDrive - Slovenská technická univerzita v Bratislave\\Python 100 days\\Day 29\\logo.png"
)
canvas.create_image(100, 100, image=logo_img)
canvas.pack()


window.mainloop()
