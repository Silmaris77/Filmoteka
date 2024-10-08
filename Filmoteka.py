import random
from datetime import datetime

class Media:
    def __init__(self, tytul, rok, gatunek):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.odtworzenia = 0
    
    def play(self):
        self.odtworzenia += 1

class Film(Media):
    def __str__(self):
        return f"{self.tytul} ({self.rok})"
    
class Serial(Media):
    def __init__(self, tytul, rok, gatunek, nr_sezonu, nr_odcinka):
        super().__init__(tytul, rok, gatunek)
        self.nr_sezonu = nr_sezonu
        self.nr_odcinka = nr_odcinka

    def __str__(self):
        return f"{self.tytul}, ({self.rok}), S{self.nr_sezonu:02d}E{self.nr_odcinka:02d}"

filmoteka =[]

def dodaj_film(tytul, rok, gatunek):
    filmoteka.append(Film(tytul, rok, gatunek))

def dodaj_serial(tytul, rok, gatunek, nr_sezonu, nr_odcinka):
    filmoteka.append(Serial(tytul, rok, gatunek, nr_sezonu, nr_odcinka))

def get_movies():
    return sorted([item for item in filmoteka if isinstance(item, Film)], key=lambda x: x.tytul)

def get_series():
    return sorted([item for item in filmoteka if isinstance(item,Serial)], key=lambda x:x.tytul)

def search(title):
    wynik = []
    for item in filmoteka:
        if item.tytul == title:
            wynik.append(item)
    if wynik:
        return f"Wynik:\n" + ",\n".join(str(i) for i in wynik)
    return "Nie ma"

def generate_views():
    item = random.choice(filmoteka)
    item.odtworzenia += random.randint(1,100)

def run_generate_views(views=20):
    for i in range(views):
        generate_views()


def top_titles(n, content_type=None):
    if content_type == "Filmy":
        items = get_movies()
    elif content_type == "Seriale":
        items = get_series()
    else:
        items = filmoteka
    return sorted(items, key=lambda x: x.odtworzenia, reverse=True)[:n]


print("Filmoteka")
dodaj_film("Forrest Gump", 1993, "Komedia")
dodaj_film("Skazani na Shawshank", 1993, "Dramat")
dodaj_serial ("Przyjaciele", 1999, "Komedia", 1, 14)
dodaj_serial ("Przyjaciele", 1999, "Komedia", 1, 17)
dodaj_serial ("Przyjaciele", 1999, "Komedia", 2, 1)
dodaj_serial ("Przyjaciele", 1999, "Komedia", 2, 11)
dodaj_serial ("Stawka większa niż życie", 1967, "Wojenny", 1, 12)
dodaj_film("Pulp Fiction", 1994, "Kryminalny")
dodaj_serial("The Simpsons", 1989, "Animowany", 1, 1)

f1 = Film("American Beauty", 1999, "Dramat")
filmoteka.append(f1)

for item in filmoteka:
    print(item)

run_generate_views()
print(f"Najpopularniejsze filmy i seriale dnia {datetime.now().strftime('%d.%m.%Y')}")
for item in top_titles(3):
    print (f"{item}, liczba odtworzeń: {item.odtworzenia}")

tytul = input("Wpisz tytuł, którego szukasz")
print(search(tytul))