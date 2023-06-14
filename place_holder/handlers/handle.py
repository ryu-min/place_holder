import abc


class Handler(abc.ABC):

    @abc.abstractmethod
    def handle(self) -> str:
        """"do something here"""


