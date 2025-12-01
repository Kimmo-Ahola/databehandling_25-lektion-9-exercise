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
