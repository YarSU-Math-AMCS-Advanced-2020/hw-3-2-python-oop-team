from dataclasses import dataclass


@dataclass
class Request:
    action: str
    args: dict
