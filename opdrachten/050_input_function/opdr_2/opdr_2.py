# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten =["Mohsen", "Paul", "Kees", "Marie", "Hilda"]
# Print de oorspronkelijke lijst van gasten
print ("Oorspronkelijke lijst van de gasten: ", gasten ,"\n") 

# Marie belt en zegt dat ze niet meer meegaat, dus verwijderen we haar\
gasten.remove("Marie")
#print Gewijzigde lijst
print( "Gewijzigde lijst",  gasten,"\n"  )

index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, "George")

# George belt en wil mee, hij wil naast Kees zitten
print("Niewue lijst ", gasten ,"\n")