from place_holder.handler_storage import FirstHandler, SecondHandler
from place_holder.handlers import Handler


def printHandlerInfo(handler: Handler):
    print(handler.handle())

f = FirstHandler()
s = SecondHandler()

printHandlerInfo(f)
printHandlerInfo(s)


