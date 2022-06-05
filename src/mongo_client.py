"""
Class to perform CRUD operations for Mongo database
"""

from .mixins.connect import ConnectMixin
from .mixins.retrieve import RetrieveMixin
from .mixins.delete import DeleteMixin


# TODO: use dataclasses

class Mongo(ConnectMixin, RetrieveMixin, DeleteMixin):

    def __init__(
            self,
            mongodb_url: str,
            db_name: str = None,
            collection_name: str = None
        ) -> None:
        self.connect_client(mongodb_url)
        self.connect_db(db_name)
        self.connect_collection(collection_name)
