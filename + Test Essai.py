### Enlever 1 essai au joueur
attempt -= 1
attempts.set(f"{attempts} Tentatives")


# Variable stockant les tentatives
attempts = tk.StringVar()
attempts.set("17 tentatives")


# Ajout du nombre de tentatives
attempt = tk.Label(window, textvariable=attempts, bg=color)
attempt.place(x=250, y=10)
attempts = tk.Label(window, textvariable=time, bg=color)
attempts.place(x=20, y=20)


# Compteur de tentatives
attempt = 17
