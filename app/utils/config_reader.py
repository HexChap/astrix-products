import json
from configparser import ConfigParser
from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str
    bot_id: int


@dataclass
class LoggingConfig:
    level: str
    rotation: str
    compression: str


@dataclass
class Config:
    bot: BotConfig
    logging: LoggingConfig
    admin_ids: list[int]


def load_config(path: str) -> Config:
    config = ConfigParser()
    config.read(path)

    bot_conf = config["bot_config"]
    logging_conf = config["logging_config"]
    misc_conf = config["misc_config"]

    admin_ids = json.loads(misc_conf["admin_ids"])

    bot_config = BotConfig(
        token=bot_conf["token"],
        bot_id=bot_conf["bot_id"]
    )

    logging_config = LoggingConfig(
        level=logging_conf["level"],
        rotation=logging_conf["rotation"].strip('"'),
        compression=logging_conf["compression"]
    )

    return Config(
        bot=bot_config,
        logging=logging_config,
        admin_ids=admin_ids
    )
