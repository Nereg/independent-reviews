# Code generated by sqlc. DO NOT EDIT.
# versions:
#   sqlc v1.27.0
#   sqlc-gen-better-python v0.4.2
"""Module containing models."""
from __future__ import annotations

__all__: collections.abc.Sequence[str] = (
    "Faculty",
    "Lector",
    "Permission",
    "Practitioner",
    "Review",
    "Subject",
    "Telegram",
    "User",
)

import dataclasses
import typing

if typing.TYPE_CHECKING:
    import collections.abc
    import datetime


@dataclasses.dataclass()
class Faculty:
    """Model representing Faculty.

    Attributes:
        id: int
        university: str
        name: str
    """

    id: int
    university: str
    name: str


@dataclasses.dataclass()
class Lector:
    """Model representing Lector.

    Attributes:
        id: int
        aisid: int | None
        name: str
        surname: str
    """

    id: int
    aisid: int | None
    name: str
    surname: str


@dataclasses.dataclass()
class Permission:
    """Model representing Permission.

    Attributes:
        userId: int
        permissions: int
    """

    userId: int
    permissions: int


@dataclasses.dataclass()
class Practitioner:
    """Model representing Practitioner.

    Attributes:
        id: int
        aisid: int | None
        name: str
        surname: str
    """

    id: int
    aisid: int | None
    name: str
    surname: str


@dataclasses.dataclass()
class Review:
    """Model representing Review.

    Attributes:
        id: int
        author: int
        text: str
        deleted: bool
        language: str
        subjectId: int
        lectorId: int | None
        practitionerId: int
        subjectRating: int
        lectorRating: int | None
        practitionerRating: int
        practitionerReview: str | None
        lectorReview: str | None
        yearBeginning: int
        timestamp: datetime.datetime
        mark: float
    """

    id: int
    author: int
    text: str
    deleted: bool
    language: str
    subjectId: int
    lectorId: int | None
    practitionerId: int
    subjectRating: int
    lectorRating: int | None
    practitionerRating: int
    practitionerReview: str | None
    lectorReview: str | None
    yearBeginning: int
    timestamp: datetime.datetime
    mark: float


@dataclasses.dataclass()
class Subject:
    """Model representing Subject.

    Attributes:
        id: int
        name: str
        facultyId: int
        aisid: int
        stage: int
        semester: int
        aisCode: str
    """

    id: int
    name: str
    facultyId: int
    aisid: int
    stage: int
    semester: int
    aisCode: str


@dataclasses.dataclass()
class Telegram:
    """Model representing Telegram.

    Attributes:
        telegramId: int
        userId: int
        chatId: int
    """

    telegramId: int
    userId: int
    chatId: int


@dataclasses.dataclass()
class User:
    """Model representing User.

    Attributes:
        id: int
        aisId: int | None
        facultyId: int | None
        eduEmail: str | None
        ISICNum: int | None
        registred: datetime.datetime
    """

    id: int
    aisId: int | None
    facultyId: int | None
    eduEmail: str | None
    ISICNum: int | None
    registred: datetime.datetime
