# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn" : ["nederland", "duitsland", "Frankrijk"],
    "maas" : ["nederland", "belgië", "duitsland"],
    "nijl" : ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Print de naam van de 1e rivier en het 2e land
print(f"de riviren {rivieren[0].capitalize()}stroom onder andere door {rivier_info[rivieren[0]][1].capitalize()} ")

# Print de naam van de 2e rivier en het 1e land
print(f"De rivieren {rivieren [1].capitalize()} stroom onder andere doot {rivier_info [rivieren [1]][0].capitalize()}")