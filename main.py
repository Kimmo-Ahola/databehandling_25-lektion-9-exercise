from typing import List
from models.author import Author
from seeding import Seeding
from database.db import My_Session
from repositories.author_repository import AuthorRepository


if __name__ == "__main__":
    author_repo = AuthorRepository()
    with My_Session() as session:
        Seeding.seed_database(session)

    with My_Session() as session:
        all_authors: List[Author] = author_repo.get_all(session)

        print("Här är alla författare i databasen: ")

        for author in all_authors:
            print(author)
        try:
            user_choice = int(
                input("Vilken författares information vill du se? Ange id: ")
            )
            author = author_repo.get_by_id(user_choice, session)
            if author:
                # lazy loading here!
                print(author.books)
        except:
            print("Du måste ange en siffra!")

    with My_Session() as session:
        author_with_books = author_repo.get_authors_and_books(session)

        for author in author_with_books:
            # This is not lazy loaded!
            print(author, author.books)

    # reviews = reviews_for_book()
