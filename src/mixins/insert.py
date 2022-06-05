"""
Mixin class for insert operations.
"""

from typing import Iterable, Union, Optional, Any
from bson.raw_bson import RawBSONDocument
from pymongo.results import InsertOneResult, InsertManyResult


class InsertMixin:
    """Class contains only functions for insert operations for MongoDB.

    Functions:
        1. insert_one(self, document: dict[str, Any] | RawBSONDocument) -> None
        2. insert_many(self, documents: Iterable[dict[str, Any] | RawBSONDocument]) -> None
    """

    def insert_one(self, document: Union[dict[str, Any], RawBSONDocument]) -> None:
        """Insert a single document.

        Args:
            document (dict[str, Any] | RawBSONDocument, optional): The document to insert.
        """
        self.collection_connected()
        insert_one_result: InsertOneResult = self.collection.insert_one(document)
        print(f"\nSuccessfully inserted document with `_id`: {insert_one_result.inserted_id}")

    def insert_many(self, documents: Iterable[Union[dict[str, Any], RawBSONDocument]]) -> None:
        """Insert an iterable of documents.

        Args:
            documents (Iterable[dict[str, Any]  |  RawBSONDocument]): An iterable of documents to insert.
        """
        self.collection_connected()
        insert_many_result: InsertManyResult = self.collection.insert_many(documents)
        print("")
        for inserted_id in insert_many_result.inserted_ids:
            print(f"Successfully inserted document with `_id`: {inserted_id}")
