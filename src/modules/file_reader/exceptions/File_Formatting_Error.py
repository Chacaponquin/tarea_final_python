
class FileFormattingError(Exception):
    def __init__(self, message="Existe un error con el formato del archivo"):
        self.message = message
        super().__init__(self.message)


