import dataclasses
from datetime import date, datetime
from typing import Self

import aiohttp
from bs4 import BeautifulSoup

from commons import Faculty


@dataclasses.dataclass
class ISICInfo:
    AISId: int
    ISICChipId: int
    faulty: Faculty
    valid: bool
    name: str
    surname: str
    validDate: date


class ISICVerifier:
    def __init__(self, session: aiohttp.ClientSession):
        self.http = session

    @classmethod
    async def create(cls, session: aiohttp.ClientSession) -> Self:
        return cls(session)

    async def _fetch(self, ISICNum: str) -> str:
        payload = {"lang": "en", "cislo": ISICNum, "valid": "Search"}
        req = await self.http.post(
            "https://is.stuba.sk/karty/platnost.pl", data=payload
        )
        return await req.text()

    async def verify(self, ISICNum: str) -> None:
        page = await self._fetch(ISICNum)
        # print(page)
        if "Found card" not in page:
            raise ValueError("No card found!")
        parsed = BeautifulSoup(page, "html.parser")
        rows = parsed.find_all("tbody")[1].find_all("td")
        # print(rows)
        AISLink = rows[1].b.a["href"]
        AISId = int(AISLink.split("=")[1].split(";")[0])
        fullName = rows[1].b.a.text
        facultyn = rows[1].b.text.split("-")[1].split(" ")[1]
        validUntil = rows[5].text
        validUntil = datetime.strptime(validUntil, "%m/%d/%Y").date()
        ISICChipNum = int(rows[9].text.replace("\xa0", ""))
        # print(AISId)
        # print(fullName)
        # print(facultyn)
        # print(validUntil)
        # print(ISICChipNum)
        isValid = datetime.now().date() < validUntil
        trueFaculty = Faculty.from_str(facultyn)
        return ISICInfo(
            AISId,
            ISICChipNum,
            trueFaculty,
            isValid,
            fullName.split(" ")[0],
            " ".join(fullName.split(" ")[1:]),
            validUntil,
        )
