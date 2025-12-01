# Installation
1. Skapa virtuell miljö och aktivera den
1. pip install -r requirements.txt
1. skapa databasen om ni inte har den
1. kör alembic stamp base
1. kör alembic upgrade head


# Övning

Ni har följande ERD som ska implementeras
<img width="961" height="328" alt="image" src="https://github.com/user-attachments/assets/dfb89d9a-70ea-483e-b0b3-e5eb2c1ff973" />

## Author
id: primary key INT

name: varchar(100)

## Book
id: primary key INT

title: varchar(200)

author_id: Foreign Key till PK i Author

## Review
id: primary key INT

rating: int

comment: Text

book_id: Foreign Key till PK I Book

## Relationships

Tänk på vilka relationer ni har mellan tabellerna och implementera dessa.
OBS! relationship är inte samma sak som Foreign Key även om de är relaterade. De är endast ett smidigare sätt att koppla ihop tabeller och gör det smidigare att hämta data.


## Uppgifter

1. Lägg till foreign key i Review-klassen
2. Kör en migration + update
3. Lägg till relationships
4. Implementera seeding-funktionen (se det andra repot för inspiration: https://github.com/Kimmo-Ahola/databehandling_25-lektion-9-relationships)
5. Implementera funktionerna som står i main.py
