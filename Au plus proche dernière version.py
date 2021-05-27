### On importe le module random pour générer des nombres aléatoires et le module tkinter pour l'interface
import random
import tkinter as tk


def test(event=None):
    global enter_number, random_number, infos


    ### Récupérer le nombre
    number = enter_number.get()


    ### Tester si le caractère est un chiffre décimal et modifier le nombre en entier
    if number.isdigit():
        number_proposition = int(number)


        ### Résultat
        if number_proposition < random_number:
            infos.set("Le nombre est plus haut.")
        elif number_proposition > random_number:
            infos.set("Le nombre est plus bas.")
        else:
            infos.set("Gagné !")
            window.destroy()
            quit()


    ### Annonce
    else:
        infos.set("Entre un nombre entre 1 et 75 :")


### Sélection du nombre et de la couleur de la fenêtre Tkinter
random_number = random.randint(1, 75)
color = "#B22222"


### Fenêtre Tkinter as TK
window = tk.Tk()
window.geometry("1200x600")
window.title("Au plus proche")
window.resizable(width=False, height=False)
window.config(bg=color)


frame = tk.Frame(window)
frame.pack(expand=True)


### Fenêtre Tkinter as Tk pour rentrer les informations et bouton Valider
enter_number = tk.Entry(frame)
enter_number.bind('<Return>', test)
enter_number.focus()
enter_number.pack()
button = tk.Button(frame, text="Valider", command=test)
button.pack()


### Texte d'information Tkinter
infos = tk.StringVar()
infos.set("Bonne chance ^^!")
information = tk.Label(window, textvariable=infos, bg=color)
information.place(x=550, y=220)


### Tout exécuter pour tout afficher
window.mainloop()