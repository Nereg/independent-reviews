from __future__ import annotations

import abc
import dataclasses
import tomllib
from typing import Any, Self

CONFIG_PATH = "./configs/config.toml.secret"


class BaseConfig(abc.ABC):
    def load(self, input: dict[str, Any]) -> Self:
        raise NotImplementedError


@dataclasses.dataclass()
class DbConfig(BaseConfig):
    dsn: str

    @classmethod
    def load(cls, input: dict[str, Any] | None = None) -> Self:
        if input is None:
            raise ValueError("Input config is empty!")
        dsn = input["dsn"]
        return cls(dsn)


@dataclasses.dataclass()
class TelegramConfig(BaseConfig):
    token: str

    @classmethod
    def load(cls, input: dict[str, Any] | None = None) -> Self:
        if input is None:
            raise ValueError("Input config is empty!")
        dsn = input["token"]
        return cls(dsn)


@dataclasses.dataclass()
class GlobalConfig(BaseConfig):
    """
    Global config class. Throws an error, if anything is missing
    """

    version: str
    logging_level: str
    debug: bool
    db: DbConfig
    telegram: TelegramConfig

    @classmethod
    def load(cls, input: dict[str, Any] | None = None) -> GlobalConfig:
        with open(CONFIG_PATH, "rb") as config_file:
            data = tomllib.load(config_file)
            db = DbConfig.load(data["db"])
            tg = TelegramConfig.load(data["telegram"])
            # telegram = TelegramConfig.load(data["telegram"])
            # sources = SourcesConfig.load(data["sources"])
            # database = DatabaseConfig.load(data["database"])
            version = data["version"]
            logging_level = data["logging_level"]
            debug = bool(data["debug"])
            return cls(version, logging_level, debug, db, tg)
