### On importe le module random pour générer des nombres aléatoires et le module tkinter pour l'interface
import random
import tkinter as tk


def test(event=None):
    global enter_number, random_number, attempts, infos


### Récupérer le nombre
    number = enter_number.get()


### Tester si le caractère est un chiffre décimal
    if number.isdigit():


### Modifier le nombre en entier
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
        infos.set("Entre un nombre entre 1 et 50 :")


### Sélection du nombre
random_number = random.randint(1, 50)


### Fenêtre Tkinter as TK
window = tk.Tk()
window.geometry("600x300")
window.title("Au plus proche")
window.resizable(width=False, height=False)
frame = tk.Frame(window)
frame.pack(expand=True)


### Fenêtre Tkinter as Tk pour l'écriture
enter_number = tk.Entry(frame)
enter_number.bind('<Return>', test)
enter_number.focus()
enter_number.pack()
button = tk.Button(frame, text="Validate", command=test)
button.pack()
infos = tk.StringVar()
infos.set("Bonne chance ^^!")


### Tout exécuter pour tout afficher
window.mainloop()