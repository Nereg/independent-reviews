# A dumper for IS system of STU
# Should dump at least subjects
# Minimal Shipping Product: dump every Bc subject for FIIT
import asyncio
import dataclasses
import os
import sys

import aiohttp
import asyncpg
import bs4
from bs4 import BeautifulSoup

sys.path.insert(
    1, os.path.join(sys.path[0], "../..")
)  # PATH hack to import out standard things

from config import GlobalConfig
from sql import subjects, util

DRY_RUN = False


@dataclasses.dataclass
class Subject:
    code: str
    name: str
    ais_id: int
    stage: int  # 1 for Bc, 2 for Ing, -1 for unknown


async def fetch(session: aiohttp.ClientSession) -> str:
    """
    Fetches whatever whole page from AIS you specified with parameters
    """
    payload = {  # STU FIIT, ZS 24/25, faculty 1, semester 1
        "ustav": 0,
        "vypsat": "Vypísať predmety",
        "fakulta": 21070,
        "obdobi": 361,
        "obdobi_fak": 691,
        "jak": "dle_pracovist",
        "lang": "sk",
    }
    res = await session.post("https://is.stuba.sk/katalog/index.pl", data=payload)
    return await res.text()


def parseLink(link: bs4.Tag) -> Subject | None:
    comb_name = link.text
    href = link["href"]
    # some links are JS buttons, protect from them
    if "syllabus.pl" not in href:
        return None
    # print(href)
    sid = int(href.split("predmet=")[1].split(";")[0])
    code = comb_name.split(" ", maxsplit=1)[0]
    name = comb_name.split(" ", maxsplit=1)[1]
    char_stage = code.split("_")[-1]
    # print(char_stage)
    if char_stage in ["UISI", "UPAI", "IB", "ISS"]:  # VPP_IB, VPP_ISS
        stage = 2
        print("Weird subject!")
    elif char_stage in [
        "L",
        "TK",
        "Z",
    ]:  # TK_L + TK_Z +  VYBER_TK Výberová telesná kultúra
        stage = 1
    elif char_stage == "B":
        stage = 1
    elif char_stage == "I":
        stage = 2
    else:
        print(char_stage)
        raise ValueError()
    return Subject(code, name, sid, stage)


async def insertSubject(input: Subject, querier: subjects.AsyncQuerier) -> None:
    await querier.create_subject(
        subjects.createSubjectParams(
            input.name,
            facultyId=1,
            aisid=input.ais_id,
            stage=input.stage,
            semester=1,
            aisCode=input.code,
        )
    )


async def main():
    cfg = GlobalConfig.load()
    con = await asyncpg.connect(cfg.db.dsn)
    querier = subjects.AsyncQuerier(util.convert(con))
    ses = aiohttp.ClientSession()
    text = await fetch(ses)
    print(len(text))
    soup = BeautifulSoup(text, "html.parser")
    thelinks = soup.find("form").find_all("a")  # somebody had a stroke naming this form
    # print(thelinks)
    for link in thelinks:
        sub = parseLink(link)
        print(sub)
        if sub is not None and not DRY_RUN:
            await insertSubject(sub, querier)
    await ses.close()
    # await ses.close()


if __name__ == "__main__":
    asyncio.run(main())
