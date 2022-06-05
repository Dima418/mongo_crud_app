"""
Mixin class for retrieve operations
"""

from pprint import pprint
from pymongo.database import Database, Collection
from pymongo.errors import ConnectionFailure
from typing import Optional, Any


class RetrieveMixin:
    """Class contains only functions that retrieve data from MongoDB

    Functions:
        1. print_dbs(self) -> None
        2. print_collections(self, query_filter: Optional[dict[str, Any]] = None) -> None
        3.
    """

    def print_dbs(self) -> None:
        """Print all databases names
        """

        self.client_connected()

        db_names: list[str] = self.mongodb_client.list_database_names()

        print("\nAll databases:")

        for i, db_name in enumerate(db_names):
            print("\t", f"{i}. {db_name}")

    def print_collections(self, query_filter: Optional[dict[str, Any]] = None) -> None:
        """Print all collections names

        Args:
            query_filter (dict[str, Any], optional): Filter for query. Defaults to None.
        """

        self.db_connected()

        collections_names: list[str] = self.db.list_collection_names(filter=query_filter)

        print(f"\nAll collections of database '{self.db.name}':")

        for i, collections_name in enumerate(collections_names):
            print("\t", f"{i}. {collections_name}")

    def print_documents(self, query_filter: Optional[dict[str, Any]] = None) -> None:
        """Print only documents that matches filter.

        If filter is None, then prints all documents in collection

        Args:
            query_filter (dict[str, Any], optional): Filter for query. Defaults to None.
        """

        self.collection_connected()

        documents = self.collection.find(filter=query_filter)

        print(f"\nAll documents of collection '{self.collection.name}':")

        for i, document in enumerate(documents):
            print("\t", f"{i}. {document}")
