"""
Class to perform CRUD operations for Mongo database.
"""

from .mixins import (
    ConnectMixin,
    RetrieveMixin,
    DeleteMixin,
    InsertMixin,
    UpdateMixin
)


class MongoAPIClient(ConnectMixin, RetrieveMixin, DeleteMixin, InsertMixin, UpdateMixin):
    """MongoDB API class for CRUD operations."""

    def __init__(
            self,
            mongodb_url: str,
            db_name: str = None,
            collection_name: str = None
        ) -> None:
        self.connect_client(mongodb_url)
        self.connect_db(db_name)
        self.connect_collection(collection_name)
