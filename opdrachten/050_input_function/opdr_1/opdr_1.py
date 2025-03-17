# Opdracht 1 input function
# Naam student:Mohsen Abaza
# Groep:expert iT systems en devices

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

  

a = float(input("Geef de lengte van de eerste zijde: "))
b = float(input("Geef de lengte van de tweede zijde: "))

# Pythagoras: c = √(a² + b²)
c =(a**2 + b**2)**0.5

print(f"\nDe lengte van de schuine zijde is: {c}")
    
