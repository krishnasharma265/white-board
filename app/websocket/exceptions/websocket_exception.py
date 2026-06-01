class WebSocketExceptionBase(
    Exception
):

    def __init__(
        self,
        message: str
    ):

        self.message = message

class InvalidEventType(
    WebSocketExceptionBase
):
    pass

class UserNotFound(
    WebSocketExceptionBase
):
    pass

class RoomNotFound(
    WebSocketExceptionBase
):
    pass