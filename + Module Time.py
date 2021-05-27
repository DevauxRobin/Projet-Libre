### On importe le module "time" pour pouvoir moduler le temps du jeu
import time


### Résultat
time.sleep(2)


### Récupération du temps à l'instant T
time = time.time()


### Temps restant
time = tk.StringVar()
time.set("60s")
tentativestxt = tk.Label(window, textvariable=time, bg=color)
tentativestxt.place(x=20, y=20)
