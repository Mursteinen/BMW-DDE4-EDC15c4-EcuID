import os
import tkinter as tk
from tkinter import filedialog

# Opprett hovedvinduet
root = tk.Tk()
root.title("EcuRituals 0.1")
root.geometry('150x75+50+50')
root.resizable(False, False)

label = tk.Label(root, text="")
label.pack()

def open_file():
    # Åpne fil-dialogboks for å velge fil
    filepath = filedialog.askopenfilename()

    # Sjekk om filen eksisterer
    if not os.path.exists(filepath):
        tk.messagebox.showerror("Feil", "Filen eksisterer ikke.")
        return

    # Åpne filen i binærmodus og les innholdet som hex
    with open(filepath, "rb") as file:
        file.seek(0x7BFB4)  # int EDC15Version = 0x7BFB4; Dette er verdien som skal valideres da denne leser SW versjon
        long = file.read(6)
    print("")
    print(long)
    label.config(text=long)



# Opprett knapp for å åpne fil
open_file_button = tk.Button(root, text="Open File", command=open_file)
open_file_button.pack()

# Kjør hovedløkken
root.mainloop()