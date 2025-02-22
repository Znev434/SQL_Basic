import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect("Biblioteka.db")
cursor = conn.cursor()

# Lista książek do dodania
ksiazki = [
    ("Wiedźmin: Ostatnie Życzenie", "Andrzej Sapkowski", 1993, "Fantasy", 1),
    ("Duma i uprzedzenie", "Jane Austen", 1813, "Romans", 1),
    ("1984", "George Orwell", 1949, "Sci-Fi", 1),
    ("Zbrodnia i kara", "Fiodor Dostojewski", 1866, "Dramat", 1),
    ("Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 1)
]

# Wstawienie danych do tabeli
cursor.executemany("INSERT INTO Ksiazki (tytul, autor, rok_wydania, gatunek, dostepnosc) VALUES (?, ?, ?, ?, ?)", ksiazki)

conn.commit()
conn.close()

print("📚 Książki dodane do bazy!")
