# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(Bfile, Btext):
    with open(Bfile, 'w', encoding='utf-8') as file:
        file.write(Btext + '\n')

my_tekst = "nog een test"
my_file = "opdrachten/090_functies/opdr_1/bestand.txt"
write_to_file(my_file, my_tekst)
