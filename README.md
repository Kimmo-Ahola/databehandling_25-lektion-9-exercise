# Installation
1. Skapa virtuell miljö och aktivera den
1. pip install -r requirements.txt
1. kör alembic stamp base
1. kör alembic upgrade head

Om ni vill köra mysql istället:
1. alembic stamp base
1. radera migrationsfilen som finns i versions-mappen
1. byt ut url till mysql-url istället
1. kör alembic revision --autogenerate -m "initial"
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
