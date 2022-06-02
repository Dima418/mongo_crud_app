"""
Mixin class for retrieve operations
"""

from pymongo.database import Database, Collection
from pymongo.errors import ConnectionFailure


class RetrieveMixin:

    # Database related

    def select_db(self, db_name: str) -> None:
        self.db: Database = self.client[db_name]

        if self.db is None:
            raise ConnectionFailure(
                f"Database with the name '{db_name}' not found")

        print("Database selected successfully")

    # Collection related

    def select_collection(self, collection_name: str):
        if self.db is None:
            raise ConnectionFailure(
                "No database instance found. Try to select a new database")

        self.collection: Collection = self.db[collection_name]

        if self.collection is None:
            raise ConnectionFailure(
                f"Collection with the name '{collection_name}' not found")

        print("Collection selected successfully")
