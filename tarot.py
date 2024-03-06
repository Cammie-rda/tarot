import random

#Implementar opciones del juego
arcanos_mayores=["El loco", "El mago", "La papisa", "La emperatriz", "El emperador", "El papa", "El enamorado", "El carro", "La justicia", "El ermitaño", "La rueda de la fortuna", "La fuerza", "El colgado", "La muerte", "La templanza", "La diabla", "La torre", "La estrella", "La luna", "El sol", "El juicio", "El mundo"]
arc_may= (f"{random.choice(arcanos_mayores)}")
#Descripcion arcanos menores
    #palos
palos=["oros", "copas", "bastos","espadas"]
arc_men = (f"{random.randint(1,10)} de {random.choice(palos)}")

#Cartas de la corte
cartas_de_la_corte=["Rey", "Reina", "Sota", "Caballero"]
car_cort = (f"{random.choice(cartas_de_la_corte)} de {random.choice(palos)}")

#Dar Bienvenida
print("Hola, consultante. Llegaste al tarot!")

#Preguntar al consultante su opción
opcion_consultante=input(
    "Sacar una carta:") .capitalize()
print("Ahora tienes que sacar una carta")


#Definir la opción del computador

tarot=[arc_may, car_cort, arc_men]
print(f"El tarot dice: {random.choice(tarot)}")

print("No olvides el libre albedrio")

