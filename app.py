"""
Main function.

To run application:
    $ git clone https://github.com/Dima418/mongo_crud_app.git
    $ cd mongo_crud_app.
    $ export MONGO_URL=<connection string>
    $ python3 app.py

Created by: Dmytro Dziubenko
"""

from src.config import MONGODB_CONNECTION_STRING
from src.mongo_client import Mongo


def main():
    db = Mongo(MONGODB_CONNECTION_STRING)


if __name__ == "__main__":
    main()
