from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Response:
    class Type(Enum):
        BOOL = auto()
        LIST = auto()
        DICT = auto()

    type: Type
    data: bool | list | dict
