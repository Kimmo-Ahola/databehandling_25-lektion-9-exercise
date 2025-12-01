from sqlalchemy.orm import Session

class Seeding():

    """
    Check if the tables are empty (count is 0).
    If they are empty:
        create three authors
        then add books
        then add reviews to the books
    
    """
    @staticmethod
    def seed_database(session: Session):
        raise NotImplementedError("Seeding is not implemented yet")
        