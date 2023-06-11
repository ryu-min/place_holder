import typing


class Handler(typing.Protocol):

    def handle(self) -> str:
        """"do something here"""


