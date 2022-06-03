"""
Mixin class with connection functions
"""

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import ConnectionFailure
from typing import Optional


class ConnectMixin:
    """Class contains only functions to connect to MongoDB client, database, collection

    Functions:

        Connection checker functions:
            1. client_connected(self) -> bool
            2. db_connected(self, db_name: Optional[str] = None) -> bool
            3. collection_connected(self, collection_name: Optional[str] = None) -> bool

        Connect functions:
            4. connect_client(self, mongodb_url: str) -> None
            5. connect_db(self, db_name: str) -> None
            6. connect_collection(self, collection_name: str) -> None
    """

    # Connection checker functions

    def client_connected(self) -> bool:
        """Check if MongoDB client instance is present and available

        Raises:
            ConnectionFailure: MongoDB client instance is absent or unavailable

        Returns:
            bool: True if MongoDB client is available
        """

        if self.mongodb_client is None:
            raise ConnectionFailure("Client is not connected. Please specify connection string as environment variable and try to run program again")

        try:
            # ping client to check if it is avaliable
            self.mongodb_client.admin.command("ping")
        except ConnectionFailure as e:
            raise

        return True

    def db_connected(self, db_name: Optional[str] = None) -> bool:
        """Check if database instance is present

        Args:
            db_name (str, optional): database name. Defaults to None.

        Raises:
            ConnectionFailure: database is None

        Returns:
            bool: True if database is available
        """

        self.client_connected()

        if self.db is None:
            if db_name is not None:
                raise ConnectionFailure(f"Database with the name '{db_name}' not found")

            raise ConnectionFailure("No database instance found. Try to select a new database")

        return True

    def collection_connected(self, collection_name: Optional[str] = None) -> bool:
        """Check if database collection instance is present

        Args:
            collection_name (str, optional): collection name. Defaults to None.

        Raises:
            ConnectionFailure: collection is None

        Returns:
            bool: True if collection is available
        """

        self.db_connected()

        if self.collection is None:
            if collection_name is not None:
                raise ConnectionFailure(f"Collection with the name '{collection_name}' not found")

            raise ConnectionFailure("No collection instance found. Try to select a new collection")

        return True

    # Connect functions

    def connect_client(self, mongodb_url: str) -> None:
        """Set MongoDB client instance

        Args:
            mongodb_url (str): MongoDB connection string
        """

        self.mongodb_client: MongoClient = MongoClient(mongodb_url)

        self.client_connected()

        print("Client connected successfully")

    def connect_db(self, db_name: Optional[str] = None) -> None:
        """Set database instance

        Args:
            db_name (str, optional): database name from MongoDB server. Defaults to None.

        Raises:
            ConnectionFailure: database with specified name is not found
        """

        if db_name is None:
            self.db: Database = None
        else:
            self.db: Database = self.mongodb_client[db_name]

            self.db_connected(db_name)

            print("Database selected successfully")

    def connect_collection(self, collection_name: Optional[str] = None) -> None:
        """Set collection instance to perform CRUD operations with it

        Args:
            collection_name (str, optional): collection name from database. Defaults to None.

        Raises:
            ConnectionFailure: collection with specified name is not found
        """

        if collection_name is None:
            self.collection: Collection = None
        else:
            self.collection: Collection = self.db[collection_name]

            self.collection_connected(collection_name)

            print("Collection selected successfully")
