import sqlite3

# Połączenie z bazą danych (automatyczne utworzenie pliku Biblioteka.db)
conn = sqlite3.connect("Biblioteka.db")
cursor = conn.cursor()

# Tworzenie tabeli
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ksiazki ( 
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        tytul VARCHAR(100) NOT NULL,
        autor VARCHAR(100) NOT NULL,
        rok_wydania INTEGER NOT NULL,
        gatunek VARCHAR(50) NOT NULL,
        dostepnosc INTEGER NOT NULL DEFAULT 1
    )
""")

conn.commit()
conn.close()

print("✅ Baza danych 'Biblioteka.db' została utworzona!")
