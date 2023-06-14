def buscarpersonaje(listapersonajes, nombresuperheroe):
    for personaje in listapersonajes:
        if personaje[0] == nombresuperheroe:
            return personaje[1]
    return None

from collections import deque

def almacenar_grupo(listapersonajes, grupo):
    cola = deque()
    for personaje in listapersonajes:
        if personaje[2] == grupo:
            cola.append(personaje[0])
    return cola

def mostrarsuperheroesgrupo(listapersonajes, grupo):
    superheroes_grupo = []
    for personaje in listapersonajes:
        if personaje[2] == grupo:
            superheroes_grupo.append(personaje[0])
    superheroes_grupo.sort(reverse=True)
    for superheroe in superheroes_grupo:
        print(superheroe)

avengers = [
    ("Ant-Man", "Scott Lang", "Avengers", 2015),
    ("Black Widow" ,'Scarlett Johansson', "Avengers", 2010),
    ("Capitana Marvel", "Carol Danvers", "", 2012),
    ("Hawkeye", "Clint Barton", "Avengers", 1964),
    ("Iron Man", "Tony Stark", "Avengers", 1963),
    ("Spider-Man", "Peter Parker", "Avengers", 1962),
    ("Thor",'Chris Hemsworth', "Avengers", 1962),
    ("Star Lord", "Peter Quill", "Guardianes de la galaxia", 1976),
    ("Gamora",'Zoe Saldana', "Guardianes de la galaxia", 1975),
    ("Drax",'Dave Bautista', "Guardianes de la galaxia", 1973),
    ("Rocket Raccoon",'Bradley Cooper', "Guardianes de la galaxia", 2008),
    ("Groot",'Vin Diesel', "Guardianes de la galaxia", 1960),
    ("Mantis",'Pom Klementieff', "Guardianes de la galaxia", 1973),
    ("Nebula",'Karen Gillan', "Guardianes de la galaxia", 1985),
    ("Mr. Fantastic", "Reed Richards", "Los cuatro fantásticos", 1961),
    ("Invisible Woman", "Sue Storm", "Los cuatro fantásticos", 1961),
    ("Human Torch", "Johnny Storm", "Los cuatro fantásticos", 1961),
    ("The Thing", "Ben Grimm", "Los cuatro fantásticos", 1961)
]
nombresuperheroe = "Capitana Marvel"

nombrepersonaje = buscarpersonaje(avengers, nombresuperheroe)

if nombrepersonaje:
    print(f"El nombre del personaje de {nombresuperheroe} es: {nombrepersonaje}")
else:
    print(f"{nombresuperheroe} no se encuentra en la lista de personajes.")

grupo = "Guardianes de la galaxia"
cola_guardianes = almacenar_grupo(avengers, grupo)
cantidad_guardianes = len(cola_guardianes)

print(f"Hay {cantidad_guardianes} superhéroes en el grupo {grupo}:")
for superheroe in cola_guardianes:
    print(superheroe)

print("Superhéroes del grupo Los cuatro fantásticos:")
mostrarsuperheroesgrupo(avengers, "Los cuatro fantásticos")

print("Superhéroes del grupo Guardianes de la galaxia:")
mostrarsuperheroesgrupo(avengers, "Guardianes de la galaxia")

superheroes1960 = [personaje[0] for personaje in avengers if personaje[3] > 1960]

print("Superhéroes con año de aparición posterior a 1960: "),
for superheroe in superheroes1960:
    print (superheroe)

newlist = [("Vlanck Widow", "", "Avengers", 2010),
    ("Capitana Marvel", "Carol Danvers", "", 2012),
    ("Hawkeye", "Clint Barton", "Avengers", 1964),
    ("Iron Man", "Tony Stark", "Avengers", 1963),
    ("Spider-Man", "Peter Parker", "Avengers", 1962),
    ("Thor",'Chris Hemsworth', "Avengers", 1962)
    ]
for i in range(len(newlist)):
    if newlist[i][0] == "Vlanck Widow":
        newlist[i] = ("Black Widow", newlist[i][1], newlist[i][2], newlist[i][3])

print("Lista de personajes de Avengers en la nueva lista corregida:")
for personaje in newlist:
    print(personaje)

listaaux = [
    ("Black Cat", "Felicia Hardy", "SpiderMan", 2021),
    ("Hulk", "Bruce Banner", "Avengers", 2012),
    ("Rocket Racoonn", "Bradley Cooper", "Guardians de la Galaxia", 2014),
    ("Loki", "Tom Hiddleston", "Thor", 2011)
]

for personaje, actor, pelicula, año in listaaux:
    encontrado = False
    for p in avengers:
        if p[0] == personaje:
            encontrado = True
    if not encontrado:
        avengers.append((personaje, actor, pelicula, año))

print("Lista de personajes de Avengers con los personajes de la lista auxiliar agregados:")
for personaje in avengers:
    print(personaje)