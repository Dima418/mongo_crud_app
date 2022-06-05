"""
Mixin class for delete operations
"""

from typing import Optional, Any


class DeleteMixin:
    """Class contains only functions for delete operations for MongoDB

    Functions:
        1. delete_documents(self, query_filter: Optional[dict[str, Any]] = None, many: bool = False) -> None
    """

    def delete_documents(self, query_filter: Optional[dict[str, Any]] = None, many: bool = False) -> None:
        """Delete documents according to `query_filter`

        Args:
            query_filter (dict[str, Any], optional): Filter for query. Defaults to None.
            many (bool, optional): If True then delete many, else delete one. Defaults to False.

        Raises:
            ValueError: Trying to delete one document without `query_filter`
        """

        self.collection_connected()

        if not many and query_filter is None:
            raise ValueError("Please specify query filter to delete one document")

        if not many:
            delete_result = self.collection.delete_one(filter=query_filter)
        else:
            delete_result = self.collection.delete_many(filter=query_filter)

        print(f"\nSuccessfully deleted {delete_result.deleted_count} document(s)")
