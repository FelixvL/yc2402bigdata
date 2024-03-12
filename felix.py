import pandas
teller = 0

def mijnmethode(pokemonnaam):
    global teller
    pokemons = pandas.read_csv("Pokemon.csv")
    teller += 1
    print(teller)
    print(pokemons)
    for pok in pokemons["Name"]:
        if pok == pokemonnaam:
            return "gevonden"

    return "Pokemon niet gevonden " + str(4+5)


# print(mijnmethode())