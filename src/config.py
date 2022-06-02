"""
Configuration variables
"""

from os import environ
from pathlib import Path
from pymongo.errors import ConfigurationError


__all__ = ["BASE_DIR", "MONGODB_CONNECTION_STRING"]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Get MongoDB connection string from system environment variables
MONGODB_CONNECTION_STRING = environ.get("MONGO_URL")

if MONGODB_CONNECTION_STRING is None:
    raise ConfigurationError(
        "MongoDB URL is not defined in environment variables")
