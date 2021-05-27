###On importe le module "time" pour pouvoir moduler le temps du jeu
import time


time.sleep(2)


### Récupération du temps à l'instant T
temps = time.time()


### Temps restant
tempsvar = tk.StringVar()
tempsvar.set("60s")
tentativestxt = tk.Label(window, textvariable=tempsvar, bg=color)
tentativestxt.place(x=20, y=20)

