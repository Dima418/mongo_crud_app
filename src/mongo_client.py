"""
Class to perform CRUD operations for Mongo database
"""

from pymongo import MongoClient

from .mixins.retrieve import RetrieveMixin


class Mongo(RetrieveMixin):

    def __init__(self, mongodb_url: str, db_name: str = None):
        self.mongodb_client: MongoClient = MongoClient(mongodb_url)

        # ping client to check if it is avaliable
        # throws: ConnectionError
        self.mongodb_client.admin.command("ping")

        if db_name is not None:
            self.select_db(db_name)
