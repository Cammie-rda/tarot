import random

#implementar opciones del juego
arcanos=["El loco", "El mago", "La papisa", "La emperatriz", "El emperador", "El papa", "El enamorado", "El carro", "La justicia", "El ermitaño", "La rueda de la fortuna", "La fuerza", "El colgado", "La muerte", "La templanza", "La diabla", "La torre", "La estrella", "La luna", "El sol", "El juicio", "El mundo"]

#dar Bienvenida
print("Hola, consultante. Llegaste al tarot!")
print("No olvides el libre albedrio")

#preguntar al consultante su opción
opcion_consultante=input(
    "Tienes que barajar:") .capitalize()
print("")

#definir la opción del computador
tarot= random.choice(arcanos)
print(f"El tarot dice:, '{tarot}'")


