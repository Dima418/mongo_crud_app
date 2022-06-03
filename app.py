"""
Main function.

To run application:
    $ git clone https://github.com/Dima418/mongo_crud_app.git
    $ cd mongo_crud_app.

    Linux/Ubuntu:
    $ export MONGO_URL=<connection string>
    $ python3 app.py

    Windows:
    $ set MONGO_URL=<connection string>
    $ python app.py

Created by: Dmytro Dziubenko
"""

from typing import NoReturn

from src.config import MONGODB_CONNECTION_STRING
from src.mongo_client import Mongo as Mongo


def connect() -> Mongo:
    """Connect to MongoDB server

    Returns:
        Mongo: MongoDB client instance that have CRUD functions implemented
    """

    return Mongo(MONGODB_CONNECTION_STRING)


def perform_actions(db: Mongo) -> NoReturn:
    """Start infinite loop for user to make DB operations

    Args:
        db (Mongo): MongoDB client instance
    """

    pass


def close(db: Mongo) -> None:
    """Close MongoDB connection

    Args:
        db (Mongo): MongoDB client instance
    """

    db.mongodb_client.close()


def main():
    db = connect()
    perform_actions(db)
    close(db)


if __name__ == "__main__":
    main()
