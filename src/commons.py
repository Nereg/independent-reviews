import enum
from typing import Self


class Faculty(enum.IntEnum):
    FIIT = 1
    FEI = 2
    SvF = 3
    SjF = 4
    FCHPT = 5
    FAD = 6
    MFT = 7
    UM = 8

    @classmethod
    def from_str(cls, name: str) -> Self:
        return cls[name.upper()]


class Semester(enum.IntEnum):
    ZS = 1
    LS = 2

    @classmethod
    def from_str(cls, name: str) -> Self:
        return cls[name.upper()]


class Stage(enum.IntEnum):
    BC = 1
    ING = 2
