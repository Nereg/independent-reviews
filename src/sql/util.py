from asyncpg import Connection
from sqlalchemy.ext.asyncio import AsyncConnection


def convert(con: Connection) -> AsyncConnection:
    """
    A helper method to convert asyncpg to sqlc supported sqlalchemy imitations
    """
    return AsyncConnection(con)
