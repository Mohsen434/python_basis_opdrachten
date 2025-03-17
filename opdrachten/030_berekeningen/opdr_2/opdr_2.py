# Opdracht 2 berekeningen
# Naam student:Mohsen Abaza
# Groep:Expert iTz system en device's

# Hier komt je code...

c = 60
f = 102
schakelen_tot_C = (f - 32) * 5 / 9
schakelen_tot_F = (c * 9 / 5) + 32

# Vraag de gebruiker om een keuze te maken
keuze = input("Typ de Fahrenheit temperatuur of de Celsius temperatuur (f of c): ").lower()

# Gebruiker kiest voor Fahrenheit invoer
if keuze == 'f':
    f_temp = float(input("Typ de Fahrenheit temperatuur: "))
    c_temp = (f_temp - 32) * 5 / 9
    print(f"De temperatuur in Celsius is: {c_temp:.1f}°C")

# Gebruiker kiest voor Celsius invoer
elif keuze == 'c':
    c_temp = float(input("Typ de Celsius temperatuur: "))
    f_temp = (c_temp * 9 / 5) + 32
    print(f"De temperatuur in Fahrenheit is: {f_temp:.1f}°F")

else:
    print("Ongeldige keuze. Typ 'f' voor Fahrenheit of 'c' voor Celsius.")