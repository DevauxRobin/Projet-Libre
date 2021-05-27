### Enlever 1 essai au joueur
attempts -= 1
attemptsvar.set(f"{attempts} Tentatives")


# Variable stockant les tentatives
attemptsvar = tk.StringVar()
attemptsvar.set("? tentatives")


# Ajout du nombre de tentatives
attempts = tk.Label(window, textvariable=attemptsvar, bg=color)
attempts.place(x=250, y=10)


# Compteur de tentatives
attempts = 10