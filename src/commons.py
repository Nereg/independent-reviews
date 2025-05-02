import enum
from typing import Self


class Faculty(enum.IntEnum):
    # fmt: off
    # black was for some reason wrapping those numbers into tuples
    FIIT = 1,
    FEI = 2,
    SvF = 3,
    SjF = 4,
    FCHPT = 5,
    FAD = 6,
    MFT = 7,
    UM = 8
    # fmt: on
    @classmethod
    def from_str(cls, name: str) -> Self:
        return cls[name.upper()]
