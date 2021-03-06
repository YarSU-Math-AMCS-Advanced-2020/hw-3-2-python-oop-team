from typing import Union
from dataclasses import dataclass
from enum import Enum, auto
from decimal import Decimal


@dataclass
class Response:
    class Type(Enum):
        BOOL = auto()
        LIST = auto()
        DICT = auto()
        DECIMAL = auto()

    type: Type
    data: Union[bool, list, dict, Decimal]
