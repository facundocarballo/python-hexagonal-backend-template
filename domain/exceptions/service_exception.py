class ServiceException(Exception):
    _source: str
    _error_message: str

    def __init__(self, source: str, error_message: str):
        super().__init__(f"Error at {source}: {error_message}")
        self._source = source
        self._error_message = error_message