import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect("Biblioteka.db")
cursor = conn.cursor()

# Pobranie wszystkich książek
cursor.execute("SELECT * FROM Ksiazki")
ksiazki = cursor.fetchall()

# Wyświetlenie wyników
print("📖 Lista książek:")
for ksiazka in ksiazki:
    print(f"ID: {ksiazka[0]}, Tytuł: {ksiazka[1]}, Autor: {ksiazka[2]}, Rok: {ksiazka[3]}, Gatunek: {ksiazka[4]}, Dostępność: {'Dostępna' if ksiazka[5] == 1 else 'Niedostępna'}")

conn.close()
