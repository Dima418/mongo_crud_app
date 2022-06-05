"""
Mixin class for update operations.
"""

from typing import Sequence, Union, Optional, Any
from pymongo.results import UpdateResult


class UpdateMixin:
    """Class contains only functions for update operations for MongoDB.

    Functions:
        1. update(self, query_filter: dict[str, Any], update_filter: Union[dict[str, Any], Sequence[dict[str, Any]]], many: bool = False) -> None
    """

    def update(self, query_filter: dict[str, Any], update_filter: Union[dict[str, Any], Sequence[dict[str, Any]]], many: bool = False) -> None:
        """Update one or more documents that match the filter.

        Args:
            query_filter (dict[str, Any]): A query that matches the documents to update.
            update_filter (Union[dict[str, Any], Sequence[dict[str, Any]]]): The modifications to apply.
            many (bool, optional): If ``True`` then update many, else update one. Defaults to ``False``.
        """
        self.collection_connected()
        if not many:
            update_result: UpdateResult = self.collection.update_one(query_filter, update_filter)
        else:
            update_result: UpdateResult = self.collection.update_many(query_filter, update_filter)

        print(f"\nMatched {update_result.matched_count}. Modified {update_result.modified_count}")
