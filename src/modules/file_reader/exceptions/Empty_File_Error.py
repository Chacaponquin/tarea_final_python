class EmptyFileError(Exception):
    def __init__(self, message="El archivo está vacío"):
        self.message = message
        super().__init__(self.message)


