"""
Main function.

Created by: Dmytro Dziubenko
"""

from typing import NoReturn

from src.config import MONGODB_CONNECTION_STRING
from src.mongo_client import MongoAPIClient as Mongo


def connect() -> Mongo:
    """Connect to MongoDB server.

    Returns:
        Mongo: MongoDB client instance that have CRUD functions implemented.
    """
    return Mongo(MONGODB_CONNECTION_STRING)


def perform_actions(db: Mongo) -> None:
    """Hardcoded DB operations to demonstrate API possibilities.

    Args:
        db (Mongo): MongoDB client instance.
    """
    # enter your actions here
    pass


def close(db: Mongo) -> None:
    """Close MongoDB connection.

    Args:
        db (Mongo): MongoDB client instance.
    """
    db.mongodb_client.close()


def main():
    db = connect()
    perform_actions(db)
    close(db)


if __name__ == "__main__":
    main()
