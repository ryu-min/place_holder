from place_holder.handlers import Handler

class FirstHandler(Handler):
    def handle(self) -> str:
        return "handler by first handler"

class SecondHandler(Handler):
    def handle(self) -> str:
        return "handler by second handler"
