# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Vraag de gebruiker om steden in te voeren, gescheiden door een komma
steden = input("Typ de steden, gescheiden door een komma: ")

# Zet de invoer om naar een lijst en verwijder overtollige spaties
steden_lijst = [stad.strip() for stad in steden.split(",")]

# Sorteer de lijst in omgekeerde alfabetische volgorde
steden_lijst.sort(reverse=True)

# Print de gesorteerde lijst
print("Gesorteerde lijst in omgekeerde volgorde:")
for stad in steden_lijst:
    print(stad)
